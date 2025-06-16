from server.extensions import db
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    ingredients = Column(String, nullable=False)

    # One-to-many relationship with RestaurantPizza
    restaurant_pizzas = relationship('RestaurantPizza', back_populates='pizza')

    def __repr__(self):
        return f'<Pizza {self.name}>'
