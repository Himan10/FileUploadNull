from django.urls import path, include
from django.conf.urls.static import static
from helloAPI.views import JobViewSets, PersonViewSets
from rest_framework import routers

# create a router
router = routers.DefaultRouter()
router.register(r'jobs', JobViewSets)
router.register(r'person', PersonViewSets)
print(router.urls)

urlpatterns = [
    path('', include(router.urls), name="Default")
]