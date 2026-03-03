from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, BigInteger
from typing import List
from models.base import Model


class Category(Model):
    name: Mapped[str] = mapped_column(String(255))

    products: Mapped[List["Product"]] = relationship(
        back_populates="category",
        cascade="all, delete"
    )
    def __str__(self):
        return f"{self.id} - {self.name}"

    def __repr__(self):
        return self.name


class Product(Model):
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id")
    )

    category: Mapped["Category"] = relationship(
        back_populates="products"
    )

    carts: Mapped[List["Cart"]] = relationship(
        back_populates="product"
    )

class Cart(Model):
    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False)

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False
    )

    quantity: Mapped[int] = mapped_column(default=1)

    product: Mapped["Product"] = relationship(
        back_populates="carts"
    )
