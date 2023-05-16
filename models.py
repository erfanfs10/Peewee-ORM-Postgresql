from peewee import *
from datetime import datetime
import csv


class BaseModel(Model):
    class Meta:
        database = None


class Device(BaseModel):

    SMS = 1
    VOICE = 2
    CALL_FORWARD = 2

    CALL_TYPES = (
        (SMS, "SMS"),
        (VOICE, "VOICE"),
        (CALL_FORWARD, "CALL_FORWARD")
    )

    Anum = CharField(max_length=13 ,verbose_name='phone number starts with 98')
    Bnum = CharField(max_length=13 ,verbose_name='phone number starts with 98')
    Cnum = CharField(max_length=13 ,verbose_name='phone number starts with 98')
    duration = DecimalField(max_digits=4, decimal_places=2,
                             auto_round=True, verbose_name="round up second base number")
    location = CharField(max_length=10,
                          verbose_name="hex(lac)-hex(cell) sample CD8E-5F98 5 digit max each",
                          null=True)
    call_type = SmallIntegerField(choices=CALL_TYPES, default=SMS)
    device_name = CharField(max_length=255, verbose_name="name of the device")
    created = DateTimeField(default=datetime.now, formats=['%Y-%m-%d %H:%M:%S'])

    @property
    def formatted_time(self):
        return self.created.strftime('%Y-%m-%d %H:%M:%S')

    class Meta:
        table_name = "device"


class DeviceManager:
    def create(self, Anum="41", Bnum="96", Cnum="3",
                                            duration=7.10, location="K046E207",
                                             device_name="device number three"):
        
        new_device = Device(Anum=Anum, Bnum=Bnum, Cnum=Cnum,
                                            duration=duration, location=location,
                                             device_name=device_name)
        new_device.save()
        print(f"The New Device has made with Name '{device_name}'")


    def update(self, device_id=1, device_name="updated one"):
        try:
            device = Device.get(Device.id == device_id)
        except:
            print(f"There is no Device with ID {device_id} to UPDATE!")  
            return  
        device.device_name = device_name
        device.save()
        print(f"The Devies With ID {device_id} UPDATED Successfuly.")


    def select(self):
        devices = Device.select()
        if devices:
            for device in devices:
                print("id:", device.id, "\nAnum:", device.Anum,"\nBnum:", device.Bnum,
                       "\nduration:", device.duration, "\nlocation:", device.location,
                         "\ncall_type:", device.call_type, "\ndevice_name:",
                           device.device_name, "\ncreated:", device.formatted_time,"\n")
        else:        
            print("There is no Data in The Table!")


    def delete(self, device_id=1):
        try:
            device = Device.get(Device.id == device_id)
        except:
            print(f"There Is No Device With ID {device_id} To DELETE!")  
            return  
        device.delete_instance()
        print(f"The Device With ID {device_id} DELETED Successfuly.")


    def export_to_csv(self):
        devices = Device.select()
        if devices:
            with open("device.csv", 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['ID', 'Anum', 'Bnum', 'Cnum','duration',
                                'location', 'call_type', 'device_name', 'created'])  # Write header
                for device in devices:
                    writer.writerow([device.id, device.Anum, device.Bnum,
                                     device.Cnum, device.duration, device.location,
                                     device.call_type, device.device_name, device.formatted_time])
        else:
            print("There is No Data in The Table to create CSV!")

