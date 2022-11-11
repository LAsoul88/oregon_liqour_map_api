from sqlalchemy import func
from flask import request

from database.db import db
from models.store import Store
from models.liqour import Liqour
from models.liqour_store import LiqourStore

# filter object
# {
#   data: {
#     search: <query here>,
#     filter: <filter here>,
#   }
# }

def filter_results(request):
  results = []
  filter_string = request['data']['filter']
  search_string = request['data']['search']
  match filter_string:
    case 'Browse By Store':
      print('we here')
      stores = Store.query.filter(Store.address.ilike("%{}%".format(search_string))).all()
      for store in stores:
        results.append(store.serialized)
      return results
    case 'Browse By Area':
      return results
    case 'Browse All Locations':
      return results
    case 'Type':
      return results
    case 'Case Price':
      return results
    case 'Bottle Price':
      return results
    case 'size': 
      return results
    case 'proof':
      return results
    case 'age':
      return results
# (Browse By Store) - Address
# (Browse By City) - City 
# (Browse By Postal Code) - Postal Code
# (Browse All Locations) - Description
# (Type) - Category
# (Case Price) - Case Price
# (Bottle Price) - Bottle Price
# (Size) - Size
# (Proof) - Proof
# (Age) - Age
