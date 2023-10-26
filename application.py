import os
import logging

from flask import Flask, request, redirect, url_for
from flask_cors import CORS

from database.db import initialize_db
from routes.liquor import get_bottles, get_bottle, get_bottle_and_stores
from routes.store import get_stores, get_store
from routes.filter import filter_results


application = app = Flask(__name__)
CORS(app)

prod_url = f"postgresql://{os.environ['RDS_USERNAME']}:{os.environ['RDS_PASSWORD']}@{os.environ['RDS_HOSTNAME']}:{os.environ['RDS_PORT']}/{os.environ['RDS_DB_NAME']}"
# from credentials import dev_url
class Config:
  SQLALCHEMY_DATABASE_URI = prod_url
  SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config.from_object(Config())

initialize_db(app)

# routes
@app.route('/')
def redirect_route():
  print('hello welcome to the log')
  return redirect(url_for('liquor_route'))

@app.route('/liquor', methods = ['GET'])
def liquor_route():
  # get all bottles
  if request.method == 'GET':
    return get_bottles(request)
  
@app.route('/liquor/<id>', methods = ['GET', 'POST'])
def liquor_id_route(id):
  # get single bottle
  if request.method == 'GET':
    return get_bottle(id)
  if request.method == 'POST':
    data = request.get_json()
    return get_bottle_and_stores(data)

@app.route('/stores', methods = ['GET'])
def store_route():
  # get all stores
  if request.method == 'GET':
    return get_stores(request)

@app.route('/stores/<phone_number>', methods = ['GET'])
def store_id_route(phone_number):
  # get a store
  if request.method == 'GET':
    return get_store(phone_number)

@app.route('/filter', methods = ['POST'])
def filter_route():
  # filter results
  if request.method == 'POST':
    data = request.get_json()
    return filter_results(data)

# @app.route('/initial', methods = ['POST'])
# def initial_route():
#   # produce initial payload
#   data = request.get_json()
#   if request.method == 'POST':
#     return initial_results(data)

@app.route('/health_check')
def check():
  get_store("541-256-1200")
  return 'healthy'

if __name__ == '__main__':
  app.run(debug=False)
else:
  gunicorn_logger = logging.getLogger('gunicorn.error')
  app.logger.handlers = gunicorn_logger.handlers
  app.logger.setLevel(logging.INFO)