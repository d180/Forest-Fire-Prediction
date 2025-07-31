from flask import Flask, render_template, request
import pickle
import requests
model = pickle.load(open('model.pkl','rb'))


def weatherDetails(lat,lon):
    api_key="e0abe9e525cc6d6e83a49c10d9cb7a76"
    url = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric'.format(lat,lon,api_key)
    res = requests.get(url)
    data = res.json()
    temp1 = data['main']['temp']-273.15
    temp1 = round(temp1,2)
    hum1 = data['main']['humidity']

    return temp1,hum1



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

    



@app.route('/predict',methods=['POST','GET'])
def predict():
    lat=request.form['latitude']
    lon=request.form['longitude']
    temp,hum=weatherDetails(lat,lon)
    prediction = model.predict([[temp,hum]])
    print(prediction)
    if(prediction==0):
        return render_template('index.html',pred='Your Forest is SAFE.')
    else:
        return render_template('index.html',pred='Your Forest is in DANGER.')




@app.route("/contact")
def contact():
    return "contact"

@app.route("/about_us")
def about():
    return "about us"


if __name__ == "__main__":
    app.run(debug=True, port=9091)