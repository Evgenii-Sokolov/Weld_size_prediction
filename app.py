import flask
from flask import render_template
import pickle
import sklearn
from sklearn.ensemble import RandomForestRegressor

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['POST','GET'])

@app.route('/index', methods=['POST','GET'])
def main():
    if flask.request.method == 'GET':
        return render_template('index.html')
    
    if flask.request.method == 'POST':
        with open('rf_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

        input_iw = float(flask.request.form['iw'])
        input_if = float(flask.request.form['if'])
        input_vw = float(flask.request.form['vw'])
        input_fp = float(flask.request.form['fp'])

        input_data = [[input_iw, input_if, input_vw, input_fp]]

        y_pred = loaded_model.predict(input_data)
    value1 = y_pred[0][0]
    value2 = y_pred[0][1]
    value1 = round(value1, 3)
    value2 = round(value2, 3)

    return render_template('index.html', result1=value1, result2=value2)
    
if __name__ == '__main__':
    app.run() 