import math
from flask import jsonify

from models.store import Store
from models.liquor import Liquor
from models.liquor_store import LiquorStore
from routes.formatting import format_liquor, format_store

# get all stores
def get_stores(request):
  page = request.args.get('page') or 1
  per_page = request.args.get('per_page') or 20
  query = Store.query
  page_count = math.ceil(query.count() / int(per_page))
  stores = query.order_by(Store.id.asc()).paginate(page=int(page), per_page=int(per_page), max_per_page=50)
  store_list = []
  for store in stores:
    store_list.append(format_store(store))
  return jsonify({'stores': store_list, 'page_total': page_count})

# get single store
def get_store(id):
  try:
    store = Store.query.filter_by(id = id).one()
    liquor_store_table = LiquorStore.query.filter_by(store_id = id).order_by(LiquorStore.liquor_id.asc()).all()
    liquor_list = []
    for row in liquor_store_table:
      liquor = Liquor.query.filter_by(id = row.liquor_id).one()
      formatted_liquor = format_liquor(liquor)
      formatted_liquor['quantity'] = row.quantity
      liquor_list.append(formatted_liquor)
    return format_store(store, liquor_list)
  except:
    store = Store.query.filter_by(id = id).scalar()
    liquor_store_table = LiquorStore.query.filter_by(store_id = id).order_by(LiquorStore.liquor_id.asc()).scalar()
    if not store:
      print(f'== did not find store id: {id} ==')
    elif not liquor_store_table:
      print(f'== did not find liquor_store_table associated with store id: {id}')
    else:
      print('== something else went wrong ==')
