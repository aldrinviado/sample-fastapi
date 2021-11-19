from time import timezone
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.orm.util import CascadeOptions
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.sqltypes import TEXT, TIMESTAMP
from .database import Base


# class User(Base):
#     __tablename__ = "users1"

#     id = Column(Integer, primary_key=True, index=True)
#     userid = Column(String, unique=True, index=True)
#     hashed_password = Column(String,nullable= False)
#     emailaddress = Column(String,nullable= False)
#     is_active = Column(Boolean, server_default='True',nullable=False)
#     created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,server_default='TRUE',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=('now()'))
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True,nullable=False)
    password = Column(String,nullable= False)
    is_active = Column(Boolean, server_default='True',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
class Votes(Base):
    __tablename__ = "votes"

    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True, nullable=False)
    user_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True, nullable=False)
    
    
    
#items = relationship("Item", back_populates="owner")