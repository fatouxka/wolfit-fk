import pytest
from app import create_app
from app.models import User, Post, Category
from app.helpers import pretty_date
from app import db

def test_helpers_line_36():
    """Cover helpers.py line 36 - pretty_date edge case"""
    assert pretty_date(None) == 'just now'
    assert pretty_date('') == 'just now'
    assert pretty_date('invalid') == 'just now'

def test_models_line_7(init_database):
    """Cover models.py line 7 - User __repr__"""
    user = User.query.filter_by(username='testuser').first()
    assert user is not None
    repr_str = repr(user)
    assert 'User' in repr_str

def test_models_line_61(init_database):
    """Cover models.py line 61 - Category __repr__"""
    category = Category.query.first()
    assert category is not None
    repr_str = repr(category)
    assert 'Category' in repr_str

def test_routes_lines_42_50(test_client, init_database):
    """Cover routes.py lines 42-50 - registration success"""
    # Use a unique username to avoid conflicts
    import time
    unique_username = f'newuser_{int(time.time())}'
    
    response = test_client.post('/register', data={
        'username': unique_username,
        'email': f'{unique_username}@example.com',
        'password': 'testpass123',
        'confirm_password': 'testpass123'
    }, follow_redirects=True)
    assert response.status_code == 200
    
    # Verify user was created
    user = User.query.filter_by(username=unique_username).first()
    assert user is not None

def test_routes_lines_66_69(test_client, init_database):
    """Cover routes.py lines 66-69 - post creation success"""
    # Login
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    
    # Get or create category
    category = Category.query.first()
    if not category:
        category = Category(title='General')
        db.session.add(category)
        db.session.commit()
    
    assert category is not None
    
    response = test_client.post('/create-post', data={
        'title': '100 Percent Post',
        'body': 'This covers lines 66-69',
        'category_id': category.id
    }, follow_redirects=True)
    assert response.status_code == 200
    
    # Verify post was created
    post = Post.query.filter_by(title='100 Percent Post').first()
    assert post is not None

def test_routes_line_20(test_client, init_database):
    """Cover line 20 - login redirect when already authenticated"""
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/login', follow_redirects=True)
    assert response.status_code == 200

def test_routes_line_39(test_client, init_database):
    """Cover line 39 - register redirect when already authenticated"""
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/register', follow_redirects=True)
    assert response.status_code == 200
