from django.db import models

# Create your models here.
class Bahagian(models.Model):


	BUOrgChart = models.IntegerField('BUOrgChart',unique = True,blank=False,null=False)
	NamaBahagian = models.CharField('Nama Bahagian',max_length=60,blank=False,null=False)


	def __str__(self):
		return str(self.BUOrgChart)
		# return self.NamaBahagian
