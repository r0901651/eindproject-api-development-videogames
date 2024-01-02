# Nog niet af !!!!!!!!!!!!

from pydantic import BaseModel
from datetime import date
from decimal import Decimal
from typing import List, Optional


class VideogameBase(BaseModel):
    naam: str
    uitgavejaar: date
    rating: float
    prijs: Decimal
    genreid: int
    ontwikkelaarid: int
    platformid: int

class VideogameCreate(VideogameBase):
    pass

class Videogame(VideogameBase):
    id: int
    genre: "Genre"
    ontwikkelaar: "Ontwikkelaar"
    platform: "Platform"

    class Config:
        orm_mode = True


class GenreBase(BaseModel):
    genre: str

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


class OntwikkelaarBase(BaseModel):
    naam: str
    land: str

class OntwikkelaarCreate(OntwikkelaarBase):
    pass

class Ontwikkelaar(OntwikkelaarBase):
    id: int

    class Config:
        orm_mode = True


class PlatformBase(BaseModel):
    platform: str
    ontwikkelaar: str

class PlatformCreate(PlatformBase):
    pass

class Platform(PlatformBase):
    id: int

    class Config:
        orm_mode = True


Videogame.update_forward_refs()