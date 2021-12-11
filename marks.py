import csv
import numpy as np
import plotly.express as px

def get_data_source(data_path):
    student_marks=[]
    days_present=[]
    with open(data_path) as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            student_marks.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return{"x":days_present,"y":student_marks}

def findcorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("correlation between number of days present and marks is: ",correlation[0,1])

def plotfigure(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Days Present",y="Marks In Percentage")
        fig.show()

def setup():
    data_path="Student Marks vs Days Present.csv"
    data_source=get_data_source(data_path)
    findcorrelation(data_source)
    plotfigure(data_path)

setup()
