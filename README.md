Mood Sensing App


![alt text](https://docs.aws.amazon.com/rekognition/latest/dg/images/sample-detect-faces.png)
A back-end implementation for facial emotion sensing using AWS Rekognition REST API. This project is based on Django REST framework and has three main functions:

1) Upload a mood capture for a given user and location (POST request to http://localhost/api/Mood/ you must include
 your user credentials, Latitud, Longitud, Photo (imageFLocalFile) it will be record the timestap and 
 consume AWS Rekognition service to determine your facial emotion)
2) Return the mood frequency distribution for a given user (GET request to http://localhost/api/Mood/ with your user credentials to verify your mood stats. Also you can use http://localhost/api/stats/?userid= to know other user stats for which you need admin access.)
3) Return the proximity to locations (home, office, shopping center,…) where a given user is happy. (Using the http://localhost/api/happyplaces/?userid= GET request)

## Getting Started 
pip install requirements.txt 
python manage.py runserver 80



These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
In order to use and keep safe your credentials
You need to set the follow OS enviromental Variables:
https://docs.aws.amazon.com/rekognition/latest/dg/faces.html
NAME:AWS_ACCESS_KEY_ID
VALUE:YOUR AWS KEY ID  with the Rekognition EXEC ROLLS
NAME: AWS_SECRET_ACCESS_KEY 
VALUE:YOU SECRET KEY


NAME:GEOPOSITION_GOOGLE_MAPS_API_KEY
VALUE:GOOGLE MAPS APY  KEY
Check detals:

https://developers.google.com/maps/documentation/javascript/get-api-key

Additional HELP TO SET UP OS ENV VARS:
linux https://www.cyberciti.biz/faq/set-environment-variable-linux/
Windos https://docs.microsoft.com/en-us/windows/desktop/ProcThread/environment-variables

python and pip installation.

### Installing

pip install requirements.txt 
python manage.py runserver 80


you can access to the admin page 
localhost/admin
user name:admin
password:Welcome1


## Running the tests


### Break down into end to end tests


### And coding style tests

python manage.py test.py

## Deployment

Add additional notes about how to deploy this on a live system

This is a beta version, if you want test how ir works in a live system, please change the DEBUG = True to False
and put this as 

## Built With

boto3==1.9.6
botocore==1.12.6
Django==2.1.1
Django-Accounts==0.1
django-crispy-forms==1.7.2
django-geoposition==0.3.0
djangorestframework==3.8.2
docutils==0.14
jmespath==0.9.3
Pillow==5.2.0
python-dateutil==2.7.3
pytz==2018.5
s3transfer==0.1.13
six==1.11.0
urllib3==1.23



## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

Adan Rosales
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

To the Tiempo Development TEAM, this is a good test!!
