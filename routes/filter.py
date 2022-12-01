from models.store import Store
from models.liquor import Liquor

# filter object
# {
#   data: {
#     filters: [
#       {
#         search: <query here>,
#         filter: <filter here>,
#         range: <range here>,
#       },
#     ]
#   }
# }

def filter_results(request):
  results = []
  filter_list = request['data']['filters']

  if filter_list[0]['filter'] == 'Browse By Store':
    search_string = filter_list[0]['search']
    print(search_string)
    stores = Store.query.filter(Store.address.ilike("%{}%".format(search_string))).all()
    for store in stores:
      results.append(store.serialized)
    return results 

  query = Liquor.query
  
  for field in filter_list:
    filter_string = field['filter']
    search_string = field['search']    

    if 'Price' in filter_string:
      range_string = field['range']
      search_price = float(search_string.replace('$', ''))
      price = getattr(Liquor, filter_string.replace(' ', '_').lower())
      if range_string == 'lower':
        query = query.filter(price <= search_price).order_by(price.asc())
      elif range_string == 'higher':
        query = query.filter(price >= search_price).order_by(price.asc())
    
    elif filter_string == 'Proof':
      range_string = field['range']
      proof = float(search_string)
      if range_string == 'lower':
        query = query.filter(Liquor.proof <= proof)
      elif range_string == 'higher':
        query = query.filter(Liquor.proof >= proof)
    
    else: 
      if filter_string == 'Browse All Liquor':
        filter_string = 'description'
      descriptor = getattr(Liquor, filter_string.replace(' ', '_').lower())
      query = query.filter(descriptor.ilike("%{}%".format(search_string)))

  liquor = query.all()
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
