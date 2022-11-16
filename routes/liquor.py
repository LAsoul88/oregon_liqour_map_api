from models.liquor import Liquor
from models.store import Store
from models.liquor_store import LiquorStore
from routes.formatting import format_store, format_liquor


# get all bottles
def get_bottles():
  bottles = Liquor.query.order_by(Liquor.id.asc()).all()
  bottle_list = []
  for bottle in bottles:
    bottle_list.append(format_liquor(bottle))
  return bottle_list

# get single bottle
def get_bottle(id):
  bottle = Liquor.query.filter_by(id = id).one()
  liqour_store_table = LiquorStore.query.filter_by(liqour_id = id).order_by(LiquorStore.store_id.asc()).all()
  store_list = []
  for row in liqour_store_table:
    store = Store.query.filter_by(id = row.store_id).one()
    formatted_store = format_store(store)
    formatted_store['quantity'] = row.quantity
    store_list.append(formatted_store)
  return format_liquor(bottle, store_list)
