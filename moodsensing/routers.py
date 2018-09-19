from rest_framework import routers
from core.ViewSet import MoodViewSet
from core.views import HappyPlacesView

router = routers.DefaultRouter()
router.register(r'Mood', MoodViewSet)
#router.register(r'HappyPlacesView', HappyPlacesView)
