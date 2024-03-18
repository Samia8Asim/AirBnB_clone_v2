#!/usr/bin/python3
"""Module for DBStorage class"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        db_user = os.getenv('HBNB_MYSQL_USER')
        db_password = os.getenv('HBNB_MYSQL_PWD')
        db_host = os.getenv('HBNB_MYSQL_HOST', default='localhost')
        db_name = os.getenv('HBNB_MYSQL_DB')
        db_env = os.getenv('HBNB_ENV')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(db_user, db_password, db_host, db_name),
            pool_pre_ping=True)

        if db_env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def all(self, cls=None):
        """Query on current database"""
        from models import classes_dict
        objects_dict = {}
        if cls:
            if type(cls) == str:
                cls = classes_dict.get(cls)
            query_result = self.__session.query(cls).all()
        else:
            all_classes = [State, City, User, Place, Amenity, Review]
            query_result = []
            for class_obj in all_classes:
                query_result.extend(self.__session.query(class_obj).all())

        for obj in query_result:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects_dict[key] = obj

        return objects_dict

    def new(self, obj):
        """Add object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit changes of current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and current database session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
