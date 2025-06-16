from server.models import Restaurant, db, Pizza, RestaurantPizza
from server.app import create_app
app = create_app()

with app.app_context():
    #clear existing data
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

    #create restaurants
    r1 = Restaurant(name="Mama's Pizza", address="123 Tomato St, Nairobi")
    r2 = Restaurant(name="Pizza Safari", address="456 Cheese Rd, Nakuru")

    #create pizzas
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
    p3 = Pizza(name="BBQ Chicken", ingredients="BBQ Sauce, Chicken, Onion")

    #create restaurant-pizza prices
    rp1 = RestaurantPizza(restaurant=r1, pizza=p1, price=20)
    rp2 = RestaurantPizza(restaurant=r1, pizza=p2, price=27)
    rp3 = RestaurantPizza(restaurant=r2, pizza=p3, price=19)
    rp4 = RestaurantPizza(restaurant=r2, pizza=p1, price=25)

    #add to the session and commit
    db.session.add_all([r1, r2, p1, p2, p3, rp1, rp2, rp3, rp4])
    db.session.commit()

    print("✅ Database seeded!")
