from rest_framework.routers import DefaultRouter
from django.urls import path,include
from Tracker.api.urls import post_router

router = DefaultRouter()
#posts
router.registry.extend(post_router.registry)

urlpatterns = [
    path('', include(router.urls))
]

