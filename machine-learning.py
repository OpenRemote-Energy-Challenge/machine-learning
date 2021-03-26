#Data visualisation python code
import pandas as pd
import matplotlib
import matplotlib.pyplot as pyplot
from sklearn.tree import DecisionTreeClassifier

"""def clean_data(dataset):
    dataset = dataset.drop(columns=['timestamp'])
    dataset.head()"""

if __name__ == "__main__":
   
    pd.set_option('display.max_rows', 10000)
    pd.set_option('display.max_columns', 10000)
    pd.set_option('display.width', 10000)

    solar_data = pd.read_csv("./SolarData.csv")

    solar_data['date'] = [datetime.split(' ')[0][2:].strip() for datetime in solar_data['timestamp']]
    solar_data['time'] = [datetime.split(' ')[1].strip() for datetime in solar_data['timestamp']]

    totalPower = solar_data.loc[solar_data['attribute_name'] == 'totalPower'].sort_values(by=['date', 'time'], ascending=True)
    totalEnergy = solar_data.loc[solar_data['attribute_name'] == 'totalEnergy'].sort_values(by=['date', 'time'], ascending=True)

    #totalPower = totalPower.drop(columns=['timestamp'])
    print(totalPower)

    #Code conventions:    X (capital X) = input of algorithm   y (small y) = output of algorithm
    X = totalPower.drop(columns=['value'])
    y = totalPower['value']

    model = DecisionTreeClassifier()
    #model.fit(X, y)
    


