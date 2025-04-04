from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    avatar = Column(String, nullable=True)
    email = Column(String, unique=True, index=True)

    posts = relationship('Post', back_populates='owner', cascade="all, delete")
