def test_registration_correct_fields(test_client, init_database):
    """Use correct field names: password2 instead of confirm_password"""
    import time
    unique_name = f'correctuser_{int(time.time())}'
    
    response = test_client.post('/register', data={
        'username': unique_name,
        'email': f'{unique_name}@example.com',
        'password': 'testpass123',
        'password2': 'testpass123'  # This is the correct field name
    }, follow_redirects=True)
    
    assert response.status_code == 200
    
    from app.models import User
    user = User.query.filter_by(username=unique_name).first()
    assert user is not None, f"User {unique_name} was not created"

def test_routes_lines_42_50_correct(test_client, init_database):
    """Cover lines 42-50 with correct form field names"""
    import time
    unique_name = f'line42correct_{int(time.time())}'
    
    response = test_client.post('/register', data={
        'username': unique_name,
        'email': f'{unique_name}@test.com',
        'password': 'ValidPass123',
        'password2': 'ValidPass123'  # Correct field name
    }, follow_redirects=True)
    
    assert response.status_code == 200
    
    from app.models import User
    user = User.query.filter_by(username=unique_name).first()
    assert user is not None
    assert user.email == f'{unique_name}@test.com'
