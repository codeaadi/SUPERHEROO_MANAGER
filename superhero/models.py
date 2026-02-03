from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta


# Create your models here.
class SuperHeroType(models.Model):
    WORKING_LOCATION = [
        ("KLY", "KALYAN"),
        ("MUM", "MUMBAI"),
        ("THN", "THANE"),
        ("DDR", "DADAR"),
    ]
    name = models.CharField(max_length=150)
    power = models.CharField(max_length=150)
    joined_at = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=3,choices=WORKING_LOCATION)
    
    def __str__(self):
        return self.name
    
    
    

class HeroReview(models.Model):
    review_range=[
        ('1','Very poor'),
        ('2','Poor'),
        ('3','Avarage'),
        ('4','Satisfactory'),
        ('5','Good'),
    ]    
    hero=models.ForeignKey("SuperHeroType", on_delete=models.CASCADE, related_name ='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.CharField(max_length=4,choices=review_range)
    comment = models.TextField('')
    review_date= models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.hero.name}'
    
    
class heroBranch(models.Model):
    branch_name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    available_hero = models.ManyToManyField(SuperHeroType,related_name='hero_branch')
    
    
    def __str__(self):
        return self.branch_name
    
    
class hero_work_permit(models.Model):
    hero =models.OneToOneField(SuperHeroType,on_delete=models.CASCADE,related_name='workpermit')
    permit_number =models.CharField(max_length=50)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(blank=True,null=True)
    
    
    def save(self,*args,**kwargs):
        if not self.valid_until:
            self.valid_until = self.issue_date + timedelta(days=365*2)
           
        super().save(*args,**kwargs)
                    

    def __str__(self):
        return f'certificate for {self.hero.name}' 