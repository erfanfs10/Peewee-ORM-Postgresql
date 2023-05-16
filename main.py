from peewee import *
from db_manager import DatabaseManager
from models import DeviceManager, Device
import sys


database_manager = DatabaseManager('DATABASE_NAME', "USERNAME", "PASSWORD")
database_manager.connect()
device = DeviceManager()

ALLOWED_COMMANDS = {"create": device.create,
                    "update": device.update,
                    "select": device.select, 
                    "delete": device.delete,
                    "csv": device.export_to_csv,
                    "drop_table": database_manager.database.drop_tables
                    }


if __name__ == "__main__":

    command = sys.argv

    if command[1] == "drop_table":
        func = ALLOWED_COMMANDS.get(command[1], None)
        if func is None:
            print("The Allowed Commands Are:\ncreate\nupdate\nselect\ndelete\ncsv\ndrop 'table_name'")    
        else:
            func(Device)
            print("The Device Table DELETED Successfuly.\n")
            print("\nThe Command Executed Successfuly.")

           
    else:
        func = ALLOWED_COMMANDS.get(command[1], None)
        if func is None:
            print("The Allowed Commands Are:\ncreate\nupdate\nselect\ndelete\ncsv\ndrop 'table_name'")    
        else:
            func()
            print("\nThe Command Executed Successfuly.")

         
database_manager.disconnect()
