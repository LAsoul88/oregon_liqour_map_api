from database.db import db
from models.store import Store
from models.liqour import Liqour
from models.liqour_store import LiqourStore

def search_results(search):
  results = []
  search_string = search.data['search']

  if search_string:
    if search.data['select'] == 'Browse By Store':
      query = db.session.query(Store, Liqour)
  return []