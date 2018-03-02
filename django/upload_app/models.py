from django.db import models
from django.urls import reverse

# Create your models here.
class ReportFile(models.Model):
	id = models.CharField(max_length=255,primary_key=True)
	file_size = models.IntegerField()
	magic = models.CharField(max_length=255)
	sha1 = models.CharField(max_length=255)
	sha256 = models.CharField(max_length=255)
	ssdeep = models.CharField(max_length=255)
	detected = models.CharField(max_length=255)
	result = models.CharField(max_length=255)
	uploaded_date = models.DateTimeField(auto_now_add=True)

#	def get_absolute_url(self):
#		url = reverse('report-detail',kwargs={'pk':self.pk})
#		return url

class UploadFile(models.Model):
	id = models.CharField(max_length=255,primary_key=True)
	upload_file = models.FileField()

	#def get_absolute_url(self):
		#url = reverse('report-detail',kwargs={'pk':self.pk})
		#return url

class UploadFileMeta(models.Model):
	id = models.CharField(max_length=255,primary_key=True)
	ssdeep = models.CharField(max_length=255)

