from django.urls import path
from .views import PasswordChangeRequestView, PasswordChangeConfirmView, CreateUser, UsersView, Complaint, \
    CreateUserConfirmation, GetAuthenticatedUser
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UsersView, basename="users")

urlpatterns = [
    path('change/password/', PasswordChangeRequestView.as_view()),
    path('change/password/confirm/<str:token>/', PasswordChangeConfirmView.as_view()),
    path('create-user', CreateUser.as_view()),
    path('create-user/confirmation/<str:token>/', CreateUserConfirmation.as_view()),
    path('denunciate/', Complaint.as_view()),
    path('get-authenticated-user/', GetAuthenticatedUser.as_view())
]

urlpatterns += router.urls
