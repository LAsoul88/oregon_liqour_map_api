from database.db import db

class Liqour(db.Model):
  __tablename__ = 'liqour'
  id = db.Column(db.String(15), primary_key=True)
  item_code = db.Column(db.String(10))
  description = db.Column(db.String(100))
  size = db.Column(db.String(10))
  proof = db.Column(db.Float)
  age = db.Column(db.String(10))
  case_price = db.Column(db.Float)
  bottle_price = db.Column(db.Float)
  type = db.Column(db.String(15))

  def __repr__(self):
    return self.id

  def __init__(self, liqour_data):
    self.id = liqour_data['id']
    self.item_code = liqour_data['item_code']
    self.description = liqour_data['description']
    self.size = liqour_data['size']
    self.proof = liqour_data['proof']
    self.age = liqour_data['age']
    self.case_price = '{:2f}'.format(liqour_data['case_price'])
    self.bottle_price = '{:2f}'.format(liqour_data['bottle_price'])
    self.type = liqour_data['type']

  @property
  def serialized(self):
    return {
      'id': self.id,
      'item_code': self.item_code,
      'description': self.description,
      'size': self.size,
      'proof': self.proof,
      'age': self.age,
      'case_price': '$' + str('{:.2f}'.format(self.case_price)),
      'bottle_price': '$' + str('{:.2f}'.format(self.bottle_price)),
      'type': self.type,
    }