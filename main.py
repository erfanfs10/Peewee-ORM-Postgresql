from peewee import *
import csv
from models import Device
from local_setting import DB_NAME, DB_UESR, DB_PASSWORD


class DatabaseManager:
    def __init__(self, database_name, username, password, host='localhost', port=5432):
        self.database = PostgresqlDatabase(database_name, user=username, password=password, host=host, port=port)

    def connect(self):
        self.database.connect()
        Device._meta.database = self.database
        self.database.create_tables([Device])
        
        
    def disconnect(self):
        self.database.close()


class DeviceManager:
    def create_device(self, name, price):
        new_device = Device(name=name, price=price)
        new_device.save()

    def update_device(self, device_id, name, price):
        device = Device.get(Device.id == device_id)
        device.name = name
        device.price = price
        device.save()

    def query_devices(self):
        devices = Device.select()
        for device in devices:
            print(device.id, device.name, device.price)

    def delete_device(self, device_id):
        device = Device.get(Device.id == device_id)
        device.delete_instance()

    def export_to_csv(self, file_path):
        devices = Device.select()
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Name', 'Price'])  # Write header
            for device in devices:
                writer.writerow([device.id, device.name, device.price])




database_manager = DatabaseManager(DB_NAME, DB_UESR, DB_PASSWORD)
database_manager.connect()

device_manager = DeviceManager()
device_manager.create_device()
device_manager.update_device()
device_manager.query_devices()
device_manager.export_to_csv('devices.csv')
device_manager.delete_device()


database_manager.disconnect()


