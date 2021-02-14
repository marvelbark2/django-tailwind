from django.db import models
import jsonfield
from django.contrib.auth.models import User


class BadHabbit(models.Model):
    
    title = models.CharField(max_length = 200)
    description = models.TextField()
    dangers = jsonfield.JSONField()

    class Meta:
        verbose_name_plural = "Bad Habbits"
        verbose_name = "Bad Habbit"

    def __str__(self):
        return self.title

class Subs(models.Model):
    
    title = models.CharField(max_length = 200)
    description = models.TextField()
    bad_id = models.ForeignKey(BadHabbit,on_delete=models.CASCADE)
    badget_min = models.IntegerField()
    badget_max = models.IntegerField()
    efficacite = models.IntegerField()
    duration = models.IntegerField()

    class Meta:
        verbose_name_plural = "Subscriptions"
        verbose_name = "Subscriptions"
    
    def __str__(self):
        return self.title

class Sub_detail(models.Model):
    subs_id = models.ForeignKey(Subs, on_delete=models.CASCADE)
    description = models.TextField()
    order = models.IntegerField()
    date_daily = models.IntegerField()

    class Meta:
        verbose_name_plural = "Subscription Details"
        verbose_name = "Subscription Detail"

    def __str__(self):
        return self.title


class Contrats(models.Model):
    subs_id = models.ForeignKey(Subs, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Contrats"
        verbose_name = "Contrat"

class Contrat_detail(models.Model):
    sub_id = models.ForeignKey(Sub_detail, on_delete=models.CASCADE)
    contrats_id = models.ForeignKey(Contrats, on_delete=models.CASCADE) 
    feedback = models.TextField()

    class Meta:
        verbose_name_plural = "Contrats details"
        verbose_name = "Contrats detail"

