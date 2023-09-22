#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


env = os.getenv('HBNB_TYPE_STORAGE')
if env == 'file' or env == 'fs':
    storage = FileStorage()
    storage.reload()
else:
    storage = DBStorage()
    storage.reload()
