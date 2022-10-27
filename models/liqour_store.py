from database.db import db

class LiqourStore(db.Model):
  __tablename__ = 'liqour_store'
  liqour_id = db.Column(db.String(15), db.ForeignKey('liqour.id'), primary_key=True)
  store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), primary_key=True)
  quantity = db.Column(db.Integer)

  def __init__(self, liqour_store_data):
    self.quantity = liqour_store_data['quantity']
    self.liqour_id = liqour_store_data['liqour_id']
    self.store_id = liqour_store_data['store_id']

# liqour_store_table = db.Table(
#   "liqour_store",
#   db.Column("liqour_id", db.String(15), db.ForeignKey('liqour.id'), primary_key=True),
#   db.Column("store_id", db.Integer, db.ForeignKey('stores.id'), primary_key=True),
#   db.Column("quantity", db.Integer),
# )