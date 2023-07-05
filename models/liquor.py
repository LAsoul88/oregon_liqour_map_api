from database.db import db

class Liquor(db.Model):
  __tablename__ = 'liquor'
  id = db.Column(db.String(15), primary_key=True)
  item_code = db.Column(db.String(10))
  description = db.Column(db.String(100))
  size = db.Column(db.String(10))
  proof = db.Column(db.Float)
  age = db.Column(db.String(10))
  case_price = db.Column(db.Float)
  bottle_price = db.Column(db.Float)
  type = db.Column(db.String(30))
  img = db.Column(db.String())

  def __repr__(self):
    return self.id

  def __init__(self, liquor_data):
    self.id = liquor_data['id']
    self.item_code = liquor_data['item_code']
    self.description = liquor_data['description']
    self.size = liquor_data['size']
    self.proof = liquor_data['proof']
    self.age = liquor_data['age']
    self.case_price = '{:2f}'.format(liquor_data['case_price'])
    self.bottle_price = '{:2f}'.format(liquor_data['bottle_price'])
    self.type = liquor_data['type']
    self.img = liquor_data['img']

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
      'img': self.img,
    }