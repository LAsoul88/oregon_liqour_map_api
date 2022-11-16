from database.db import db

class LiquorStore(db.Model):
  __tablename__ = 'liqour_store'
  liquor_id = db.Column(db.String(15), db.ForeignKey('liqour.id'), primary_key=True)
  store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), primary_key=True)
  quantity = db.Column(db.Integer)

  def __init__(self, liquor_store_data):
    self.quantity = liquor_store_data['quantity']
    self.liqour_id = liquor_store_data['liqour_id']
    self.store_id = liquor_store_data['store_id']

  @property
  def serialized(self):
    return {
      'quantity': self.quantity,
      'liqour_id': self.liquor_id,
      'store_id': self.store_id
    }

