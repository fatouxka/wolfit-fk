def test_logout_route(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/logout', follow_redirects=True)
    assert response.status_code == 200

def test_register_existing_user(test_client, init_database):
    response = test_client.post('/register', data={
        'username': 'testuser',
        'email': 'test@test.com',
        'password': 'password123',
        'confirm_password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_login_invalid_credentials(test_client, init_database):
    response = test_client.post('/login', data={
        'username': 'wronguser',
        'password': 'wrongpass'
    }, follow_redirects=True)
    assert b'Login' in response.data or b'username' in response.data.lower()
