# from flask import request

# from database.db import db
from models.store import Store
from models.liqour import Liqour
from models.liqour_store import LiqourStore
from routes.formatting import format_liqour, format_store

# get all stores
def get_stores():
  stores = Store.query.order_by(Store.id.asc()).all()
  store_list = []
  for store in stores:
    store_list.append(format_store(store))
  return store_list

# get single store
def get_store(id):
  store = Store.query.filter_by(id = id).one()
  if not store:
    return f'No Store at {id}'
  elif store:
    return f'Store: {store} - id: {id}'
  liqour_store_table = LiqourStore.query.filter_by(store_id = id).order_by(LiqourStore.liqour_id.asc()).all()
  liqour_list = []
  for row in liqour_store_table:
    liqour = Liqour.query.filter_by(id = row.liqour_id).one()
    formatted_liqour = format_liqour(liqour)
    formatted_liqour['quantity'] = row.quantity
    liqour_list.append(formatted_liqour)
  return format_store(store, liqour_list)

# # create a store
# def create_store():
#   request_data = request.get_json()
#   store = Store(request_data)
#   db.session.add(store)
#   db.session.commit()
#   return format_store(store)

# # update a store
# def update_store(id):
#   store = Store.query.filter_by(id = id)
#   request_data = request.get_json()
#   store.update(request_data)
#   db.session.commit()
#   return { 'store': format_store(store.one()) }

# # delete a store
# def delete_store(id):
#   store = Store.query.filter_by(id = id).one()
#   db.session.delete(store)
#   db.session.commit()
#   return f'Store (id: {id}) deleted!'