from django.db import models
from users.models import Users
from django.contrib.auth.models import User



class Notifications(models.Model):
	user = models.ForeignKey(Users,on_delete=models.CASCADE)
	text = models.TextField()
	link = models.CharField(max_length=255)

class Comments(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	startup = models.ForeignKey('Startups', on_delete=models.CASCADE)
	text = models.TextField(blank=True, default='', null= True)
	date = models.DateTimeField(auto_now=True)

class Startups(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	startupStatus = models.ForeignKey('StartupStatuses', on_delete=models.CASCADE)

class StartupStatuses(models.Model):
	status = models.CharField(max_length=255)

class StartupFiles(models.Model):
	fileType = models.CharField(max_length=255)

class StartupReply(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	reply = models.ForeignKey('Comments', on_delete=models.CASCADE)
	text = models.TextField(blank=True,default='', null=True)
	date = models.DateTimeField(auto_now=True)

	
