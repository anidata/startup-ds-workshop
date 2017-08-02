import luigi
import urllib2
import sqlite3
import pandas as pd



class extractData(luigi.Task):
	"""
	EXTRACT data from kaggle
	"""

	def output(self):
		return luigi.LocalTarget("titanic.csv")


	def run(self):
		#TODO Add Anidata repo when merged
		url = "https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv"
		response = urllib2.urlopen(url)
		with open("titanic.csv","wb") as f:
			f.write(response.read())



class transformData(luigi.Task):
	"""
	TRANSFORM data  by creating aggregates og classes
	"""
	def requires(self):
        	return extractData()

	def output(self):
        	return luigi.LocalTarget("agg.csv")

	def run(self):

		data = pd.read_csv("titanic.csv")
		agg = data.groupby("Pclass")["Pclass"].count()
		agg.to_csv("agg.csv")

class loadData(luigi.Task):
	"""
	LOAD Data into sql server
	"""
	def requires(self):
		return transformData()

	def run(self):
		data = pd.read_csv("agg.csv")
		conn = sqlite3.connect("database.sqlite")
		data.to_sql("aggregate",con = conn,if_exists="replace")
		conn.close()
if __name__ == '__main__':
    luigi.run()
