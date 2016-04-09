from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic import View

from users.models import Follow


class UserFollowView(View):
    def get(self, request, *args, **kwargs):
        follower_nickname = kwargs.get("slug")
        follower = get_user_model().objects.get(
            nickname=follower_nickname,
        )

        follow_object, is_created = Follow.objects.get_or_create(
            followee=request.user,
            follower=follower,
        )

        return redirect(follow_object)
