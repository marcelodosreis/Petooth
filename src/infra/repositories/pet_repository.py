from src.domain.models import Pets
from src.infra.config.db_config import DBConnectionHandler
from src.infra.entities import Pets as PetsModel


class PetRepository:
    """Class to manage Pet Repository"""

    @classmethod
    def insert_pet(cls, name: str, specie: str, user_id: int) -> Pets:
        """
        Insert data in PetsEntity
        :param  - name: name of the pet
                - specie: Enum with species acepted
                - user_id: id of the owner (FK)
        :return - tuple with new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsModel(name=name, specie=specie, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    user_id=new_pet.user_id,
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()
