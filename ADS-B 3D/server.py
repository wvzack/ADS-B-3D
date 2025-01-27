import json
from flask import Flask, render_template, jsonify, send_from_directory
import requests
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

ACCESS_TOKEN = ''
Data_Fetch_Link = 'http://192.168.x.x:8080/data/aircraft.json' #swap this for your ip and port (normally on port 8080)
Port = '5000'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adsb_data', methods=['GET'])
def adsb_data():
    try:
        headers = {
            'Authorization': f'Bearer {ACCESS_TOKEN}'
        }
        response = requests.get(Data_Fetch_Link, headers=headers)
        data = response.json()
        #app.logger.debug(f"ADS-B Data: {data}")
        
        return jsonify(data)
    except requests.RequestException as e:
        app.logger.error(f"Request error: {e}")
        return jsonify({"error": "Failed to fetch ADS-B data"}), 500
    except json.JSONDecodeError as e:
        app.logger.error(f"JSON decode error: {e}")
        return jsonify({"error": "Failed to decode JSON data"}), 500
    except Exception as e:
        app.logger.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route('/models/<path:filename>')
def serve_model(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Port, debug=True)
