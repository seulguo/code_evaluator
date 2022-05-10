from allauth.account.forms import LoginForm


class GoogleSocialLoginForm(LoginForm):

    def login(self, *args, **kwargs):
        return super().login(*args, **kwargs)
