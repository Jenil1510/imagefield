from django.db import models
from django.utils.html import mark_safe

class Information(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    img=models.ImageField(upload_to="media/images/", blank=True, null=True)
    salary = models.IntegerField()
    
    def image_tag(self):
        return mark_safe('<img src="{{ img.img.url }}" width="100px" height="100px" />'%(self.img.url))
    image_tag.short_description = 'Image'
    
    class Meta:
        db_table = "Information"
        
    
