from flask import request

from database.db import db

from models.liquor import Liquor
from models.store import Store
from models.liquor_store import LiquorStore

def format_table(table):
  return {
    "liquor_id": table.liqour_id,
    "store_id": table.store_id,
    "quantity": table.quantity
  }

def create_table():
  request_data = request.get_json()
  table = LiquorStore(request_data)
  db.session.add(table)
  db.session.commit()
  return format_table(table)

# use liquor_id for updating/deleting

def update_table(id):
  table = LiquorStore.query.filter_by(liquor_id = id)
  request_data = request.get_json()
  table.update(request_data)
  db.session.commit()
  return format_table(table.one())

def delete_table(id):
  table = LiquorStore.query.filter_by(liquor_id = id).one()
  db.session.delete(table)
  db.session.commit()
  return f'Table (id: {id}) deleted!'