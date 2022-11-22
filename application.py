import os
import logging

from flask import Flask, request, redirect, url_for
from flask_cors import CORS
from flask_apscheduler import APScheduler

from database.db import initialize_db
from routes.liquor import get_bottles, get_bottle
from routes.store import get_stores, get_store
from routes.filter import filter_results
from scraper.scraper import Scraper
from database.db_converter import update_db
# from credentials import dev_url

class Config:
  SCHEDULER_API_ENABLED = True

application = app = Flask(__name__)

username = os.environ['RDS_USERNAME']
password = os.environ['RDS_PASSWORD']
host = os.environ['RDS_HOSTNAME']
port = os.environ['RDS_PORT']
database = os.environ['RDS_DB_NAME']

url_string = f'postgresql://{username}:{password}@{host}:{port}/{database}'
app.config['SQLALCHEMY_DATABASE_URI'] = url_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config())

initialize_db(app)

CORS(app)

scheduler = APScheduler()
@scheduler.task('cron', id='update_db', hour=3, minute=30, misfire_grace_time=900)
def database_update():
  print('scraping in progress')
  scraper = Scraper()
  scraper.execute()
  print('scraping complete')
  print('db updating in progress')
  update_db()
  print('db updating complete')
scheduler.init_app(app)
scheduler.start()

# routes
@app.route('/')
def redirect_route():
  print('hello welcome to the log')
  return redirect(url_for('liquor_route'))

@app.route('/liquor', methods = ['GET'])
def liquor_route():
  # get all bottles
  if request.method == 'GET':
    return get_bottles()
  
@app.route('/liquor/<id>', methods = ['GET'])
def liquor_id_route(id):
  # get single bottle
  if request.method == 'GET':
    return get_bottle(id)

@app.route('/stores', methods = ['GET'])
def store_route():
  # get all stores
  if request.method == 'GET':
    return get_stores()

@app.route('/stores/<id>', methods = ['GET'])
def store_id_route(id):
  # get a store
  if request.method == 'GET':
    return get_store(id)

@app.route('/filter', methods = ['POST'])
def filter_route():
  # filter results
  if request.method == 'POST':
    data = request.get_json()
    return filter_results(data)

@app.route('/health_check')
def check():
  get_store(1213)
  return 'healthy'

if __name__ == '__main__':
  app.run(debug=False)
else:
  gunicorn_logger = logging.getLogger('gunicorn.error')
  app.logger.handlers = gunicorn_logger.handlers
  app.logger.setLevel(logging.INFO)