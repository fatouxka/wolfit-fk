from app.forms import LoginForm

def test_login_form(app):
    with app.app_context():
        form = LoginForm()
        form.username.data = "john"
        form.password.data = "yoko"
        assert form.username.data == "john"
        assert form.password.data == "yoko"

def test_login_form_validation(app):
    with app.test_request_context():
        form = LoginForm(data={
            "username": "john",
            "password": "yoko"
        })
        assert form.validate() is True
