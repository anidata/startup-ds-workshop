import luigi
import urllib2
import pandas as pd



class pullData(luigi.Task):

    def requires(self):
        return []

    def output(self):
        return luigi.LocalTarget("titanic.csv")


    def run(self):

        url = "https://storage.googleapis.com/kaggle-competitions-data/kaggle/3136/train.csv?GoogleAccessId=competitions-data@kaggle-161607.iam.gserviceaccount.com&Expires=1501210675&Signature=UfZbwVp5ZIBIYii5aGSWQHcy8qSYjK9LCAEj4UqvRaDTNo2aFJgQMhrSiZGQDI2%2FY8MagKH8UVVjARuHhBv0HLJZ0Z9HYr38YanvdvD1bXzcyrSVvJI1W9A6sbDqmho88SoRi2FPFFk608j%2BexgwO9OxAg5jS8A480nv9dEZ6w%2FICiBujT%2B6dTycWRps9PjntMWdQKSbbrHS%2FdZKg73arO1o4hCN0UiQ0MQk3JgvtYE7GG2n0hR7deevTQrgFEVwHLdfLzsGCrwVYvnLr%2FmS2JEU9Rxa6FoTGvfmJEYegTbsg2lnjqbOViIKm3lOMwjN%2F%2B7olKSyMMeZs5QPf8%2FuWg%3D%3D"
        response = urllib2.urlopen(url)
        with open("titanic.csv","wb") as f:
            f.write(response.read())



class computeData(luigi.Task):

    def requires(self):
        return [pullData()]

    def output(self):
        return luigi.LocalTarget("agg.pk")

    def run(self):

        data = pd.read_csv("titanic.csv")
	agg = data.groupby("Pclass")["Pclass"].count()
        agg.to_pickle("agg.pk")


if __name__ == '__main__':
    luigi.run()
