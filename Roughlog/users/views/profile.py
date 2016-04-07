from django.contrib.auth import get_user_model
from django.views.generic import DetailView


class UserProfilePage(DetailView):
    model = get_user_model()
    template_name = "users/profile.html"
    slug_field = "nickname"
