import os
import sqlite3
from os import path as osp

import luigi
import pandas as pd
import requests


def abspath(filename):
    """
    Returns a path by appending the input filename to 
    the directory in which this file resides.
    
    Parameters
    ----------
    filename : str
    """
    return osp.join(osp.dirname(os.path.abspath(__file__)), filename)


class ExtractData(luigi.Task):
    """
    Extract data from Kaggle and write it to disk
    
    Parameters
    ----------
    data_source : str
        The remote location of the Titanic data set from
        the Kaggle competition
    output_name : str
        The local name of the dataset file
    """

    data_source = luigi.Parameter(
        default='https://raw.githubusercontent.com/agconti/'
                'kaggle-titanic/master/data/train.csv'
    )
    output_name = luigi.Parameter(default='titanic.csv')

    def output(self):
        path = abspath(self.output_name)
        return luigi.LocalTarget(path)

    def run(self):
        # TODO Add Anidata repo when merged
        response = requests.get(self.data_source)
        data = response.text
        with self.output().open('w') as f:
            f.write(data)


class TransformData(luigi.Task):
    """
    Transform data by creating aggregate counts of ticket
    classes
    
    Parameters
    ----------
    agg_output_name : str
        The local name of the output aggregate data file
    titanic_output_name : str
        THe local name of the titanic dataset with modified
        column names
    """

    agg_output_name = luigi.Parameter(default='aggregated.csv')
    titanic_output_name = luigi.Parameter(default='titanic_renamed.csv')

    def requires(self):
        return ExtractData()

    def output(self):
        agg_path = abspath(self.agg_output_name)
        tit_path = abspath(self.titanic_output_name)
        return luigi.LocalTarget(agg_path), luigi.LocalTarget(tit_path)

    def run(self):
        with self.input().open('r') as f:
            data = pd.read_csv(f)

        # lowercase all column names in prep for loading into database
        data.columns = [col.lower() for col in data.columns.astype(str)]
        # group classes and then count instances of each class
        agg = (data.groupby('pclass')['pclass'].count()
               .to_frame('count').reset_index())

        agg_target, tit_target = self.output()
        with agg_target.open('w') as af, tit_target.open('w') as tf:
            agg.to_csv(af, index=False)
            data.to_csv(tf, index=False)


class LoadData(luigi.Task):
    """
    Load source and aggregate into sql server
    """

    def requires(self):
        return TransformData()

    def run(self):
        agg, tit = self.input()
        with agg.open('r') as af, tit.open('r') as tf:
            agg_data = pd.read_csv(af)
            source_data = pd.read_csv(tf)

        conn = sqlite3.connect('database.sqlite')

        try:
            with conn:
                agg_data.to_sql('class_agg', con=conn, if_exists='replace')
                source_data.to_sql('titanic', con=conn, if_exists='replace')
        except:
            raise
        finally:
            conn.close()


if __name__ == '__main__':
    luigi.run(['LoadData', '--local-scheduler'])
