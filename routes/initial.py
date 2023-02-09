from flask import jsonify

from models.liquor import Liquor
from models.store import Store
from models.liquor_store import LiquorStore
from routes.formatting import format_initial, format_liquor, format_store

def initial_results(request):
  phone_numbers = request['phone_numbers']
  store_query = Store.query
  stores = []
  # store_list = []
  for phone_number in phone_numbers:
    store = store_query.filter_by(phone_number = phone_number).scalar()
    if not store:
      continue
    else:
      stores.append(store)

  search = request['search']
  liquor_query = Liquor.query
  liquor_query = liquor_query.filter(Liquor.description.ilike("%{}%".format(search))).all()
  for store in stores:
    liquor_store_table = LiquorStore.query.filter_by(store_id = store.id).all()
    print(liquor_store_table)






  
  # for store in stores:
  #   liquor_list = []
  #   liquor_store_table = LiquorStore.query.filter_by(store_id = store.id).order_by(LiquorStore.liquor_id.asc()).all()
    # for row in liquor_store_table:
    #   liquor = Liquor.query.filter_by(id = row.liquor_id).scalar()
    #   formatted_liquor = format_liquor(liquor)
    #   formatted_liquor['quantity'] = row.quantity
    #   liquor_list.append(formatted_liquor)
    # store_list.append(format_initial(store, liquor_list))
  return jsonify({'stores': store_list})