from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        username_check = re.match('^[a-z][a-z][a-z]+$', username)
        password_check = re.match("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", password)

        if not username_check:
            raise UserInputError("Invalid username")

        if not password_check:
            raise UserInputError("Invalid password")
        
        if password != password_confirmation:
            raise UserInputError("Passwords dont match")

user_service = UserService()
