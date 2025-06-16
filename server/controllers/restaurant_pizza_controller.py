# server/controllers/restaurant_pizza_controller.py

from flask import Blueprint, request, jsonify
from server.app import db
from server.models import RestaurantPizza, Pizza, Restaurant

# Use the correct blueprint name that matches what app.py expects
restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()
        price = data['price']
        pizza_id = data['pizza_id']
        restaurant_id = data['restaurant_id']

        new_rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_rp)
        db.session.commit()

        return jsonify({
            "id": new_rp.id,
            "price": new_rp.price,
            "pizza_id": new_rp.pizza_id,
            "restaurant_id": new_rp.restaurant_id,
            "pizza": {
                "id": new_rp.pizza.id,
                "name": new_rp.pizza.name,
                "ingredients": new_rp.pizza.ingredients
            },
            "restaurant": {
                "id": new_rp.restaurant.id,
                "name": new_rp.restaurant.name,
                "address": new_rp.restaurant.address
            }
        }), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
