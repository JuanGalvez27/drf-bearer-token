from django.db import models

class Poll(models.Model):
    question = models.CharField(verbose_name="Question", max_length=250, blank=True)

    class Meta:
            verbose_name = ("question")
            verbose_name_plural = ("question")

    def __str__(self):
        return self.question
    
    
class Choice(models.Model):
    question = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.CharField(verbose_name="Choice", max_length=250, blank=True)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice