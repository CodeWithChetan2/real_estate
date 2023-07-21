import json
import joblib
import numpy as np
import pickle

__data_columns = None
__Model = None


def Load_artifacts():
    print("Loading saved artifacts.. start")
    global __data_columns
    global __Model

    with open(r'C:\Users\chetr\OneDrive\Desktop\Dragon_real_estate\server\artifacts\columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open(r"C:\Users\chetr\OneDrive\Desktop\Dragon_real_estate\server\artifacts\Dragon1.joblib", "rb") as f:
        __Model = joblib.load(f)
    print("Loading artifacts.. Done")


def predict_price(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT):
    X = np.zeros(len(__data_columns))
    X[0] = CRIM
    X[1] = ZN
    X[2] = INDUS
    X[3] = CHAS
    X[4] = NOX
    X[5] = RM
    X[6] = AGE
    X[7] = DIS
    X[8] = RAD
    X[9] = TAX
    X[10] = PTRATIO
    X[11] = B
    X[12] = LSTAT

    return np.round(__Model.predict([X])[0], 2)


if __name__ == '__main__':
    Load_artifacts()

    print(predict_price(1.9802e-01, 0.0000e+00, 1.0590e+01, 0.0000e+00, 4.8900e-01,
                        6.1820e+00, 4.2400e+01, 3.9454e+00, 4.0000e+00, 2.7700e+02,
                        1.8600e+01, 3.9363e+02, 9.4700e+00))
