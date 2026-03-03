from sqlalchemy import String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from models.base import Model

class User(Model):
    name: Mapped[str] = mapped_column(String)
    birth_date: Mapped[int] = mapped_column(Integer)
    phone: Mapped[str] = mapped_column(String(12), unique=True)






#