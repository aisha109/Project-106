import csv 
import numpy as np 


def Data_Source(dataPath):
    Students_Marks=[]
    Days_Present =[]

    with open(dataPath) as f:
        csvReader= csv.DictReader(f)
        for row in csvReader:
            Students_Marks.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
        return{"x":Students_Marks , "y" : Days_Present}


def findCorrelation(data_source):
    Correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("The correlation for the data is", Correlation[0,1])

def setup():
    dataPath = "Students.csv"
    data_source = Data_Source(dataPath)
    findCorrelation(data_source)

setup()

        
    