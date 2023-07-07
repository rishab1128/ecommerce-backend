from fastapi import APIRouter
from pymongo import ReturnDocument
from models.ecommerce_model import Product,Order
from config.db import connection
from schemas.ecommerce_schema import product_serializer, products_serializer, order_serializer, orders_serializer
from bson import ObjectId,SON

route = APIRouter()
products_collection = connection.ecommerce.products
orders_collection = connection.ecommerce.orders



@route.get("/")
def read_root():
    return {"Hello": "World"}


#PRODUCT ENDPOINTS

@route.get("/products")
def list_products():
    products = products_collection.find({})
    productList = products_serializer(products)
    print("Get All Products Testing")
    return {"productList": productList}


@route.put("/products/{product_id}")
def update_product(product_id: str, quantity: int):
    products_collection.find_one_and_update({"_id": ObjectId(product_id)}, {"$set": {"Qty": quantity}})
    updated_product = products_serializer(products_collection.find({"_id":ObjectId(product_id)}))
    print("Update Product-Testing")
    return {"status": "ok", "upadted_product": updated_product}


@route.post("/")
def add_product(product: Product):
    _id = products_collection.insert_one(dict(product))
    product = products_serializer(products_collection.find({"_id":_id.inserted_id}))
    print("Post product testing")
    return {"status":"ok", "product": product}

###########################################################################################################


#ORDER ENDPOINTS

@route.post("/create_order")
def create_order(order: Order):
    for i in range(len(order.items)):
        order.items[i] = dict(order.items[i])
    order.user_address = dict(order.user_address)
    print(order)
    _id = orders_collection.insert_one(dict(order))
    order = orders_serializer(orders_collection.find({"_id":ObjectId(_id.inserted_id)}))
    print("Post order testing")
    return {"status":"ok", "order": order}


@route.get("/orders")
def list_orders(limit: int = 3, offset: int = 0):
    all_orders = orders_collection.find({})
    total_num_orders = orders_collection.count_documents({})

    if limit+offset > total_num_orders:
        return {"status": "error" , "message": "Sum of Offset and Limit value exceeds the total number of orders"}

    orders = orders_collection.find().skip(offset).limit(limit)
    orderList = orders_serializer(orders)
    print(orderList)
    print("Get All Orders Testing")
    return {"orderList": orderList}


@route.get("/orders/{order_id}")
def get_specific_order(order_id:str):
    order = orders_serializer(orders_collection.find({"_id":ObjectId(order_id)}))
    print("Get specific order testing" , order)
    return {"status":"ok" , "order": order}




