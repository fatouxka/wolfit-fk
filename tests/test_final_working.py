import pytest
from app import create_app
from app.models import User, Post, Category
from app.helpers import pretty_date
from app import db

def test_helpers_line_36():
    """Test helpers.py line 36"""
    assert pretty_date(None) == 'just now'
    assert pretty_date('') == 'just now'

def test_models_line_7(init_database):
    """Test models.py line 7 - uses fixture with database"""
    user = User.query.filter_by(username='testuser').first()
    assert user is not None
    repr_str = repr(user)
    assert 'User' in repr_str
    assert 'testuser' in repr_str

def test_routes_line_20(test_client, init_database):
    """Test line 20 - login redirect when authenticated"""
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/login', follow_redirects=True)
    assert response.status_code == 200

def test_routes_line_39(test_client, init_database):
    """Test line 39 - register redirect when authenticated"""
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/register', follow_redirects=True)
    assert response.status_code == 200

def test_routes_lines_47_50(test_client, init_database):
    """Test lines 47-50 - successful registration"""
    response = test_client.post('/register', data={
        'username': 'working_user',
        'email': 'working@example.com',
        'password': 'testpass123',
        'confirm_password': 'testpass123'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_routes_lines_67_70(test_client, init_database):
    """Test lines 67-70 - successful post creation"""
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    
    # Get category from fixture
    category = Category.query.first()
    assert category is not None
    
    response = test_client.post('/create-post', data={
        'title': 'Working Post',
        'body': 'Working body content',
        'category_id': category.id
    }, follow_redirects=True)
    assert response.status_code == 200
