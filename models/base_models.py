#!/usr/bin/python3
"""
module for base model class
"""
import uuid
import models
from datetime import datetime

class basemodel:
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

                if kwargs:
                for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at"
                setattr(self, key, datetime.strptime(value, time_format))
            else:
                setattr(self, key, value)

                models.storage.new(self)

                def save(self)
                """
                update updated_at with current datetime.utcnow
                """
                self.updated_at = datetime.utcnow()
                model.storage.save()

                def to_dict(self):
                    """
                    return the dictionary of the BaseModel instance
                    """
                    inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return int_dict

    def __str__(self)
    """
    return the str representation of the BaseModel instance"""
class name = self.__class__.__name__
return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

