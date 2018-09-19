from rest_framework import generics
from .models import Mood
from .serializers import MoodSerializer
import urllib.request,base64,boto3,os,random,functools, json
from django.http import HttpResponse 


class MoodView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    #queryset = Mood.objects.all()
    #serializer_class = MoodSerializer
    def get(self,request):
        mod=Mood.objects.all()
        serializer=MoodSerializer(mod,many=True)
        return Response(serializer.data)

    def post(self,request):

    	return HttpResponse(status=201)

def HappyPlacesView(request,user_id):
		jsonData=""
		usermoods=Mood.objects.filter(user=user_id,mood='HAPPY')
		#types='HOME+OFFICE+SHOP+CINEMA+SPOORTS+CAFETERIA+TRABAJO'
		types=["HOME", "travel_agency", "restaurant", "food", "establishment" ]
		for usermod in usermoods:
			print("Entra a Loop")
			radius='200' + '@' + 'usermod.latitude,' + 'usermod.longitude'
			jsonData+=GoogPlac(usermod.latitude,usermod.longitude,radius,types)
		return HttpResponse(json.dumps(jsonData))


def GoogPlac(lat,lng,radius,types):
		AUTH_KEY = os.environ.get('GEOPOSITION_GOOGLE_MAPS_API_KEY')
		LOCATION = str(lat) + "," + str(lng)
		RADIUS = radius
		TYPES = types
		MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
			'?location=%s'
			'&radius=%s'
			'&types=%s'
			'&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
		response = urllib.request.urlopen(MyUrl)
		jsonRaw = response.read()
		jsonData = json.loads(jsonRaw)
		return jsonDat

def stats(request,userID):

		usermoods=Mood.objects.filter(user=userID)
		moodsstats=[0,0,0,0,0]

		for mymood in usermoods:
			print(str(mymood))
			if mymood.mood=="SAD":
				moodsstats[0]+= 1
			elif mymood.mood=="HAPPY":
				moodsstats[1]+= 1	
			elif mymood.mood=="CALM":
				moodsstats[2]+=1
			else:
				moodsstats[3]+=1

		moodfrec={'SAD':moodsstats[0],'HAPPY':moodsstats[1],'CALM':moodsstats[2],'OTHER':moodsstats[3]}
		print(moodfrec)
		return HttpResponse(json.dumps(moodfrec))


