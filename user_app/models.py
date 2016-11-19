from django.db import models

class userInfo (models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	age = models.IntegerField(blank = True, default = 29)
	address = models.TextField(blank= True)
	birth_date = models.DateField(blank = True)

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

