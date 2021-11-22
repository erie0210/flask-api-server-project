# -*- coding: utf-8 -*-
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MyUser(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(20,'utf8mb4_unicode_ci'))
    password = db.Column(db.String(20,'utf8mb4_unicode_ci'))
    created_at = db.Column(db.DateTime, server_default = db.FetchedValue())
    updated_at = db.Column(db.DateTime, server_default = db.FetchedValue())

    def __init__(self, email, password, created_at, updated_at):
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(20,'utf8mb4_unicode_ci'), nullable=False)
    body = db.Column(db.String(2000,'utf8mb4_unicode_ci'))
    created_at = db.Column(db.DateTime, server_default = db.FetchedValue())
    updated_at = db.Column(db.DateTime, server_default = db.FetchedValue())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    deleted = db.Column(db.Boolean, default=0)

    def __init__(self, amount, title, body, created_at, updated_at, author_id, deleted):
        self.id = id
        self.amount = amount
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at
        self.author_id = author_id
        self.deleted = deleted