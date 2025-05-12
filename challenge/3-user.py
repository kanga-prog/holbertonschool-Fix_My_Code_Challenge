#!/usr/bin/env python3
import hashlib


class User:
    """User class with password hashing and validation."""

    def __init__(self, password):
        self.__password = None
        self.set_password(password)

    def set_password(self, password):
        """Hash and set the password"""
        if type(password) is str:
            self.__password = hashlib.md5(password.encode()).hexdigest()

    def is_valid_password(self, password):
        """Check if the password matches the stored hashed password"""
        if type(password) is not str or self.__password is None:
            return False
        return hashlib.md5(password.encode()).hexdigest() == self.__password


if __name__ == "__main__":
    print("Test User")

    user = User("holberton")
    assert user.is_valid_password("holberton") is True, "is_valid_password should return True if it's the right password"
    assert user.is_valid_password("wrong") is False, "is_valid_password should return False if password is wrong"
    print("All tests passed.")
