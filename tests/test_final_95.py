import pytest
from app import create_app
from app.models import User, Post, Category
from app import db

def test_routes_lines_42_50(test_client, init_database):
    """Cover lines 42-50: user creation, db add, commit, flash, redirect"""
    # Use a unique username
    response = test_client.post('/register', data={
        'username': 'testuser42',
        'email': 'test42@example.com',
        'password': 'testpass123',
        'confirm_password': 'testpass123'
    }, follow_redirects=True)
    assert response.status_code == 200
    
    # Verify the user was created (covers lines 42-50)
    user = User.query.filter_by(username='testuser42').first()
    assert user is not None
    assert user.email == 'test42@example.com'

def test_routes_lines_66_69(test_client, init_database):
    """Cover lines 66-69: post creation, db add, commit, flash, redirect"""
    # Login first
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    
    # Get a category
    category = Category.query.first()
    if not category:
        category = Category(title='General')
        db.session.add(category)
        db.session.commit()
    
    # Create a post (covers lines 66-69)
    response = test_client.post('/create-post', data={
        'title': 'Test Post Lines 66-69',
        'body': 'This post covers lines 66-69',
        'category_id': category.id
    }, follow_redirects=True)
    assert response.status_code == 200
    
    # Verify the post was created
    post = Post.query.filter_by(title='Test Post Lines 66-69').first()
    assert post is not None
    assert post.body == 'This post covers lines 66-69'

def test_helpers_line_36():
    """Cover helpers.py line 36"""
    from app.helpers import pretty_date
    assert pretty_date(None) == 'just now'
    assert pretty_date('') == 'just now'

def test_models_line_7(init_database):
    """Cover models.py line 7 - User __repr__"""
    user = User.query.filter_by(username='testuser').first()
    assert user is not None
    repr_str = repr(user)
    assert 'User' in repr_str

def test_models_line_61(init_database):
    """Cover models.py line 61 - Category __repr__"""
    category = Category.query.first()
    if category:
        repr_str = repr(category)
        assert 'Category' in repr_str
