from rest_framework import routers
from .views  import Handover2pmViewSet

router = routers.DefaultRouter()
router.register(r'winopp', Handover2pmViewSet)