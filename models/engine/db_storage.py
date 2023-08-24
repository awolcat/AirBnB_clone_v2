#!/usr/bin/python3
"""This module defines one class - The Database storage engine"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


User = os.getenv('HBNB_MYSQL_USER')
Pass = os.getenv('HBNB_MYSQL_PWD')
Host = os.getenv('HBNB_MYSQL_HOST')
DBname = os.getenv('HBNB_MYSQL_DB')
URL = f'mysql+mysqldb://{User}:{Pass}@{Host}/{DBname}'


class DBStorage():
    """ This class defines the database storage engine
        using SQLAlchemy
    """

    __engine = None
    __session = None


    def __init__(self):
        """ This method initializes the ORM engine """
        self.__engine = create_engine(URL, pool_pre_ping=True)
        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ This method will query the current database session
            and retrieve objects depending on the class name arg
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State
        # approved = [User, State, City, Amenity, Place, Review]
        result = []
        objects = {}
        if cls:
            result.append(self.__session.query(cls).all())
        else:
            for cls in [State, City, User, Place, Review]:
                result.extend(self.__session.query(cls).all())

        for obj in result:
            k = f'{obj.__class__.__name__}.{obj.id}'
            objects[k] = obj

        return objects

    def new(self, obj):
        """ Add the obj passed to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit / Flush all changes in the current session to the DB """
        self.__session.commit()
        # self.__session.close()

    def delete(self, obj=None):
        """ Delete an existing object from the database """
        if obj:
            self.__session.delete(obj)
            # self.__session.commit()

    def reload(self):
        """ Create all tables in the metadata
            and create the current database session
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State


        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
