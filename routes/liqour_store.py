from flask import request

from database.db import db

from models.liqour import Liqour
from models.store import Store
from models.liqour_store import LiqourStore

def format_table(table):
  return {
    "liqour_id": table.liqour_id,
    "store_id": table.store_id,
    "quantity": table.quantity
  }

def create_table():
  request_data = request.get_json()
  table = LiqourStore(request_data)
  db.session.add(table)
  db.session.commit()
  return format_table(table)

# use liqour_id for updating/deleting

def update_table(id):
  table = LiqourStore.query.filter_by(liqour_id = id)
  request_data = request.get_json()
  table.update(request_data)
  db.session.commit()
  return format_table(table.one())

def delete_table(id):
  table = LiqourStore.query.filter_by(liqour_id = id).one()
  db.session.delete(table)
  db.session.commit()
  return f'Table (id: {id}) deleted!'