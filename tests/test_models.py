import pytest
from app.models import User, Post, Category

def test_user_creation(init_database):
    user = User.query.filter_by(username='testuser').first()
    assert user is not None
    assert user.username == 'testuser'

def test_post_creation(init_database):
    post = Post.query.first()
    assert post is not None
    assert post.title == 'Test Post'
    assert post.body == 'Test body content'

def test_category_creation(init_database):
    category = Category.query.first()
    assert category is not None
    assert category.title == 'Python'
def test_user_repr_method(init_database):
    from app.models import User
    user = User.query.first()
    assert repr(user) is not None
    assert 'User' in repr(user)

def test_post_repr_method(init_database):
    from app.models import Post
    post = Post.query.first()
    assert repr(post) is not None
    assert 'Post' in repr(post)

def test_category_repr_method(init_database):
    from app.models import Category
    category = Category.query.first()
    assert repr(category) is not None
    assert 'Category' in repr(category)
