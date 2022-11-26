# database_service
This service transfers changes to a database table from one server to another.
When data is changed in the Transaction, Employee, Turn tables, a trigger is fired that writes batch_id, the number of rows changed,
runtime and other useful information to the Batch table. 
The Changes table records the primary keys of the modified table, the type of change (Insert, Update, Delete), and more.
Since data can be transferred to various servers, 
there are auxiliary tables that contain information whether a particular transmission channel / client / group of clients is open.
Database objects can be viewed in the model.py file.

Data transfer in the project is implemented in multi-threaded mode. The PostgreSQL database uses the SqlAlchemy framework.
