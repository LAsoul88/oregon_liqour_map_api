def format_store(store, liqour_list = None):
  if liqour_list:
    return { 
      "id": store.id,
      "address": store.address,
      "phone_number": store.phone_number,
      "liqour": liqour_list,
    }
  else:
    return {
      "id": store.id,
      "address": store.address,
      "phone_number": store.phone_number,
    }

def format_liqour(liqour, store_list = None):
  if store_list:
    return {
      "id": liqour.id,
      "item_code": liqour.item_code,
      "description": liqour.description,
      "size": liqour.size,
      "proof": liqour.proof,
      "age": liqour.age,
      "case_price": liqour.case_price,
      "bottle_price": liqour.bottle_price,
      "stores": store_list
    }
  else:
    return {
      "id": liqour.id,
      "item_code": liqour.item_code,
      "description": liqour.description,
      "size": liqour.size,
      "proof": liqour.proof,
      "age": liqour.age,
      "case_price": liqour.case_price,
      "bottle_price": liqour.bottle_price,
      }