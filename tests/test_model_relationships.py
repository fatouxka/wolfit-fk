from app.models import User, Post, Category
from app import db

def test_user_posts_relationship(init_database):
    user = User.query.filter_by(username='testuser').first()
    assert hasattr(user, 'posts')

def test_post_author_relationship(init_database):
    post = Post.query.first()
    assert hasattr(post, 'author')
    assert post.author.username == 'testuser'

def test_category_posts_relationship(init_database):
    category = Category.query.first()
    assert hasattr(category, 'posts')

def test_post_category_relationship(init_database):
    post = Post.query.first()
    assert hasattr(post, 'category')

def test_cascade_delete(init_database):
    from app import db
    user = User(username='tempuser', email='temp@test.com')
    user.set_password('temp')
    db.session.add(user)
    db.session.commit()
    
    post = Post(title='Temp Post', body='Temp', author=user, category_id=1)
    db.session.add(post)
    db.session.commit()
    
    db.session.delete(user)
    db.session.commit()
    
    deleted_user = User.query.get(user.id)
    assert deleted_user is None
