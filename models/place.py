#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Table

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id', onupdate='CASCADE',
                                        ondelete='CASCADE'),
                             primary_key=True,
                             nullable=False)
                      )



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='places')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 viewonly=False, backref='place_amenities')
    
    # amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
        @property
        def reviews(self):
            """Return place reviews"""
            place_reviews = storage.all('Review')
            my_reviews = []
            for review in place_reviews.values():
                if review.place_id == self.id:
                    my_reviews.append(review)
            return my_reviews

        @property
        def amenities(self):
            """Return Place amenities"""
            all_amenities = storage.all('Amenity')
            output = []
            for my_amenity in self.amenity_ids:
                for key, obj in all_amenities.items():
                    if my_amenity in key:                 # key is a string
                        output.append(v)
                        break
            return output

        @amenities.setter
        def amenities (self, obj=None):
            """Append list of amenities"""
            if obj is not None:
                if obj.__class__.__name__ == 'Amenity':
                    self.amenity_ids.append(obj.id)
