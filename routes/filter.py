from database.db import db
from models.store import Store
from models.liqour import Liqour
from models.liqour_store import LiqourStore

def filter_results(filter):
  results = []
  search_string = filter.data['search']
  match search_string:
    case 'Browse By Store':
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
# (Browse By Area) - City or Postal Code
# (Browse All Locations) - Description
# (Type) - Category
# (Case Price) - Case Price
# (Bottle Price) - Bottle Price
# (Size) - Size
# (Proof) - Proof
# (Age) - Age
