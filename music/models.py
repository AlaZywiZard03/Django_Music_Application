from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in seconds")
    
    def __str__(self):
        return f"{self.title} - {self.artist}"
        
    @property
    def duration_formatted(self):
        """Format duration as MM:SS"""
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{minutes}:{seconds:02d}"
