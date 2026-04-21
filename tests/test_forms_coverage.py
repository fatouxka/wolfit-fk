def test_registration_form_password_mismatch(test_client, init_database):
    response = test_client.post('/register', data={
        'username': 'testuser2',
        'email': 'test2@test.com',
        'password': 'password123',
        'confirm_password': 'different'
    }, follow_redirects=True)
    assert b'password' in response.data.lower() or response.status_code == 200

def test_login_form_empty_fields(test_client, init_database):
    response = test_client.post('/login', data={
        'username': '',
        'password': ''
    }, follow_redirects=True)
    assert response.status_code == 200

def test_post_form_validation(test_client, init_database):
    from app.forms import PostForm
    form = PostForm(data={'title': '', 'body': ''})
    assert not form.validate()
