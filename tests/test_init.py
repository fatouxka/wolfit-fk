def test_app_debug_mode():
    from app import create_app
    app = create_app()
    assert app is not None
    assert app.config['SECRET_KEY'] is not None

def test_login_manager_config():
    from app import login_manager
    assert login_manager.login_view == 'login'
