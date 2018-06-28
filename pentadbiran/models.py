from django.db import models

# Create your models here.
class Bahagian(models.Model):

		nama = models.CharField('Nama Bahagian',max_length=100,unique=True,blank=False,null=False)
		createdby = models.ForeignKey('auth.User',on_delete=models.CASCADE)
		created_date = models.DateTimeField('Created Date',auto_now_add=True)
	
		def __str__(self):
			return self.nama
