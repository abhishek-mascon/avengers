# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Stocks(models.Model):
	symbol = models.CharField(max_length=200)
	series = models.CharField(max_length=200)
	open = models.FloatField()
	high = models.FloatField()
	low = models.FloatField()
	close = models.FloatField()
	last = models.FloatField()
	prev_close = models.FloatField()
	tottrdqty = models.FloatField()
	tottrdval = models.FloatField()
	timestamp = models.DateTimeField()
	total_trades = models.IntegerField()
	isin = models.CharField(max_length=200)
	

class nse_bhav_staging(models.Model):
	pass


class Portfolio(models.Model):
	stock = models.CharField(max_length=200)
	shares = models.IntegerField()
	notes = models.CharField(max_length=200)
	price = models.FloatField()
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	added_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self): 
		return self.stock

