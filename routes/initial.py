from flask import jsonify

from models.liquor import Liquor
from models.store import Store
from models.liquor_store import LiquorStore
from routes.formatting import format_initial, format_liquor

def initial_results():
  query = Store.query
  stores = query.order_by(Store.id.asc()).all()
  store_list = []
  for store in stores:
    liquor_list = []
    liquor_store_table = LiquorStore.query.filter_by(store_id = store.id).order_by(LiquorStore.liquor_id.asc()).all()
    for row in liquor_store_table:
      liquor = Liquor.query.filter_by(id = row.liquor_id).one()
      formatted_liquor = format_liquor(liquor)
      formatted_liquor['quantity'] = row.quantity
      liquor_list.append(formatted_liquor)
    store_list.append(format_initial(store, liquor_list))
  return jsonify({'stores': store_list})