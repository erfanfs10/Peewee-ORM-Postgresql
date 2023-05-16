from peewee import *

class BaseModel(Model):
    class Meta:
        database = None


class DatabaseManager:
    def __init__(self, database_name, username, password, host='localhost', port=5432):
        self.database = PostgresqlDatabase(database_name, user=username, password=password, host=host, port=port)

    def connect(self):
        self.database.connect()
        
    def disconnect(self):
        self.database.close()



database_manager = DatabaseManager('YOUR DB NAME', 'DB USER NAME', 'PASSWORD')
database_manager.connect()
database_manager.disconnect()


