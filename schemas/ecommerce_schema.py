def product_serializer(item) -> dict:
    return{
        "id": str(item["_id"]),
        "Name": item["Name"],
        "Price": item["Price"],
        "Qty": item ["Qty"]
    }

def products_serializer(items) -> list:
    return [ product_serializer(item) for item in items]



def order_serializer(order) -> dict:
    return{
        "id": str(order["_id"]),
        "timestamp": order["timestamp"],
        "items": order["items"],
        "total_amount": order["total_amount"],
        "user_address": order["user_address"]
    }

def orders_serializer(orders) -> list:
    return [ order_serializer(order) for order in orders]