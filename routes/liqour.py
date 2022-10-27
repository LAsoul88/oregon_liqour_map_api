# from flask import request

# from database.db import db
from models.liqour import Liqour
from models.store import Store
from models.liqour_store import LiqourStore
from routes.formatting import format_store, format_liqour


# get all bottles
def get_bottles():
  bottles = Liqour.query.order_by(Liqour.id.asc()).all()
  bottle_list = []
  for bottle in bottles:
    bottle_list.append(format_liqour(bottle))
  return bottle_list

# get single bottle
def get_bottle(id):
  bottle = Liqour.query.filter_by(id = id).one()
  liqour_store_table = LiqourStore.query.filter_by(liqour_id = id).order_by(LiqourStore.store_id.asc()).all()
  store_list = []
  for row in liqour_store_table:
    store = Store.query.filter_by(id = row.store_id).one()
    formatted_store = format_store(store)
    formatted_store['quantity'] = row.quantity
    store_list.append(formatted_store)
  return format_liqour(bottle, store_list)

# # create a bottle
# def create_bottle():
#   request_data = request.get_json()
#   bottle = Liqour(request_data)
#   db.session.add(bottle)
#   db.session.commit()
#   return format_liqour(bottle)

# # update a bottle
# def update_bottle(id):
#   bottle = Liqour.query.filter_by(id = id)
#   request_data = request.get_json()
#   bottle.update(request_data)
#   db.session.commit()
#   return { 'liqour': format_liqour(bottle.one()) }

# # delete a bottle
# def delete_bottle(id):
#   bottle = Liqour.query.filter_by(id = id).one()
#   db.session.delete(bottle)
#   db.session.commit()
#   return f'Bottle (id: {id}) deleted!'