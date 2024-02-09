#!/usr/bin/python3
"""
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
