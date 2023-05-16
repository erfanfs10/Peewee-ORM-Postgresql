from peewee import *


class BaseModel(Model):
    class Meta:
        database = None


class Device(BaseModel):
    Anum = CharField(max_length=13 ,verbose_name='phone number starts with 98')
    Bnum = CharField(max_length=13 ,verbose_name='phone number starts with 98')
    Cnum = CharField(max_length=13 ,verbose_name='phone number starts with 98')
    duration = DecimalField(max_digits=4, decimal_places=2, auto_round=True)
    

    class Meta:
        table_name = "devices"
        
        