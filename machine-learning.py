#Data visualisation python code
import pandas as pd
import matplotlib
import matplotlib.pyplot as pyplot
from sklearn.tree import DecisionTreeClassifier

pd.set_option('display.max_rows', 10000)
pd.set_option('display.max_columns', 10000)
pd.set_option('display.width', 10000)

solar_data = pd.read_csv("./SolarData.csv")

#print(solar_data)

solar_data['date'] = [datetime.split(' ')[0][2:].strip() for datetime in solar_data['timestamp']]
solar_data['time'] = [datetime.split(' ')[1].strip() for datetime in solar_data['timestamp']]

totalPower = solar_data.loc[solar_data['attribute_name'] == 'totalPower']
totalEnergy = solar_data.loc[solar_data['attribute_name'] == 'totalEnergy']

#print(totalPower)
count = 0

for power in totalEnergy['value']:
    print(count, power)
    if (count == 2939 or count == 5474):
        print(power)
    count = count + 1

#solar_data['totalPower'] = [power for power in totalPower['value']]
#solar_data['totalEnergy'] = [energy for energy in totalEnergy['value']]    Length of values (2939) does not match length of index (5474)


#print(solar_data)

def clean_data(dataset):
    print(dataset)
