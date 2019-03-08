from django.db import models

class Candidate(models.Model):
    first_name = models.CharField('名字', max_length=10)
    last_name = models.CharField('姓', max_length=10)
    age = models.PositiveIntegerField('年齡')
    politics = models.TextField('政見')
    vote = models.PositiveIntegerField('得票數')

    def __str__(self):
        return self.first_name
    
