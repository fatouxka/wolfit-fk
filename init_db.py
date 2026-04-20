#!/usr/bin/env python
from app import create_app, db
from app.models import User, Post, Category, Comment

app = create_app()

with app.app_context():
    db.create_all()
    print("Database tables created successfully")
    from sqlalchemy import inspect
    inspector = inspect(db.engine)
    print("Tables:", inspector.get_table_names())
