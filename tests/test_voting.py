import pytest
from app.models import User, Post
from app import db

def test_upvote_route_exists(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    
    post = Post.query.first()
    response = test_client.get(f'/upvote/{post.id}', follow_redirects=True)
    assert response.status_code == 200

def test_downvote_route_exists(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    
    post = Post.query.first()
    response = test_client.get(f'/downvote/{post.id}', follow_redirects=True)
    assert response.status_code == 200

def test_upvote_requires_login(test_client, init_database):
    post = Post.query.first()
    response = test_client.get(f'/upvote/{post.id}', follow_redirects=True)
    assert b'Login' in response.data
