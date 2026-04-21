def test_pagination_exists(test_client, init_database):
    response = test_client.get('/')
    assert response.status_code == 200
    # Check that pagination div exists
    assert b'pagination' in response.data
