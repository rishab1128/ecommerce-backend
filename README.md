# Ecommerce API

This is an example implementation of an e-commerce API using Python FastAPI and MongoDB as the database.

## Requirements

To run this project, you need to have the following installed:

- Python (version 3.10 or above)
- FastAPI
- pymongo
- uvicorn
- Faker (to generate fake dummy data)
- certifi
- MongoDB

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/ecommerce-backend.git
```

2. Move into the repository using the `cd` command:
```bash
cd ecommerce-backend
```

3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

4. Set up the MongoDB database:

   - Install MongoDB following the official [MongoDB Installation Guide](https://docs.mongodb.com/manual/installation/).
   - Start the MongoDB service.
   - Create a new database named `ecommerce`.
   - Create two collections namely `products` and `orders`.
   - Import `data/products.json` file in the `products` collection and `data/orders.json` file in the `orders` collection

5. Create a .env file:

   - Create a new file named `.env` in the project root directory.
   - Add the following line to the .env file:

     ```
     MONGO_URI=mongodb://localhost:27017/ecommerce
     ```

   - Replace `localhost:27017` with the appropriate MongoDB connection URI if you are using a different host or port.

## Project Structure

```
ecommerce-backend
├── config/
│   ├── db.py #mongo db connection
├── models/
│   ├── ecommerce_model.py #pydantic models
├── routes/
│   └── ecommerce_routes.py #api endpoints 
├── schemas/
│   ├── ecommerce_schema.py #database schema
├── data/
│   ├── generateDummyOrders.py #generates 20 fake dummy orders
|   ├── generateDummyProducts.py #generates 20 fake dummy products
|   ├── orders.json  #json file containing data of 20 fake dummy orders
|   ├── products.json  #json file containing data of 20 fake dummy products
├── .env # contains environment variables (MONGO_URI in this case)
├── .gitignore
├── test.http
├── requirements.txt
└── README.md
```

## Usage

1. Run the FastAPI application:

     ```bash
      uvicorn index:app --reload
     ```

2. Access the API using the provided endpoints. You can use tools like cURL, Postman, or your web browser (`http://127.0.0.1:8000/docs`) to interact with the API.
   
- GET `/products`: Lists all available products in the system.
- PUT `/products/{product_id}`: Updates the available quantity for a product.
- POST `/add_product`: Creates a new product.
- POST `/create_order`: Creates a new order.
- GET `/orders`: Lists all orders from the system with pagination support.
- GET `/orders/{order_id}`: Retrieves a specific order by its ID.

3. You can also test the API by installing the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) extension in VS-Code and then sending the requests through the `test.http` file which is present in the root-directory of this project.

## Project Explanation

The project is implemented using Python FastAPI and MongoDB as the database. It provides various API endpoints to manage products and orders in an ecommerce system.

### Products

- `GET /products`: This endpoint lists all available products in the system. It retrieves the products from the MongoDB `products` collection and returns them as a JSON response.

- `PUT /products/{product_id}`: This endpoint allows updating the available quantity for a specific product. It takes the `product_id` as a path parameter and the new `quantity` as a request parameter. The product is updated in the MongoDB collection, and the updated product is returned in the response.

- `POST /add_product`: This endpoint creates a new product. It expects a JSON payload containing the product details in the request body. The new product is inserted into the MongoDB `products` collection, and the created product is returned in the response.

### Orders

- `POST /create_order`: This endpoint creates a new order. It expects a JSON payload containing the order details in the request body. The order is inserted into the MongoDB `orders` collection, and the created order is returned in the response.

- `GET /orders`: This endpoint lists all orders from the system with pagination support. It accepts optional `limit` and `offset` query parameters to control the number of results returned. The orders are retrieved from the MongoDB `orders` collection, and the paginated orders are returned in the response.

- `GET /orders/{order_id}`: This endpoint retrieves a specific order by its ID. It takes the `order_id` as a path parameter and fetches the order from the MongoDB `orders` collection. The order is returned in the response.

## Further Enhancements

This is a basic implementation of an e-commerce API. Some possible improvements include:

- Implementing authentication and authorization for secure access to the API.
- Adding validation and error handling for the input data.
- Implementing search functionality to filter products or orders based on specific criteria.
- Adding additional endpoints for updating and deleting orders.
- Implementing tests to ensure the correctness and robustness of the API.
