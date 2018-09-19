from rest_framework import viewsets
from .models import Mood
from .serializers import MoodSerializer
from django.http import HttpResponse 
from django.contrib.auth.models import User
import urllib.request,base64,boto3,os,random,functools, json
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response



class MoodViewSet(viewsets.ModelViewSet):

	queryset = Mood.objects.all()
	serializer_class = MoodSerializer
	"""This viewSET Return the mood frequency distribution for the auth User:
	"""

	def list(self,request):
		user=request.user
		usermoods=Mood.objects.filter(user=user)
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

	"""This View Attends the POST request to http://localhost/api/Mood/ you must to include
	Your user credentials, Latitud,Longitud,Photo(imageFLocalFile) it will be record the timestap and 
	consume aws rekognition service to determine your facial emotion
	"""
	def create(self, request):

		print("User: " + str(request.user) )
		print("Latitude: " + str(request.POST.get('latitude')))
		print("Longitude: " + str(request.POST.get('longitude')))
		print("Photo: " + str(request.data['photo']))

		mymood=Mood.objects.create(
			user=request.user, 
			photo=request.data['photo'], 
			latitude=request.POST.get('latitude'),
			longitude=request.POST.get('longitude'),
			mood=None,
			)

		mood=self.moodrecon(mymood)
		mymood.mood=mood
		mymood.save()
		return HttpResponse(status=201)

	def moodrecon(self,Mood):

		"""AWS rekognition service Implementation
		#and determine emotion
		#aws_access_key = os.environ.get('AWS_ACCESS_KEY_ID')
		#aws_secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
		#client=boto3.client('rekognition',
		#	region_name='us-east-2', 
		#	aws_access_key_id=aws_access_key, 
		#	aws_secret_access_key=aws_secret_key)
		#with open(Mood.photo.path, 'rb') as image:
			#issues with encode image to bytes
			#Type: Base64-encoded binary data object
			#https://docs.python.org/3/library/base64.html
			#source_bytes = base64.b64encode(image.read())
			#response = client.detect_labels(Image={'Bytes':image})
		#emotions=respose['Emotions']
		"""

		agry_random=random.uniform(0, 100)
		confused_random=random.uniform(0, 100)
		calm_random=random.uniform(0, 100)
		emotions= [
		{"Type": "HAPPY","Confidence": agry_random},
		{"Type": "SAD","Confidence": confused_random},
		{"Type": "CALM","Confidence": calm_random}]

		emotionsL=[(emotions[0]['Type'],emotions[0]['Confidence']),
		(emotions[1]['Type'],emotions[1]['Confidence']),
		(emotions[2]['Type'],emotions[2]['Confidence'])]
		mood=max(emotionsL,key=lambda item:item[1])
		print('mood: ' + mood[0])
		print('Timestamp: ' + str(Mood.timestamp))
		return mood[0]

class HappyPlacesViewSet(viewsets.ModelViewSet):
	queryset = Mood.objects.all()
	serializer_class = MoodSerializer

	def list(request,user_id):
		jsonData=""
		usermoods=Mood.objects.filter(user=user_id,mood='HAPPY')
		#types='HOME+OFFICE+SHOP+CINEMA+SPOORTS+CAFETERIA+TRABAJO'
		types=["HOME", "travel_agency", "restaurant", "food", "establishment" ]
		for usermod in usermoods:
			radius='200' + '@' + 'usermod.latitude,' + 'usermod.longitude'
			jsonData+=self.GoogPlac(usermod.latitude,usermod.longitude,radius,types)
		
		return HttpResponse(json.dumps(jsonData))


	def GoogPlac(self,lat,lng,radius,types):
		AUTH_KEY = os.environ.get('GEOPOSITION_GOOGLE_MAPS_API_KEY')
		LOCATION = str(lat) + "," + str(lng)
		RADIUS = radius
		TYPES = types
		MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
			'?location=%s'
			'&radius=%s'
			'&types=%s'
			'&sensor=false&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
		response = urllib.urlopen(MyUrl)
		jsonRaw = response.read()
		jsonData = json.loads(jsonRaw)
		return jsonDat


