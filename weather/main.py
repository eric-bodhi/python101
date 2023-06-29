import requests
from flask import Flask, render_template, request

app = Flask(__name__)
api_key = "72140f5580921669a13d76e148e6bbe7"
city = "Columbia"

@app.route('/', methods=['GET', 'POST'])
def index():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    temperature_celsius = round(temperature - 273.15, 2)
    temperature_fahrenheit = round(temperature_celsius * 9/5 + 32, 2)
    description = data['weather'][0]['description']
    return render_template('result.html', temperature_celsius=temperature_celsius, temperature_fahrenheit=temperature_fahrenheit, city=city, description=description)