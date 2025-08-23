from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class HarmfulIngredient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "HarmfulIngredient"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.email

class ScanResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='scan_results/')
    extracted_text = models.TextField()
    harmful_ingredients = models.ManyToManyField(HarmfulIngredient)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Scan result for {self.user.email} at {self.created_at}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
