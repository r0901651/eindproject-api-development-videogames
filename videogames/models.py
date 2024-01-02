# Klaar (kan uitbereiden worden)

from sqlalchemy import Column, ForeignKey, Integer, Float, String, Date
from sqlalchemy.orm import relationship

from database import Base


class Videogame(Base):
    __tablename__ = "videogames"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    naam = Column(String(50), index=True, nullable=False)
    uitgavejaar = Column(Date, nullable=False, index=True)
    rating = Column(Float, nullable=True, index=True)
    prijs = Column(Float, nullable=False, index=True)
    genreid = Column(Integer, ForeignKey("genres.id"), nullable=False)
    ontwikkelaarid = Column(Integer, ForeignKey("ontwikkelaars.id"), nullable=False)
    platformid = Column(Integer, ForeignKey("platformen.id"), nullable=False)

    genre = relationship("Genre", back_populates="videogames")
    ontwikkelaar = relationship("Ontwikkelaar", back_populates="videogames")
    platform = relationship("Platform", back_populates="videogames")


class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    genre = Column(String(50), index=True, unique=True, nullable=False)

    videogames = relationship("Videogame", back_populates="genre")


class Ontwikkelaar(Base):
    __tablename__ = "ontwikkelaars"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    naam = Column(String(50), index=True, unique=True, nullable=False)
    land = Column(String(50), nullable=False)

    videogames = relationship("Videogame", back_populates="ontwikkelaar")


class Platform(Base):
    __tablename__ = "platformen"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    platform = Column(String(50), index=True, unique=True, nullable=False)
    ontwikkelaar = Column(String(50), index=True, nullable=False)

    videogames = relationship("Videogame", back_populates="platform")
