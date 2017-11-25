from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.



def upload_location(instance,filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return "%s/%s" %(instance.user.username,filename)


# Create your models here.
class properties(models.Model):
	title = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	description = models.TextField(max_length=5000)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to=upload_location,null = True, blank = False)
	bathroom = models.IntegerField()
	room = models.IntegerField()
	created_date = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-created_date"]
