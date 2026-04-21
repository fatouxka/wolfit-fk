def test_user_repr_method(init_database):
    from app.models import User
    user = User.query.first()
    assert repr(user) is not None
    assert 'User' in repr(user)
    assert 'testuser' in repr(user)

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
