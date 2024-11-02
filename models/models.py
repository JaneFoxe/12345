from sqlalchemy import MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric

from sqlalchemy.orm import relationship

from datetime import datetime
from db import engine, Base


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer(), primary_key=True)
    customer_id = Column(Integer(), ForeignKey('users.id'))
    products = relationship("Product", backref='order')
    total_amount = Column(Numeric(10), nullable=False)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200), nullable=True)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200), nullable=True)
    category = Column(Integer(), ForeignKey('categories.id'))
    rating = Column(Numeric(2, 1), nullable=False)
    rewiews = Column(String(200), nullable=True)
    cost_price = Column(Numeric(10), nullable=False)
    quantity = Column(Integer())


class Productsinshop(Base):
    __tablename__ = 'products_in_shop'
    id = Column(Integer(), primary_key=True)
    product = Column(Integer(), ForeignKey('products.id'))
    shop = Column(Integer(), ForeignKey('shops.id'))


class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer(), primary_key=True)
    name = Column(String(200), nullable=False)
    description = Column(String(200), nullable=True)
    products = Column(Integer(), ForeignKey('products.id'))
    rating = Column(Numeric(2, 1), nullable=False)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    favorite_products = Column(Integer(), ForeignKey('products.id'))
    orders = relationship("Order", backref='users')


class BankAccounts(Base):
    __tablename__ = 'bank_accounts'
    account_id = Column(Integer(), primary_key=True)
    balance = Column(Numeric(10), nullable=False)


Base.metadata.create_all(engine)
