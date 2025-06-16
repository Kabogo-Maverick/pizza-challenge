from app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False) 

    #here we establish a one-to-many relationship with RestaurantPizza
    restaurant_pizzas = relationship(
        'RestaurantPizza',
        back_populates='restaurant',
        cascade='all, delete'
    )

    def __repr__(self):
        return f"<Restaurant {self.name}>"
