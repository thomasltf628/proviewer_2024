import pickle
import numpy as np
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Etsy_wbe_scraping import Etsy
from puma_scrape import Puma
from shein_web_scraoing import SHEIN
from flask import Flask, jsonify
from flask import request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return ("Hello")

@app.route("/scrap_etsy", methods=["GET"])
def scrapping_etsy():
    #data = request.json
    result = Etsy()
    return jsonify(result)

@app.route("/scrap_puma", methods=["GET"])
def scrapping_puma():
    #data = request.json
    result = Puma()
    return jsonify(result)

@app.route("/scrap_shein", methods=["GET"])
def scrapping_shein():
    #data = request.json
    result = SHEIN()
    return jsonify(result)



"""if __name__ == "__main__":
    app.run()"""

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)