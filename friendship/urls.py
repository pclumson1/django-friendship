from django.urls import include, path

# try:
#     from django.conf.urls import url
# except ImportError:
#     from django.conf.urls.defaults import url

from friendship import views

# from friendship.views import (
#     all_users,
#     block_add,
#     block_remove,
#     blockers,
#     blocking,
#     follower_add,
#     follower_remove,
#     followers,
#     following,
#     friendship_accept,
#     friendship_add_friend,
#     friendship_cancel,
#     friendship_reject,
#     friendship_request_list,
#     friendship_request_list_rejected,
#     friendship_requests_detail,
#     view_friends,
# )

urlpatterns = [

    path('users/', views.all_users, name='friendship_view_users'),
    # url(regex=r"^users/$", view=all_users, name="friendship_view_users"),

    path('<username>/friends/', views.view_friends, name='friendship_view_friends'),
    # url(
    #     regex=r"^friends/(?P<username>[\w-]+)/$",
    #     view=view_friends,
    #     name="friendship_view_friends",
    # ),

    path('<to_username>/friends/add/', views.friendship_add_friend, name='friendship_add_friend'),
    # url(
    #     regex=r"^friend/add/(?P<to_username>[\w-]+)/$",
    #     view=friendship_add_friend,
    #     name="friendship_add_friend",
    # ),

    path('friends/accept/<int:friendship_request_id>', views.friendship_accept, name='friendship_accept'),
    # url(
    #     regex=r"^friend/accept/(?P<friendship_request_id>\d+)/$",
    #     view=friendship_accept,
    #     name="friendship_accept",
    # ),

    path('friend/reject/<int:friendship_request_id>', views.friendship_reject, name='friendship_reject'),
    # url(
    #     regex=r"^friend/reject/(?P<friendship_request_id>\d+)/$",
    #     view=friendship_reject,
    #     name="friendship_reject",
    # ),

    path('friend/cancel/<int:friendship_request_id>', views.friendship_reject, name='friendship_cancel'),
    # url(
    #     regex=r"^friend/cancel/(?P<friendship_request_id>\d+)/$",
    #     view=friendship_cancel,
    #     name="friendship_cancel",
    # ),

    path('friend/requests/', views.friendship_request_list, name='friendship_request_list'),

    #  url(
    #     regex=r"^friend/requests/$",
    #     view=friendship_request_list,
    #     name="friendship_request_list",
    # ), 

    path('friend/requests/rejected/', views.friendship_request_list_rejected, name='friendship_requests_rejected'),
    # url(
    #     regex=r"^friend/requests/rejected/$",
    #     view=friendship_request_list_rejected,
    #     name="friendship_requests_rejected",
    # ),


    path('friend/request/<int:friendship_request_id>', views.friendship_requests_detail, name='friendship_requests_detail'),
    # url(
    #     regex=r"^friend/request/(?P<friendship_request_id>\d+)/$",
    #     view=friendship_requests_detail,
    #     name="friendship_requests_detail",
    # ),

    path('<username>/followers/', views.followers, name='friendship_followers'),
    # url(
    #     regex=r"^followers/(?P<username>[\w-]+)/$",
    #     view=followers,
    #     name="friendship_followers",
    # ),

    path('following/', views.following, name='friendship_following'),
    # url(
    #     regex=r"^following/(?P<username>[\w-]+)/$",
    #     view=following,
    #     name="friendship_following",
    # ),

    path('<followee_username>/follower/add/', views.follower_add, name='follower_add'),
    # url(
    #     regex=r"^follower/add/(?P<followee_username>[\w-]+)/$",
    #     view=follower_add,
    #     name="follower_add",
    # ),

    path('<followee_username>/follower/remove/', views.follower_remove, name='follower_remove'),
    # url(
    #     regex=r"^follower/remove/(?P<followee_username>[\w-]+)/$",
    #     view=follower_remove,
    #     name="follower_remove",
    # ),

    path('<username>/blockers/', views.blockers, name='friendship_blockers'),
    # url(
    #     regex=r"^blockers/(?P<username>[\w-]+)/$",
    #     view=blockers,
    #     name="friendship_blockers",
    # ),

    path('<username>/blocking/', views.blocking, name='friendship_blocking'),

    # url(
    #     regex=r"^blocking/(?P<username>[\w-]+)/$",
    #     view=blocking,
    #     name="friendship_blocking",
    # ),

    path('<blocked_username>/block/add/', views.block_add, name='block_add '),
    # url(
    #     regex=r"^block/add/(?P<blocked_username>[\w-]+)/$",
    #     view=block_add,
    #     name="block_add",
    # ),

    path('<blocked_username>/block/remove/', views.block_remove, name='block_remove'),

    # url(
    #     regex=r"^block/remove/(?P<blocked_username>[\w-]+)/$",
    #     view=block_remove,
    #     name="block_remove",
    # ),
]

