from django.conf.urls import url

from mva import auth
from mva import views

urlpatterns = [
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
        view = auth.LoginView.as_view(),
        name = 'login'
    ),
    url(
        regex = r'^logout/', 
        view = auth.LogoutView.as_view(),
        name = 'logout'
    ),
    url(
        regex = r'^$', 
        view = views.Index.as_view(),
        name = 'home'
    ),
    url(
    	regex = r'^sessions/$', 
    	view = views.SessionListView.as_view(), 
    	name = 'session_list'
    ),
    url(
    	regex = r'^sessions/(?P<pk>[0-9]+)/$', 
    	view = views.SessionDetailView.as_view(),
    	name='session_detail'
    ),
    url(
    	regex = r'^sessions/create/$', 
    	view = views.SessionCreateView.as_view(),
    	name='session_create'
    ),
    url(
    	regex = r'^sessions/update/(?P<pk>[0-9]+)/$', 
    	view = views.SessionUpdateView.as_view(),
    	name='session_update'
    ),
    url(
    	regex = r'^sessions/delete/(?P<pk>[0-9]+)/$', 
    	view = views.SessionDeleteView.as_view(),
    	name='session_delete'
    ),
    url(
        regex = r'^speaker/(?P<pk>[0-9]+)/$', 
        view = views.SpeakerDetailView.as_view(), 
        name= 'speaker_detail'
    ),
    url(
        regex = r'^reservation/create/$',
        view = views.ReservationView.as_view(),
        name = 'reservation_create'
    ),
    url(
        regex = r'^reservations/$', 
        view = views.ReservationListView.as_view(),
        name = 'reservation_list'
    ),
    url(
        regex = r'^pases/create/$', 
        view = views.PasesView.as_view(),
        name = 'pases_create'
    ),
]

# url(
#     regex = r'^$', 
#     view = '',
#     name = None
# ),