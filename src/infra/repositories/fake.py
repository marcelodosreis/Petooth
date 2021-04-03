from src.infra.config import DBConnectionHandler
from src.infra.entities import Users


class FakerRepository:
    """ Simple fake repository """

    @classmethod
    def insert_user(cls):
        """ Insert User Method """

    with DBConnectionHandler() as db_connection:
        try:
            new_user = Users(name="Marcelo", password="123456")
            db_connection.session.add(new_user)
            db_connection.session.commit()
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()
