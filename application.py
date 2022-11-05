import os
from flask import Flask, request, redirect, url_for
from flask_cors import CORS
from flask_apscheduler import APScheduler

from database.db import initialize_db
from routes.liqour import get_bottles, get_bottle
""" , create_bottle, update_bottle, delete_bottle """
from routes.store import get_stores, get_store
""" , create_store, update_store, delete_store """
# from routes.liqour_store import create_table, update_table, delete_table
from scraper.scraper import Scraper
from database.db_converter import update_db

class Config:
  SCHEDULER_API_ENABLED = True

application = Flask(__name__)
username = os.environ['RDS_USERNAME']
password = os.environ['RDS_PASSWORD']
host = os.environ['RDS_HOSTNAME']
url_string = f'postgresql://{username}:{password}@{host}'
application.config['SQLALCHEMY_DATABASE_URI'] = url_string
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config.from_object(Config())

initialize_db(application)

CORS(application)

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
scheduler.init_app(application)
scheduler.start()


@application.route('/')
def hello():
  return redirect(url_for('liqour_route'))

@application.route('/liqour', methods = ['GET'
# , 'POST'
 ])
def liqour_route():
  # get all bottles
  if request.method == 'GET':
    return get_bottles()
  # # create a bottle
  # elif request.method == 'POST':
  #   return create_bottle()
  
@application.route('/liqour/<id>', methods = ['GET'
# , 'PUT', 'DELETE'
])
def liqour_id_route(id):
  # get single bottle
  if request.method == 'GET':
    return get_bottle(id)
  # update a bottle
  # elif request.method == 'PUT':
  #   return update_bottle(id)
  # # delete a bottle
  # elif request.method == 'DELETE':
  #   return delete_bottle(id)

@application.route('/stores', methods = ['GET'
# , 'POST'
])
def store_route():
  # get all stores
  if request.method == 'GET':
    return get_stores()
  # # create a store
  # elif request.method == 'POST':
  #   return create_store()

@application.route('/stores/<id>', methods = ['GET'
# , 'PUT', 'DELETE'
])
def store_id_route(id):
  # get a store
  if request.method == 'GET':
    return get_store(id)
  # # update a store
  # elif request.method == 'PUT':
  #   return update_store(id)
  # # delete a store
  # elif request.method == 'DELETE':
  #   return delete_store(id)

# @app.route('/table', methods = ['POST'])
# def table_route():
#   # create a table
#   if request.method == 'POST':
#     return create_table()

# @app.route('/table/<id>', methods = ['PUT', 'DELETE'])
# def table_id_route(id):
#   # update a table
#   if request.method == 'PUT':
#     return update_table(id)
#   # delete a table
#   elif request.method == 'DELETE':
#     return delete_table(id)

if __name__ == '__main__':
  application.run(debug=False)