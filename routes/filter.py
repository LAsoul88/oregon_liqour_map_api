from models.store import Store
from models.liquor import Liquor

# filter object
# {
#   data: {
#     search: <query here>,
#     filter: <filter here>,
#     range: <range here>,
#   }
# }

def filter_results(request):
  results = []
  filter_string = request['data']['filter']
  search_string = request['data']['search']

  if filter_string == 'Browse By Store':
    stores = Store.query.filter(Store.address.ilike("%{}%".format(search_string))).all()
    for store in stores:
      results.append(store.serialized)
    return results

  elif 'Price' in filter_string:
    range_string = request['data']['range']
    search_price = float(search_string.replace('$', ''))
    price = getattr(Liquor, filter_string.replace(' ', '_').lower())
    liquor = []
    if range_string == 'lower':
      liquor = Liquor.query.filter(price <= search_price).order_by(price.asc()).all()
    elif range_string == 'higher':
      liquor = Liquor.query.filter(price >= search_price).order_by(price.asc()).all()
    for bottle in liquor:
      results.append(bottle.serialized)
    return results
    
  elif filter_string == 'Proof':
    range_string = request['data']['range']
    proof = float(search_string)
    liquor = []
    if range_string == 'lower':
      liquor = liquor.query.filter(Liquor.proof <= proof).order_by(Liquor.proof.asc()).all()
    elif range_string == 'higher':
      liquor = Liquor.query.filter(Liquor.proof >= proof).order_by(Liquor.proof.asc()).all()
    for bottle in liquor:
      results.append(bottle.serialized)
    return results

  else: 
    if filter_string == 'Browse All Liquor':
      filter_string = 'description'
    descriptor = getattr(Liquor, filter_string.replace(' ', '_').lower())
    print('=== search_string ===', search_string)
    liquor = Liquor.query.filter(descriptor.ilike("%{}%".format(search_string))).all()
    for bottle in liquor:
      results.append(bottle.serialized)
    return results

# (Browse By Store) - Address
# (Browse All Liquor) - Description
# (Type) - Category
# (Case Price) - Case Price
# (Bottle Price) - Bottle Price
# (Size) - Size
# (Proof) - Proof
# (Age) - Age
