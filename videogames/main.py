# uitbereiden ? nog niet af !!!!!
from fastapi import FastAPI, HTTPException, status, Depends, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine
import models
import schemas
import crud
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

security = HTTPBasic()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):

    username = "admin@videogames.com"
    password = "games"

    if credentials.username != username or credentials.password != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return True



# POST method for creating a Videogame
@app.post("/videogames/", response_model=List[schemas.Videogame])
def create_videogames(videogame: List[schemas.VideogameCreate], db: Session = Depends(get_db)):
    return crud.create_videogames(db=db, videogames=videogame)


# GET endpoint to retrieve a list of videogames with optional skip and limit parameters
@app.get("/videogames/", response_model=List[schemas.Videogame])
def read_videogames(skip: int = Query(0, description="Number of items to skip"), limit: int = Query(10, description="Number of items to return"), db: Session = Depends(get_db)):
    videogames = crud.get_videogames(db, skip=skip, limit=limit)
    return videogames


# GET endpoint to retrieve a specific videogame by ID
@app.get("/videogames/{videogame_id}", response_model=schemas.Videogame)
def read_videogame(videogame_id: int, db: Session = Depends(get_db)):
    db_videogame = crud.get_videogame(db, videogame_id)
    if db_videogame is None:
        raise HTTPException(status_code=404, detail="Videogame not found")
    return db_videogame


# DELETE endpoint to delete a videogame by ID
@app.delete("/videogames/{videogame_id}", response_model=schemas.Videogame)
def delete_videogame(videogame_id: int, db: Session = Depends(get_db), authenticated: bool = Depends(authenticate_user)):
    db_videogame = crud.get_videogame(db, videogame_id)
    if db_videogame is None:
        raise HTTPException(status_code=404, detail="Videogame not found")
    db_videogame = crud.delete_videogame(db, videogame_id)
    return db_videogame



# POST method for creating a Genre
@app.post("/genres/", response_model=List[schemas.Genre])
def create_genres(genre: List[schemas.GenreCreate], db: Session = Depends(get_db)):
    return crud.create_genres(db=db, genres=genre)

# GET endpoint to retrieve all genres
@app.get("/genres/", response_model=list[schemas.Genre])
def read_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    genres = crud.get_genres(db, skip=skip, limit=limit)
    return genres

# GET endpoint to retrieve a specific genre by ID
@app.get("/genres/{genre_id}", response_model=schemas.Genre)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = crud.get_genre(db, genre_id=genre_id)
    if genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return genre


# DELETE endpoint to delete a genre by ID
@app.delete("/genres/{genre_id}", response_model=schemas.Genre)
def delete_genre(genre_id: int, db: Session = Depends(get_db), authenticated: bool = Depends(authenticate_user)):
    db_genre = crud.get_genre(db, genre_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    db_genre = crud.delete_genre(db, genre_id)
    return db_genre



# POST method for creating an Ontwikkelaar
@app.post("/ontwikkelaars/", response_model=List[schemas.Ontwikkelaar])
def create_ontwikkelaars(ontwikkelaar: List[schemas.OntwikkelaarCreate], db: Session = Depends(get_db)):
    return crud.create_ontwikkelaars(db=db, ontwikkelaars=ontwikkelaar)

# GET endpoint to retrieve all ontwikkelaars
@app.get("/ontwikkelaars/", response_model=list[schemas.Ontwikkelaar])
def read_ontwikkelaars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    ontwikkelaars = crud.get_ontwikkelaars(db, skip=skip, limit=limit)
    return ontwikkelaars

# GET endpoint to retrieve a specific ontwikkelaar by ID
@app.get("/ontwikkelaars/{ontwikkelaar_id}", response_model=schemas.Ontwikkelaar)
def read_ontwikkelaar(ontwikkelaar_id: int, db: Session = Depends(get_db)):
    ontwikkelaar = crud.get_ontwikkelaar(db, ontwikkelaar_id=ontwikkelaar_id)
    if ontwikkelaar is None:
        raise HTTPException(status_code=404, detail="Ontwikkelaar not found")
    return ontwikkelaar


# DELETE endpoint to delete a ontwikkelaar by ID
@app.delete("/ontwikkelaars/{ontwikkelaar_id}", response_model=schemas.Ontwikkelaar)
def delete_ontwikkelaar(ontwikkelaar_id: int, db: Session = Depends(get_db), authenticated: bool = Depends(authenticate_user)):
    db_ontwikkelaar = crud.get_ontwikkelaar(db, ontwikkelaar_id=ontwikkelaar_id)
    if db_ontwikkelaar is None:
        raise HTTPException(status_code=404, detail="Ontwikkelaar not found")
    db_ontwikkelaar = crud.delete_ontwikkelaar(db, ontwikkelaar_id)
    return db_ontwikkelaar



# POST method for creating a Platform
@app.post("/platformen/", response_model=List[schemas.Platform])
def create_platformen(platform: List[schemas.PlatformCreate], db: Session = Depends(get_db)):
    return crud.create_platformen(db=db, platforms=platform)


# GET endpoint to retrieve all platforms
@app.get("/platformen/", response_model=list[schemas.Platform])
def read_platformen(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    platforms = crud.get_platformen(db, skip=skip, limit=limit)
    return platforms


# GET endpoint to retrieve a specific platform by ID
@app.get("/platformen/{platform_id}", response_model=schemas.Platform)
def read_platform(platform_id: int, db: Session = Depends(get_db)):
    platform = crud.get_platform(db, platform_id=platform_id)
    if platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return platform


# DELETE endpoint to delete a platform by ID
@app.delete("/platformen/{platform_id}", response_model=schemas.Platform)
def delete_platform(platform_id: int, db: Session = Depends(get_db), authenticated: bool = Depends(authenticate_user)):
    db_platform = crud.get_platform(db, platform_id=platform_id)
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    db_platform = crud.delete_platform(db, platform_id)
    return db_platform