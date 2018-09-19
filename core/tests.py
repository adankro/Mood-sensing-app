from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Mood
from .serializers import MoodSerializer
from django.contrib.auth.models import User

# tests for views
#TEST with admin user
user =User.objects.get(pk=1)

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_mood(user, photo,latitude,longitude):
        if user != "" and photo != "" and latitude !="" and longitude !="":
            Mood.objects.create(user=user, photo=photo, latitude=latitude,longitude=longitude)

    def setUp(self):
        # add test data
        self.create_mood(user, "https://ak6.picdn.net/shutterstock/videos/12192296/thumb/1.jpg","15.22","-150.2")
        self.create_mood(user, "https://ak6.picdn.net/shutterstock/videos/9993956/thumb/1.jpg","15.22","-180")
        self.create_mood(user, "https://ak6.picdn.net/shutterstock/videos/9993956/thumb/1.jpg","14.22","-180")
class GetAllMoodsTest(BaseViewTest):

    def test_get_all_moods(self):
        """
        This test ensures that all moods added in the setUp method
        exist when we make a GET request to the moods/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("Mood-all")
        )
        # fetch the data from db
        expected = Mood.objects.all()
        serialized = MoodSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)