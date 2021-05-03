#Data visualisation python code
import pandas as pd
import matplotlib
import matplotlib.pyplot as pyplot
import datetime as datetime
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier

if __name__ == "__main__":
    """
    pd.set_option('display.max_rows', 10000)
    pd.set_option('display.max_columns', 10000)
    pd.set_option('display.width', 10000)
    """
    solar_data = pd.read_csv("./data/SolarData.csv")
    solar_estimations = pd.read_csv("./data/GetWeatherSiteEstimatedActuals.csv")

    solar_data['date'] = [datetime.split(' ')[0][2:].strip() for datetime in solar_data['timestamp']]
    solar_data['time'] = [datetime.split(' ')[1].strip() for datetime in solar_data['timestamp']]

    totalPower = solar_data.loc[solar_data['attribute_name'] == 'totalPower'].sort_values(by=['timestamp'], ascending=True)

    """
    le = preprocessing.LabelEncoder()
    totalPower_train = totalPower.apply(le.fit_transform)
    """

    #Code conventions:    X (capital X) = input of algorithm   y (small y) = output of algorithm
    """
    X = totalPower_train.drop(columns=['value'])
    y = totalPower_train['value']
    model = DecisionTreeClassifier()
    model.fit(X, y)
    prediction_data = solar_estimations
    """
    print(totalPower)

    """should_predict = [['21-02-05', '01:20:00']].apply(le.fit_transform)
    predictions = model.predict(should_predict)
    print(predictions)"""