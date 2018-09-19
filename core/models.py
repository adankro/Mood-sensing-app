from django.contrib.auth.models import User
#from geoposition.fields import GeopositionField


from django.db import models

class UserProfile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE,)
    photo = models.ImageField()
    adress1 = models.CharField(max_length=35)
    adress2 = models.CharField(max_length=35)
    selfdescription = models.TextField()
    def __str__(self):
    	return str(self.user)

class Mood(models.Model):
	user =models.ForeignKey(User, on_delete=models.CASCADE,)
	timestamp=models.DateTimeField(auto_now=True)
	photo = models.ImageField('images/')
	#location=GeopositionField()
	latitude=models.DecimalField(max_digits=25,decimal_places=6)
	longitude=models.DecimalField(max_digits=25,decimal_places=6)
	mood=models.CharField(max_length=15,null=True,blank=True,default="")
	def __str__(self):
		return str(self.user) + " " + str(self.timestamp) + " " + str(self.mood )


