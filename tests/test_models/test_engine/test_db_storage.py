#!/usr/bin/python3
import unittest
import models
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.state import State
from models.place import Place
from models.city import City
import os


# skip these test if the storage is not db
class TestDBStorage(unittest.TestCase):
    """DB Storage test"""

    def setUp(self):
        """ Set up test environment """
        self.storage = models.storage

    def tearDown(self):
        """ Remove storage file at end of tests """
        del self.storage
