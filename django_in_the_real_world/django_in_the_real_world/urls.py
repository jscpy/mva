from django.conf.urls import url
from django.contrib import admin

from mva.views import (Index, SessionCreateView, SessionListView, SessionDetailView, 
SessionDeleteView, SessionUpdateView )
from mva import views
from mva import auth

urlpatterns = [
    url(
    	regex = r'^admin/', 
    	view = admin.site.urls
    ),
    url(
        regex = r'^register/', 
        view = auth.RegisterForm.as_view(),
        name = 'register'
    ),
    url(
        regex = r'^success/submit/', 
        view = auth.UserSubmit.as_view(),
        name = 'success'
    ),
    url(
        regex = r'^login/', 
        view = auth.login,
        name = 'login'
    ),
    url(
        regex = r'^logout/', 
        view = auth.logout,
        name = 'logout'
    ),
    url(
        regex = r'^$', 
        view = Index.as_view(),
        name = 'home'
    ),
    url(
    	regex = r'^sessions/$', 
    	view = SessionListView.as_view(), 
    	name = 'session_list'
    ),
    url(
    	regex = r'^sessions/(?P<pk>[0-9]+)/$', 
    	view = SessionDetailView.as_view(),
    	name='session_detail'
    ),
    url(
    	regex = r'^sessions/create/$', 
    	view = SessionCreateView.as_view(),
    	name='session_create'
    ),
    url(
    	regex = r'^sessions/update/(?P<pk>[0-9]+)/$', 
    	view = SessionUpdateView.as_view(),
    	name='session_update'
    ),
    url(
    	regex = r'^sessions/delete/(?P<pk>[0-9]+)/$', 
    	view = SessionDeleteView.as_view(),
    	name='session_delete'
    ),
]