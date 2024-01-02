# Klaar (kan nog vervangen worden met bv. mariadb)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Videogames_database_url = "mysql+mysqlconnector://admin-videogames:games@mariadb/videogames"
Videogames_engine = create_engine(Videogames_database_url, pool_pre_ping=True)
VideogamesSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Videogames_engine)
VideogamesBase = declarative_base()
