import math
from flask import jsonify

from models.store import Store
from models.liquor import Liquor

# filter object
# {
#   data: {
#     pagination: {
#       page: <page number>,
#       per_page: <results per page>,
#     },
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
    search_string = str(field['search'])

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

  page = request['data']['pagination']['page'] or 1
  if request['data']['pagination']['per_page'] == 0:
    liquor = query.all()
    for bottle in liquor:
      results.append(bottle.serialized)
    return jsonify({'liquor': results})
  per_page = request['data']['pagination']['per_page'] or 20
  liquor = query.paginate(page=int(page), per_page=int(per_page), max_per_page=50)
  result_count = query.count()
  page_count = math.ceil(result_count / int(per_page))
  for bottle in liquor:
    results.append(bottle.serialized)
  return jsonify({'liquor': results, 'page_total': page_count, 'results_total': result_count})

# (Browse By Store) - Address
# (Browse All Liquor) - Description
# (Type) - Category
# (Case Price) - Case Price
# (Bottle Price) - Bottle Price
# (Size) - Size
# (Proof) - Proof
# (Age) - Age
