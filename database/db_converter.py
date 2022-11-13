import csv
from database.db import db
from models.liqour import Liqour
from models.store import Store
from models.liqour_store import LiqourStore

def update_db():
  file = open('ols-results-latest.csv')

  oregon_liqour_csv = csv.reader(file)

  header = []
  header = next(oregon_liqour_csv)

  for row in oregon_liqour_csv:

    store_data = {
      'id': row[0],
      'address': row[1],
      'city': row[2],
      'state': row[3],
      'postal_code': row[4],
      'phone_number': row[5]
    }

    liqour_data = {
      'type': row[6],
      'id': row[7],
      'item_code': row[8],
      'description': row[9],
      'size': row[10],
      'proof': row[11],
      'age': row[12],
      'case_price': float(row[13].replace('$', '')),
      'bottle_price': float(row[14].replace('$', '')),
    }

    liqour_store_data = {
      'quantity': row[15],
      'liqour_id': row[7],
      'store_id': row[0]
    }

    store = Store.query.filter_by(id = store_data['id']).scalar()
    liqour = Liqour.query.filter_by(id = liqour_data['id']).scalar()
    store_has_liqour = LiqourStore.query.filter_by(liqour_id = liqour_data['id']).filter_by(store_id = store_data['id']).scalar()

    if not store:
      store = Store(store_data)
      db.session.add(store)
      db.session.commit()

    if not liqour:
      liqour = Liqour(liqour_data)
      db.session.add(liqour)
      db.session.commit()
    
    if not store_has_liqour:
      liqour_store = LiqourStore(liqour_store_data)
      db.session.add(liqour_store)
      db.session.commit()

  file.close()