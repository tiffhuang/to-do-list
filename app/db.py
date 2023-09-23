from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace these with your actual RDS database connection details
db_username = 'root'
db_password = 'password'
db_host = 'todolistdb.c52sbppw2srg.us-east-2.rds.amazonaws.com'
db_name = 'your_database_name'  # Replace with your actual database name

# Create a database engine
db_url = f'mysql://{db_username}:{db_password}@{db_host}/{db_name}'
engine = create_engine(db_url, echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)