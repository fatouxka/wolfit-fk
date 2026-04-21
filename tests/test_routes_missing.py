def test_index_page_out_of_range(test_client, init_database):
    response = test_client.get('/?page=999')
    assert response.status_code in [200, 404]

def test_create_post_redirects_to_login(test_client, init_database):
    response = test_client.get('/create-post')
    assert response.status_code == 302

def test_upvote_nonexistent_post(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/upvote/99999')
    assert response.status_code == 404

def test_downvote_nonexistent_post(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/downvote/99999')
    assert response.status_code == 404

def test_post_not_found(test_client, init_database):
    response = test_client.get('/post/99999')
    assert response.status_code == 404

def test_user_not_found(test_client, init_database):
    response = test_client.get('/user/nonexistent_user')
    assert response.status_code == 404

def test_upvote_with_referer(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    headers = {'Referer': '/previous-page'}
    response = test_client.get('/upvote/1', headers=headers)
    assert response.status_code in [200, 302, 404]

def test_downvote_with_referer(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    headers = {'Referer': '/previous-page'}
    response = test_client.get('/downvote/1', headers=headers)
    assert response.status_code in [200, 302, 404]
