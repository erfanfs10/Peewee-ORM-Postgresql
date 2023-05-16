# peewee-orm-postgresql
This repository provides a Python script that demonstrates how to connect to a PostgreSQL database using Python and Execute CRUD operation using Peewee ORM.


1.
first install requirements with command:
pip install -r requirements.txt

2.
create a postgresql database and create a user

3.
add your database_name , username and password of your database
in main.py file

4.
add your models in models.py

4.
run python main.py create   to add tables to your database

you can update , delete , select , create and drop_table and also create CSV file 

python main.py create  # you have to define fields manualy in the models.py 
python main.py update  # you have to add id manualy in models.py
python main.py select  # select * from table   returns everything in the table
python main.py delete  # you have to add id manualy in models.py
python main.py csv     # creates csv file in you current directory
python main.py drop_table   #drop the table

