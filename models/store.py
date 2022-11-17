from database.db import db


class Store(db.Model):
  __tablename__ = 'stores'
  id = db.Column(db.Integer, primary_key=True)
  address = db.Column(db.String(100))
  phone_number = db.Column(db.String(20))
  lat = db.Column(db.Float)
  lon = db.Column(db.Float)

  def __repr__(self):
    return self.address

  def __init__(self, store_data):
    self.id = store_data['id']
    self.address = (
      f"{store_data['address']} {store_data['city']}, {store_data['state']} {store_data['postal_code']}"
    )
    self.phone_number = store_data['phone_number']
    self.coordinates = [store_data['lat'], store_data['lon']]

  @property
  def serialized(self):
    return {
      'id': self.id,
      'address': self.address,
      'phone_number': self.phone_number,
      'coordinates': self.coordinates,
    }