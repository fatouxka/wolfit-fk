def test_index_pagination_invalid_page(test_client, init_database):
    response = test_client.get('/?page=999')
    assert response.status_code in [200,404]

def test_create_post_redirect_when_not_logged_in(test_client, init_database):
    response = test_client.get('/create-post')
    assert response.status_code == 302

def test_upvote_invalid_post_returns_404(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/upvote/99999')
    assert response.status_code == 404

def test_downvote_invalid_post_returns_404(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    response = test_client.get('/downvote/99999')
    assert response.status_code == 404

def test_post_nonexistent_returns_404(test_client, init_database):
    response = test_client.get('/post/99999')
    assert response.status_code == 404

def test_user_nonexistent_returns_404(test_client, init_database):
    response = test_client.get('/user/nonexistent_user_xyz')
    assert response.status_code == 404

def test_upvote_with_referer_header(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    headers = {'Referer': '/some-page'}
    response = test_client.get('/upvote/1', headers=headers)
    assert response.status_code in [200, 302, 404]

def test_downvote_with_referer_header(test_client, init_database):
    test_client.post('/login', data={
        'username': 'testuser',
        'password': 'testpassword'
    }, follow_redirects=True)
    headers = {'Referer': '/some-page'}
    response = test_client.get('/downvote/1', headers=headers)
    assert response.status_code in [200, 302, 404]
