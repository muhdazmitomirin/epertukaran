from django.db import models

# Create your models here.
class Bahagian(models.Model):

	BUOrgChart = models.IntegerField('BUOrgChart',unique = True,blank=False,null=False)
	NamaBahagian = models.CharField('Nama Bahagian',max_length=60,blank=False,null=False)

	def __str__(self):
		return str(self.BUOrgChart)

class Tatatertib(models.Model):

	NoKP = models.CharField('No KP',max_length=12,unique=True,blank=False,null=False)
	Catatan = models.CharField('Catatan',max_length=255,blank=False,null=False)
	Status = models.CharField('Status',max_length=60,blank=False,null=False)
	UserDaftar = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	TkhDaftar = models.DateTimeField('Created Date',auto_now_add=True)

	def __str__(self):
		return str(self.NoKP)