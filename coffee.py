from icecream import findCorrelation
import plotly.express as px
import csv
import numpy as np



def get_data_source(data_path):
    coffee=[]
    hours_of_sleep=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            hours_of_sleep.append(float(row["sleep in hours"]))

    return{"x":coffee,"y":hours_of_sleep}

def findcorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between coffee and hours of sleep is: ",correlation[0,1])

def plotfigure(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Coffee in ml",y="sleep in hours")
        fig.show()


def setup():
    data_path="cups of coffee vs hours of sleep.csv"
    data_source=get_data_source(data_path)
    findCorrelation(data_source)
    plotfigure(data_path)

setup()