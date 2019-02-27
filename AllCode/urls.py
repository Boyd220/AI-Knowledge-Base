from django.conf.urls import url
from AllCode import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
     url(r'^ajax/search_all_data/$', views.search_all_data, name='search_all_data'),
     url(r'^ajax/get_action/$', views.get_action, name='get_action'),
     url(r'^ajax/post_feedback/$', views.post_feedback, name='post_feedback')
]