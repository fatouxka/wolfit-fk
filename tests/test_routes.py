def test_homepage(test_client, init_database):
    response = test_client.get('/')
    assert response.status_code == 200

def test_login_page(test_client, init_database):
    response = test_client.get('/login')
    assert response.status_code == 200

def test_register_page(test_client, init_database):
    response = test_client.get('/register')
    assert response.status_code == 200

def test_create_post_redirects(test_client, init_database):
    response = test_client.get('/create-post', follow_redirects=True)
    assert response.status_code == 200

def test_post_page(test_client, init_database):
    response = test_client.get('/post/1')
    assert response.status_code == 200
