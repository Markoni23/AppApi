from rest_framework import routers
from Base.api.viewsets import AppViewset


router = routers.DefaultRouter()
router.register("App", AppViewset)