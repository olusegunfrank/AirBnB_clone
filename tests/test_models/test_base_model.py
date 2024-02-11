#!/usr/bin/python3
"""
<<<<<<< HEAD
Test suits for the base model
"""

import os
import re
import json
import uuid
import unittest
from time import sleep
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests attributes of the base model
    """

    def setUp(self):
        """
        Classes needed for testing
        """
        pass

    def test_basic(self):
        """
        Tests basic imputs for the BaseModel class
        """
        my_model = BaseModel()
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number],
                         ["ALX", 89])

    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        pass
    
    def test_datetime(self):
        """
        Tests for correct datetime format
        """
        pass


if __name__ == '__main__':
    unittest.main()
=======
module for base_model unittest
"""

import os
import unittest
import models
from model.base_model import Base_Model

class TestBaseModel(unittest.TestCase)):
    """
    unittest for basemodel
    """

def setup(self):
    try:
        os.rename("file.json", "tmp.json")
    except FileNotFoundError:
        pass

    def tearDown(self):
        """
        teardown temporary files)
        """
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
>>>>>>> 622e914e8a2f7a2a20cf866b2c94a52faabdb70e
