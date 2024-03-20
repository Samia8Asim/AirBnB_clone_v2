#!/usr/bin/python3
"""state class definition"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage


class State(BaseModel, Base):
    """State class representing states"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    # For DBStorage
    if storage_type == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    # For FileStorage
    else:
        @property
        def cities(self):
            """Getter attribute to retrieve cities related to the state"""
            cities_list = []
            all_cities = storage.all('City')
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
