import pytest
from app.models import Post, Category
from app import db
from app.forms import PostForm

def test_create_post_requires_login(test_client, init_database):
    response = test_client.get('/create-post', follow_redirects=True)
    assert b'Login' in response.data

def test_create_post_page_loads(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    
    response = test_client.get('/create-post')
    assert response.status_code == 200
    assert b'Create' in response.data or b'Post' in response.data
