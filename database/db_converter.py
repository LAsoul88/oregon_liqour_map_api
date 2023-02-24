import os
import csv
import googlemaps

from database.db import db
from models.liquor import Liquor
from models.store import Store
from models.liquor_store import LiquorStore

from credentials import API_KEY
gmaps = googlemaps.Client(key=API_KEY)
# gmaps = googlemaps.Client(key=os.environ['MAPS_API_KEY'])

def update_db():
  file = open('ols-results-latest.csv')

  oregon_liquor_csv = csv.reader(file)

  header = []
  header = next(oregon_liquor_csv)

  for row in oregon_liquor_csv:
    store = Store.query.filter_by(id = row[0]).scalar()
    liquor = Liquor.query.filter_by(id = row[7]).scalar()
    store_has_liquor = LiquorStore.query.filter_by(liquor_id = row[7]).filter_by(store_id = row[0]).scalar()

    if not store:
      address = f'{row[1]} {row[2]}, {row[3]} {row[4]}'
      coordinates = gmaps.geocode(address)
      store_data = {
        'id': row[0],
        'address': row[1],
        'city': row[2],
        'state': row[3],
        'postal_code': row[4],
        'phone_number': row[5],
        'lat': coordinates[0]['geometry']['location']['lat'],
        'lng': coordinates[0]['geometry']['location']['lng']
      }
      store = Store(store_data)
      db.session.add(store)
      db.session.commit()

    if not liquor:
      liquor_data = {
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
      liquor = Liquor(liquor_data)
      db.session.add(liquor)
      db.session.commit()
    
    if not store_has_liquor:
      liquor_store_data = {
        'quantity': row[15],
        'liquor_id': row[7],
        'store_id': row[0]
      }
      liquor_store = LiquorStore(liquor_store_data)
      db.session.add(liquor_store)
      db.session.commit()

  file.close()