from flask import Flask, request,jsonify, send_from_directory
import os
from dotenv import load_dotenv
from requests import get

load_dotenv()
base_url = os.getenv('BASE_URL')
secret_key = os.getenv('API_KEY')
endpoint = f'api/v7/currencies?apiKey={secret_key}'

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/get-currencies')
def get_currencies():
    data = get(base_url + endpoint).json()
    return data

@app.route('/currencies-convert', methods=["POST"])
def currencies_converter():
    convertFrom = request.json.get('from')
    convertTo = request.json.get('to')
    convertAmount = request.json.get('amount')
    convert_endpoint = f'api/v7/convert?q={convertFrom}_{convertTo}&compact=ultra&apiKey={secret_key}'
    data = get(base_url + convert_endpoint).json()
    value = float(data[f'{convertFrom}_{convertTo}']) * float(convertAmount)
    return jsonify(value)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)
