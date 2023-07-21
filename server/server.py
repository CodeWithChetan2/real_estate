from flask import Flask,request,jsonify
from flask_cors import CORS
import util

app=Flask(__name__)
CORS(app)
# "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
@app.route('/price_predictions',methods=['GET',"POST"])
def price_prediction():
    CRIM=float(request.form['CRIM'])
    ZN=float(request.form['ZN'])
    INDUS=float(request.form['INDUS'])
    CHAS=float(request.form['CHAS'])
    NOX=float(request.form['NOX'])
    RM=float(request.form['RM'])
    AGE=float(request.form['AGE'])
    DIS=float(request.form['DIS'])
    RAD=float(request.form['RAD'])
    TAX=float(request.form['TAX'])
    PTRATIO=float(request.form['PTRATIO'])
    B=float(request.form['B'])
    LSTAT=float(request.form['LSTAT'])
    response=jsonify({
        "Predicted_price":util.predict_price(CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT)
    })
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__=='__main__':
 print("Creating a flask server for Price Predictions")
 util.Load_artifacts()
 app.run()
