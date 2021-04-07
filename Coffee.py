import csv 
import numpy as np 


def Data_Source(dataPath):
    Coffee=[]
    Sleep =[]

    with open(dataPath) as f:
        csvReader= csv.DictReader(f)
        for row in csvReader:
           Coffee.append(float(row["Coffee in ml"]))
           Sleep.append(float(row["sleep in hours"]))
        return{"x":Coffee , "y" : Sleep}


def findCorrelation(data_source):
    Correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The correlation for the data is", Correlation[0,1])

def setup():
    dataPath = "Coffee.csv"
    data_source = Data_Source(dataPath)
    findCorrelation(data_source)

setup()