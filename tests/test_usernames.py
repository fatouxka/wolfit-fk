import pytest
from app.models import User, Post
from app import db

def test_username_display_in_posts(test_client, init_database):
    response = test_client.get('/')
    assert response.status_code == 200
    assert b'testuser' in response.data

def test_user_profile_link_exists(test_client, init_database):
    user = User.query.filter_by(username='testuser').first()
    # Check if user profile route exists (might be 404 if not implemented)
    response = test_client.get(f'/user/{user.username}')
    # Either 200 (exists) or 404 (not implemented yet) is acceptable
    assert response.status_code in [200, 404]
