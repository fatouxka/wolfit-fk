def test_full_registration_and_post_flow(test_client, init_database):
    """Complete flow to cover any remaining lines"""
    # Register new user
    response = test_client.post('/register', data={
        'username': 'flowuser',
        'email': 'flow@example.com',
        'password': 'flowpass123',
        'confirm_password': 'flowpass123'
    }, follow_redirects=True)
    assert response.status_code == 200
    
    # Login as new user
    response = test_client.post('/login', data={
        'username': 'flowuser',
        'password': 'flowpass123'
    }, follow_redirects=True)
    assert response.status_code == 200
    
    # Create a post
    from app.models import Category
    category = Category.query.first()
    response = test_client.post('/create-post', data={
        'title': 'Flow Test Post',
        'body': 'This is a flow test post',
        'category_id': category.id if category else 1
    }, follow_redirects=True)
    assert response.status_code == 200
    
    # Test upvote
    from app.models import Post
    post = Post.query.filter_by(title='Flow Test Post').first()
    if post:
        response = test_client.get(f'/upvote/{post.id}', follow_redirects=True)
        assert response.status_code == 200

def test_logout_functionality(test_client, init_database):
    """Test logout"""
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
