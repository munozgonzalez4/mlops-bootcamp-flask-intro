"""
This is the main module for the PUT and DELETE operations in our API. It defines the endpoints for updating and deleting resources.
PUT and DELETE are HTTP methods used to update and delete resources on the server, respectively.
- PUT: This method is used to update an existing resource or create a new resource if it does not exist. 
- DELETE: This method is used to delete an existing resource from the server.
"""

# jsonify is a function that converts a Python dictionary into a JSON response. It is used to create API responses in a format that can be easily consumed by clients.
from flask import Flask, jsonify, request


app = Flask(__name__)


items = [
    {"id": 1, "name": "Item 1", "price": 10.0},
    {"id": 2, "name": "Item 2", "price": 20.0},
    {"id": 3, "name": "Item 3", "price": 30.0}
]


@app.route("/")
def home():
    return "Welcome to the PUT and DELETE API!"


# GET: retrieve items
@app.route("/items", methods = ["GET"])
def get_items():
    return jsonify(items)


# GET based on id
@app.route("/items/<int:item_id>", methods = ["GET"])
def get_item(item_id):
    # Next function is used to find the first item in the list that matches the condition (item["id"] == item_id). If no such item is found, it returns None.
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"})


# POST to create a new item
# NOTE: to test this, we can use Postman to send a POST request with a JSON body containing the name and price of the new item.
@app.route("/items", methods = ["POST"])
def create_item():
    if not request.is_json or not "name" in request.get_json() or not "price" in request.get_json():
        return jsonify({"message": "Item not found"})
    else:
        new_item = {
            "id": items[-1]["id"] + 1 if items else 1,
            "name": request.get_json()["name"],
            "price": request.get_json()["price"]
        }
        items.append(new_item)
        return jsonify(new_item)


# PUT to update an existing item
# NOTE: to test this, we can use Postman to send a PUT request with a JSON body containing the updated name and price of the item. The URL should include the id of the item we want to update (e.g., /items/1).
@app.route("/items/<int:item_id>", methods = ["PUT"])
def update_item(item_id):
    # Find the item_id
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"})
    # Update the item with the new data from the request
    item["name"] = request.get_json().get("name", item["name"])
    item["price"] = request.get_json().get("price", item["price"])
    return jsonify(item)


# DELETE to remove an item
# NOTE: to test this, we can use Postman to send a DELETE request to the URL of the item we want to delete (e.g., /items/1).
@app.route("/items/<int:item_id>", methods = ["DELETE"])
def delete_item(item_id):
    # global keyword is used to indicate that we are referring to the global variable items, allowing us to modify it within the function.
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"message": f"Item {item_id} deleted"})


if __name__ == "__main__":
    app.run(debug = True)