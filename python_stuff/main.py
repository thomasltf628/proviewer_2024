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
from adidas_scraping import Adidas
from roots_scraping import Roots
from sport_chek_scraping import Sportchek

from flask import Flask, jsonify
from flask import request, render_template
from flask_cors import CORS, cross_origin
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch.nn.functional as F
from genuinity_model import getting_label
from sentiment_model import getting_label_sentiment
from waitress import serve
import logging

logging.getLogger('flask_cors').level = logging.DEBUG

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def index():
    print('hi')
    return ("Hello")

@app.route("/scrap_etsy", methods=["POST"])
def scrapping_etsy():
    data = request.json
    link = data.get('inputs')
    result = Etsy(link)
    return jsonify(result)

@app.route("/scrap_puma", methods=["POST"])
def scrapping_puma():
    data = request.json
    link = data.get('inputs')
    result = Puma(link)
    return jsonify(result)

@app.route("/scrap_shein", methods=["POST"])
def scrapping_shein():
    data = request.json
    link = data.get('inputs')
    result = SHEIN(link)
    return jsonify(result)

@app.route("/scrap_adidas", methods=["POST"])
def scrapping_adidas():
    data = request.json
    link = data.get('inputs')
    result = Adidas(link)
    return jsonify(result)

@app.route("/scrap_roots", methods=["POST"])
@cross_origin()
def scrapping_roots():
    data = request.json
    link = data.get('inputs')
    result = Roots(link)
    return jsonify(result)


@app.route("/scrap_sportchek", methods=["POST"])
def scrapping_sportchek():
    data = request.json
    link = data.get('inputs')
    result = Sportchek(link)
    return jsonify(result)



@app.route("/call_genuinity", methods=["POST"])
def calling_genuinity_model():
    data = request.json
    sentence = data.get('text')
    result  = getting_label(sentence)
    return jsonify(result)

@app.route("/call_sentiment", methods=["POST"])
def calling_sentiment_model():
    data = request.json
    sentence = data.get('text')
    result  = getting_label_sentiment(sentence)
    return jsonify(result)




"""if __name__ == "__main__":
    app.run()"""

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)