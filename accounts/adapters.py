from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()


class HandongSocialAccountAdapter(DefaultSocialAccountAdapter):

    def is_open_for_signup(self, request, sociallogin):
        email_domain = sociallogin.account.extra_data.get('hd')
        return email_domain in ['handong.ac.kr', 'handong.edu']
