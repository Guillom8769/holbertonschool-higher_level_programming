#!/usr/bin/python3


import pickle


class CustomObject:
    """
    A custom Python class to demonstrate serialization and deserialization
    using the pickle module.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of CustomObject and save it to the
        provided filename.

        Args:
        filename (str):The name of the file where the object will be saved.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (FileNotFoundError, IOError) as e:
            print(f"Error serializing object: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from the provided filename.

        Args:
            filename (str): The name of the file from which the object will be
            loaded.

        Returns:
            CustomObject: An instance of CustomObject if deserialization is
            successful, None otherwise.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, IOError, pickle.UnpicklingError) as e:
            print(f"Error deserializing object: {e}")
            return None
