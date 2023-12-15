import math

def format_store(store, liquor_list = None):
  if liquor_list:
    return { 
      "id": store.id,
      "address": store.address,
      "phone_number": store.phone_number,
      "coordinates": store.coordinates,
      "liquor": liquor_list,
    }
  else:
    return {
      "id": store.id,
      "address": store.address,
      "phone_number": store.phone_number,
      "coordinates": store.coordinates
    }

def format_liquor(liquor, store_list = None):
  if store_list:
    return {
      "id": liquor.id,
      "item_code": liquor.item_code,
      "description": liquor.description,
      "size": liquor.size,
      "proof": liquor.proof,
      "age": liquor.age,
      "case_price": liquor.case_price,
      "bottle_price": liquor.bottle_price,
      "type": liquor.type,
      "img": liquor.img,
      "stores": store_list
    }
  else:
    return {
      "id": liquor.id,
      "item_code": liquor.item_code,
      "description": liquor.description,
      "size": liquor.size,
      "proof": liquor.proof,
      "age": liquor.age,
      "case_price": liquor.case_price,
      "bottle_price": liquor.bottle_price,
      "type": liquor.type,
      "img": liquor.img
    }

def format_initial(store, liquor_list):
  return {
    "address": store.address,
    "phone_number": store.phone_number,
    "liquor": liquor_list
  }

def find_closest_stores(store_list, coordinates):
  distance_list = []
  for store in store_list:
    distance = math.sqrt((float(store['coordinates'][0]) - float(coordinates[0]))**2 + (float(store['coordinates'][1]) - float(coordinates[1]))**2)
    store['distance'] = distance
    distance_list.append(store)
  sorted_list = sorted(distance_list, key=lambda x: x['distance'])
  return sorted_list[0:20]