from django.urls import path
from member_app import views

app_name = 'member_app'


urlpatterns = [
    path('', views.home, name='home'),
    path('member', views.MemberListView.as_view()),
]