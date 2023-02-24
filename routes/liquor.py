import math
from flask import jsonify

from models.liquor import Liquor
from models.store import Store
from models.liquor_store import LiquorStore
from routes.formatting import format_store, format_liquor, find_closest_stores


# get all bottles
def get_bottles(request):
  page = request.args.get('page') or 1
  per_page = request.args.get('per_page') or 20
  query = Liquor.query
  result_count = query.count()
  page_count = math.ceil(result_count / int(per_page))
  bottles = query.order_by(Liquor.id.asc()).paginate(page=int(page), per_page=int(per_page), max_per_page=50)
  bottle_list = []
  for bottle in bottles:
    bottle_list.append(format_liquor(bottle))
  return jsonify({'liquor': bottle_list, 'page_total': page_count, 'results_total': result_count})

# get single bottle
def get_bottle(id):
  try:
    bottle = Liquor.query.filter_by(id = id).scalar()
    liquor_store_table = LiquorStore.query.filter_by(liquor_id = id).order_by(LiquorStore.store_id.asc()).all()
    store_list = []
    for row in liquor_store_table:
      store = Store.query.filter_by(id = row.store_id).scalar()
      formatted_store = format_store(store)
      formatted_store['quantity'] = row.quantity
      store_list.append(formatted_store)
    return jsonify({'liquor': format_liquor(bottle, store_list)})
  except:
    bottle = Liquor.query.filter_by(id = id).scalar()
    liquor_store_table = LiquorStore.query.filter_by(liquor_id = id).order_by(LiquorStore.store_id.asc()).scalar()
    if not bottle:
      print(f'== did not find liquor id: {id} ==')
    elif not liquor_store_table:
      print(f'== did not find liquor_store_table associated with liquor id: {id}')
    else:
      print('== something else went wrong ==')

def get_bottle_and_stores(request):
  id = request['data']['id']
  coordinates = request['data']['coordinates']
  try:
    bottle = Liquor.query.filter_by(id = id).scalar()
    liquor_store_table = LiquorStore.query.filter_by(liquor_id = id).order_by(LiquorStore.store_id.asc()).all()
    store_list = []
    for row in liquor_store_table:
      store = Store.query.filter_by(id = row.store_id).scalar()
      formatted_store = format_store(store)
      formatted_store['quantity'] = row.quantity
      store_list.append(formatted_store)
    if len(store_list) > 20:
      store_list = find_closest_stores(store_list, coordinates)
    return jsonify({'liquor': format_liquor(bottle, store_list)})
  except:
    bottle = Liquor.query.filter_by(id = id).scalar()
    liquor_store_table = LiquorStore.query.filter_by(liquor_id = id).order_by(LiquorStore.store_id.asc()).scalar()
    if not bottle:
      print(f'== did not find liquor id: {id} ==')
    elif not liquor_store_table:
      print(f'== did not find liquor_store_table associated with liquor id: {id}')
    else:
      print('== something else went wrong ==')  
