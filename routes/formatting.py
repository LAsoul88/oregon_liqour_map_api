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