from faker import Faker

from src.infra.tests.user_repository_spy import UserRepositorySpy
from .register_user import RegisterUser

faker = Faker()


def test_register_user():
    """Testing registry method"""

    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository)

    attributes = {"name": faker.name(), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"],
        password=attributes["password"],
    )

    # Testing input
    assert user_repository.insert_user_params["name"] == attributes["name"]
    assert user_repository.insert_user_params["password"] == attributes["password"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]


def test_register_user_fail():
    """Testing registry method in Fail"""

    user_repository = UserRepositorySpy()
    register_user = RegisterUser(user_repository)

    attributes = {"name": faker.random_number(digits=2), "password": faker.name()}

    response = register_user.register(
        name=attributes["name"],
        password=attributes["password"],
    )

    # Testing input
    assert user_repository.insert_user_params == {}
    # Testing outputs
    assert response["Success"] is False
    assert response["Data"] is None
