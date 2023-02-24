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
      "type": liquor.type
    }

def format_initial(store, liquor_list):
  return {
    "address": store.address,
    "phone_number": store.phone_number,
    "liquor": liquor_list
  }

def partition(list, size):
  for i in range(0, len(list), size):
    yield list[i : i + size]

def find_closest_stores(store_list, coordinates):
  # partitioned_stores = list(partition(store_list, 25))
  # distance_map = {}
  # for group in partitioned_stores:
  #   for store in group:
  #     distance = gmaps.distance_matrix(address, store['address'], mode='driving')
  #     distance_map[distance['rows'][0]['elements'][0]['distance']['value']] = store
  # print(distance_map)
  distance_list = []
  for store in store_list:
    distance = math.sqrt((float(store['coordinates'][0]) - float(coordinates[0]))**2 + (float(store['coordinates'][1]) - float(coordinates[1]))**2)
    distance_list.append({'store': store, 'distance': distance})
  
  sorted_list = sorted(distance_list, key=lambda x: x['distance'])
  short_list = sorted_list[0:20]
  print(len(short_list))