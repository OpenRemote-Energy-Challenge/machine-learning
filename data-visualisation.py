#Data visualisation python code
import pandas as pd
import sys
import matplotlib
import matplotlib.pyplot as pyplot

#Check versions of libraries for debugging purposes
print("Python:\t", sys.version.split(' ')[0])
print("Version info:", sys.version_info)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__, "\n")

solar_data = pd.read_csv("./SolarData.csv")

#Get basic information about the solar data
print(solar_data.info(), "\n" ,solar_data.describe(), "\n")

#Get first or last 5 lines from a csv
solar_data.head()
solar_data.tail()

#Get how many field values their are in the csv
for field in solar_data:
    print("******** Field:", field, "********")
    print(solar_data[field].value_counts())
    print()

#Split date & time into seperate fields
solar_data['date'] = [datetime.split(' ')[0][2:].strip() for datetime in solar_data['timestamp']]
solar_data['time'] = [datetime.split(' ')[1].strip() for datetime in solar_data['timestamp']]
print(solar_data)

#Get the data of a single building
humber_building_data = solar_data.loc[solar_data['name'] == 'Humber building'].sort_values(by=['timestamp'])
tamar_bulding_data = solar_data.loc[solar_data['name'] == 'Tamar building'].sort_values(by=['timestamp'])

#Get the total power of a building and sort by attributes
humber_totalPower = humber_building_data.loc[humber_building_data['attribute_name'] == 'totalPower']
tamar_totalPower = tamar_bulding_data.loc[tamar_bulding_data['attribute_name'] == 'totalPower']

humber_totalPower_date = humber_totalPower.loc[humber_totalPower['date'] == '21-02-05'].sort_values(by=['time'])

#Get the total energy of a bulding
humber_totalEnergy = humber_building_data.loc[humber_building_data['attribute_name'] == 'totalEnergy']
tamar_totalEnergy = tamar_bulding_data.loc[tamar_bulding_data['attribute_name'] == 'totalEnergy']

input("Press Enter to continue...")
print("OK")

#Draw a graph from a attribute
tamar_totalPower.plot(x='timestamp', y='value', title='Total power of the tamar building')
print("Showing total power of the tamar building")
pyplot.show()

humber_totalEnergy.plot(x='timestamp', y='value', title='Total energy of the humber building')
print("Showing total energy of the humber building")
pyplot.show()

humber_totalPower_date.plot(x='time', y='value', title='Total power of the humber building on 05/02/21')
print('Showing total power of the humber building on 05/02/21')
pyplot.show()