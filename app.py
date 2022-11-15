from flask import Flask, request, render_template
import requests

API_KEY = '970aea56d9210af92749d16d0544f24f'


app = Flask(__name__)

def getWeatherData(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    data = requests.get(url).json()
    return data

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        data = getWeatherData(city)
        form = True
        return render_template('index.html', data=data, form=form)
    else:
        # data = getWeatherData('manila')
        # data = 'None'
        form = False
        return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080,debug=True)