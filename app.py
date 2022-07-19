import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #giving name
model_aapl = pickle.load(open('model_aapl.pkl', 'rb'))
model_adp = pickle.load(open('model_adp.pkl', 'rb'))
model_cboe = pickle.load(open('model_cboe.pkl', 'rb'))
model_aapl = pickle.load(open('model_aapl.pkl', 'rb'))
model_csco = pickle.load(open('model_csco.pkl', 'rb'))
model_ebay = pickle.load(open('model_ebay.pkl', 'rb'))
@app.route('/')   # default route
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():


    Stock=request.form['stock']
    steps=int(request.form['No of days to forecast'])
    if Stock=='AAPL':
        prediction = model_aapl.forecast(steps)
    if Stock=='ADP':
        prediction = model_adp.forecast(steps)
    if Stock == 'CBOE':
        prediction = model_cboe.forecast(steps)
    if Stock == 'CSCO':
        prediction = model_csco.forecast(steps)
    if Stock == 'EBAY':
        prediction = model_ebay.forecast(steps)

    #print(len(final_features))

    output = round(prediction, 2)

    return render_template('index.html', prediction_text='       {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)