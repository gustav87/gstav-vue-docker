#!/usr/bin/env python3
from flask import Flask, render_template, send_from_directory, send_file
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import backend.contact, backend.dataBasics, backend.ip, backend.flickr, os

app = Flask(__name__)
cors = CORS(app)

#connect and create db
app.config["MONGO_URI"] = "mongodb://db:27017/gstav"

#initialize the client for mongodb
mongo = PyMongo(app)

@app.route("/")
def home():
  return "hello"

@app.route("/CV.pdf")
def pdf():
  return send_file('CV.pdf')

#
# @app.route('/js/<path:path>')
# def send_js(path):
#   return send_from_directory('js', path)
#
# @app.route('/css/<path:path>')
# def send_css(path):
#   return send_from_directory('css', path)
#
# @app.route('/templates/<path:path>')
# def send_templates(path):
#   return send_from_directory('templates', path)
#
# @app.route('/util/<path:path>')
# def send_util(path):
#   return send_from_directory('util', path)
#
# @app.route('/xhr/<path:path>')
# def send_xhr(path):
#   return send_from_directory('xhr', path)
#
@app.route('/backend/contact')
def contact():
  print("hello")
  backend.contact.sendmail()
  return f'Message sent.'

@app.route('/backend/databasics/insertRow', methods = ['POST'])
def insert_row():
  backend.dataBasics.insertRow(mongo, mongo.db.customers)
  return 'Record inserted into database.'

@app.route('/backend/databasics/getDocuments')
def get_documents():
  return backend.dataBasics.getDocuments(mongo, mongo.db.customers)

@app.route('/backend/flickr/getTaggedImages')
def get_tagged_images():
  return backend.flickr.getTaggedImages()

@app.route('/backend/flickr/getDogs')
def get_dogs():
  return backend.flickr.getDogs()

if __name__ == '__main__':
  debugFlag = True
  if os.getenv('PYTHONUNBUFFERED') == '0':
    debugFlag = False
  app.run(host=backend.ip.get_ip(), debug=debugFlag)
