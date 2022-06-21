from faker import Faker
from .pet_repository import PetRepository
from src.infra.config import DBConnectionHandler

faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pet():
    """Should insert pet in Pet Table and return it"""

    name = faker.name()
    specie = "dog"
    user_id = faker.random_number()

    # SQL
    new_pet = pet_repository.insert_pet(name, specie, user_id)
    engine = db_connection_handler.get_engine()
    query_pet = engine.execute(
        "SELECT * from pets WHERE id='{}';".format(new_pet.id)
    ).fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.specie == query_pet.specie
    assert new_pet.name == query_pet.name
    assert new_pet.user_id == query_pet.user_id

    engine.execute("DELETE FROM pets WHERE id='{}';".format(new_pet.id))
