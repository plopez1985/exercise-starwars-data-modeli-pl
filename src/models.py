import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    fecha_suscripcion = Column(DateTime(timezone=True), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250),nullable=False)
    diameter = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
      
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(250),nullable=False)
    height = Column(Integer,nullable=False)
    hair_color = Column(String(250),nullable=False)
    eye_color = Column(String(250),nullable=False)
    
class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250),nullable=False)
    cost_in_credits = Column(String(250),nullable=False)
    model = Column(String(250),nullable=False)
    passengers = Column(String(250),nullable=False)
   
class Create_planet(Base):
    __tablename__ = 'create_planet'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_create_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    create = relationship(User, Planet)

class Create_vehicle(Base):
    __tablename__ = 'create_vehicle'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    vehicle_create_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    create = relationship(User, Vehicle)

class Create_character(Base):
    __tablename__ = 'create_character'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_create_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    create = relationship(User, Character)

class Favorito_planet(Base):
    __tablename__ = 'favorito_planet'
    id = Column(Integer, primary_key=True)
    planet_favorito_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    favorito_planet = relationship(User, Planet)
    
class Favorito_character(Base):
    __tablename__ = 'favorito_character'
    id = Column(Integer, primary_key=True)
    character_favorito_id = Column(Integer, ForeignKey('character.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    favorito_character = relationship(User, Character)

class Favorito_cehicle(Base):
    __tablename__ = 'favorito_vehicle'
    id = Column(Integer, primary_key=True)
    vehicle_favorito_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    favorito_vehicle = relationship(User, Vehicle)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
