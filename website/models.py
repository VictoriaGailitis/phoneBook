from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
	user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	city =  models.CharField(max_length=50)
	photo = models.ImageField(upload_to="website/files/")

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")
