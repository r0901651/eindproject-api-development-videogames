# uitbereiding ? nog niet af !!!!!
from sqlalchemy.orm import Session, joinedload
from models import Videogame, Genre, Ontwikkelaar, Platform
from schemas import VideogameCreate, GenreCreate, OntwikkelaarCreate, PlatformCreate
from typing import List

# CRUD operations for Videogames
def create_videogames(db: Session, videogames: List[VideogameCreate]):
    created_videogames = []
    for videogame_data in videogames:
        db_videogame = Videogame(**videogame_data.dict())
        db.add(db_videogame)
        db.commit()
        db.refresh(db_videogame)
        created_videogames.append(db_videogame)
    return created_videogames

def get_videogame(db: Session, videogame_id: int):
    return db.query(Videogame).filter(Videogame.id == videogame_id).first()

def get_videogames(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Videogame).offset(skip).limit(limit).all()

def delete_videogame(db: Session, videogame_id: int):
    db_videogame = db.query(Videogame).options(joinedload(Videogame.genre), joinedload(Videogame.ontwikkelaar), joinedload(Videogame.platform)).filter(Videogame.id == videogame_id).first()
    if db_videogame:
        db.delete(db_videogame)
        db.commit()
        return db_videogame
    return None

# CRUD operations for Genres
def create_genres(db: Session, genres: List[GenreCreate]):
    created_genres = []
    for genre_data in genres:
        db_genre = Genre(**genre_data.dict())
        db.add(db_genre)
        db.commit()
        db.refresh(db_genre)
        created_genres.append(db_genre)
    return created_genres

def get_genre(db: Session, genre_id: int):
    return db.query(Genre).filter(Genre.id == genre_id).first()

def get_genres(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Genre).offset(skip).limit(limit).all()

def delete_genre(db: Session, genre_id: int):
    db_genre = db.query(Genre).filter(Genre.id == genre_id).first()
    if db_genre:
        db.delete(db_genre)
        db.commit()
        return db_genre
    return None

# CRUD operations for Ontwikkelaars
def create_ontwikkelaars(db: Session, ontwikkelaars: List[OntwikkelaarCreate]):
    created_ontwikkerlaars = []
    for ontwikkelaar_data in ontwikkelaars:
        db_ontwikkelaar = Ontwikkelaar(**ontwikkelaar_data.dict())
        db.add(db_ontwikkelaar)
        db.commit()
        db.refresh(db_ontwikkelaar)
        created_ontwikkerlaars.append(db_ontwikkelaar)
    return created_ontwikkerlaars

def get_ontwikkelaar(db: Session, ontwikkelaar_id: int):
    return db.query(Ontwikkelaar).filter(Ontwikkelaar.id == ontwikkelaar_id).first()

def get_ontwikkelaars(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Ontwikkelaar).offset(skip).limit(limit).all()

def delete_ontwikkelaar(db: Session, ontwikkelaar_id: int):
    db_ontwikkelaar = db.query(Ontwikkelaar).filter(Ontwikkelaar.id == ontwikkelaar_id).first()
    if db_ontwikkelaar:
        db.delete(db_ontwikkelaar)
        db.commit()
        return db_ontwikkelaar
    return None

# CRUD operations for Platforms
def create_platformen(db: Session, platforms: List[PlatformCreate]):
    created_platforms = []
    for platform_data in platforms:
        db_platform = Platform(**platform_data.dict())
        db.add(db_platform)
        db.commit()
        db.refresh(db_platform)
        created_platforms.append(db_platform)
    return created_platforms

def get_platform(db: Session, platform_id: int):
    return db.query(Platform).filter(Platform.id == platform_id).first()

def get_platformen(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Platform).offset(skip).limit(limit).all()

def delete_platform(db: Session, platform_id: int):
    db_platform = db.query(Platform).filter(Platform.id == platform_id).first()
    if db_platform:
        db.delete(db_platform)
        db.commit()
        return db_platform
    return None