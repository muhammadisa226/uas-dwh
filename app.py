from flask import  Flask, request, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        return render_template('index.html')


@app.route('/prediksi', methods=['POST'])
def predict():
    if (request.method == 'POST'):
        return getPredictSalesInYear()



def getPredictSalesInYear():

    tahun = request.form['tahun']
    print(tahun)
    data = pd.read_csv(
        'prediksi_penjualan.csv')

    X = data.iloc[:, 0]  # mengambil data tahun
    Y = data.iloc[:, 1]  # mengambil data amount
    data = data.drop(labels=2, axis=0)

    # Building the model
    X_mean = np.mean(X)
    Y_mean = np.mean(Y)

    num = 0
    den = 0

    # perulangan perhitungan XY dan X^2
    for i in range(len(X)):
        num += (X[i] - X_mean)*(Y[i] - Y_mean)
        den += (X[i] - X_mean)**2

    # perhitungan a dan b
    m = num / den
    c = Y_mean - m*X_mean
    tahun = int(tahun)

    Y_pred =1*(m*tahun + c)
    print(round(Y_pred))
    return render_template('index.html', prediction_text='hasil Prediksi pada tahun {} adalah :  {}'.format(tahun, round(Y_pred)))

if __name__ == '__main__':
    app.run(debug=True)
