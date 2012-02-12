from django.db import models

from mfdemo.lib.globals import (MEDIUM_LEN, SMALL_LEN, TINY_LEN,
                                DECIMAL_DIGITS, DECIMAL_PLACES) 


class Location(models.Model):
    """A standard location"""
    city = models.CharField(max_length=SMALL_LEN)
    country = models.CharField(max_length=SMALL_LEN)
    latitude = models.DecimalField(max_digits=DECIMAL_DIGITS, 
                                   decimal_places=DECIMAL_PLACES)
    latitude = models.DecimalField(max_digits=DECIMAL_DIGITS, 
                                   decimal_places=DECIMAL_PLACES)
    street = models.CharField(max_length=MEDIUM_LEN)
    zipcode = models.CharField(max_length=SMALL_LEN)
    
    def __unicode__(self):
        return "%s" %self.city


class Category(models.Model):
    """Each organization belongs to one or more category"""
    name = models.CharField(max_length=MEDIUM_LEN)

    def __unicode__(self):
        return "%s" %self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Organization(models.Model):
    """An organization"""
    name = models.CharField(max_length=MEDIUM_LEN)
    category = models.ManyToManyField(Category)
    website = models.URLField(blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    phone = models.CharField(max_length=TINY_LEN)
    description = models.CharField(max_length=MEDIUM_LEN)
    
    def __unicode__(self):
        return "%s" %self.name

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    