import pytest
from app import create_app, db
from app.models import User, Post, Category
from config import Config

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    LOGIN_DISABLED = False
    SECRET_KEY = 'test-secret-key'

@pytest.fixture
def app():
    app = create_app()
    app.config.from_object(TestConfig)
    return app

@pytest.fixture
def test_client(app):
    return app.test_client()

@pytest.fixture
def init_database(test_client, app):
    with app.app_context():
        db.create_all()
        
        user = User(username='testuser', email='test@test.com')
        user.set_password('testpassword')
        db.session.add(user)
        db.session.commit()
        
        category = Category(title='Python')
        db.session.add(category)
        db.session.commit()
        
        post = Post(
            title='Test Post',
            body='Test body content',
            author_id=user.id,
            category_id=category.id
        )
        db.session.add(post)
        db.session.commit()
        
        yield db
        
        db.drop_all()
