from django.db import models

class userInfo (models.Model):
	first_name = models.CharField(max_length=150)
	last_name = models.CharField(max_length=150)
	age = models.IntegerField(blank = True)
	address = models.TextField()
	birth_date = models.DateField()

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name

