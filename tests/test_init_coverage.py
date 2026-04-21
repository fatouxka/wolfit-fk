def test_login_manager_config(test_client, init_database):
    from app import login_manager
    assert login_manager.login_view == 'login'

def test_user_loader_function(test_client, init_database):
    from app import load_user
    user = load_user(1)
    assert user is not None
    assert user.username == 'testuser'
    
    none_user = load_user(99999)
    assert none_user is None
