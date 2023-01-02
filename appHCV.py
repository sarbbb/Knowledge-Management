from flask import Flask, render_template,request
import pickle
import numpy as np
from pypmml import Model

normalized = Model.fromFile('HCV_normalized.pmml') #正規化
model = Model.fromFile('HCV.pmml') #加載pmml

app = Flask(__name__)

@app.route("/")
def man():
    return render_template('HCV_predict.html')

@app.route("/predict",methods=['POST'])
def home():
    data1 = int(request.form['Age'])
    data2 = float(request.form['ALB'])
    data3 = float(request.form['ALP'])
    data4 = float(request.form['ALT'])
    data5 = float(request.form['AST'])
    data6 = float(request.form['BIL'])
    data7 = float(request.form['CHE'])
    data8 = float(request.form['CHOL'])
    data9 = float(request.form['CREA'])
    data10 = float(request.form['GGT'])
    data11 = float(request.form['PROT'])
    data12 = request.form['PROT']
    if data12=='M':  #因為做Normalizer
        data12_1 =1
        data12_2 =0
    else:
        data12_1 =0
        data12_2 =1

    arr = np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12_1,data12_2]])
    print(arr)
    pred = model.predict(normalized.predict(np.array(arr)))
    print(pred)
    result=pred
    print(type(result[0]))
    return render_template('HCV_predict_result.html',data = result[0])


if __name__ =='__main__':
    app.run(port=3000,debug=True)