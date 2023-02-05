import numpy as np
from sklearn.linear_model import LinearRegression

def predict_sales(dates, sales):
    dates = np.reshape(dates, (len(dates), 1))
    sales = np.reshape(sales, (len(sales), 1))
    reg = LinearRegression().fit(dates, sales)
    return reg.predict(dates)
