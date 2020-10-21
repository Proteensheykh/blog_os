from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime

# Create your models here.

class Categories(models.TextChoices):
    
    BUSINESS = 'business'
    MANAGEMENT = 'management'
    TECHNOLOGY = 'technology'
    DESIGN = 'design'
    CULTURE = 'culture'

class BlogPost(models.Model):
    
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.CharField(max_length=50, choices=Categories.choices, default=Categories.BUSINESS)
    thumbnail = models.ImageField()
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=3)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now())

    def save(self, *args, **kwargs):

        slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()

        if(queryset):   #if slug exists append position number to new slug
            slug += '-'+str(queryset)
                
        self.slug = slug

        #ensure only one post is featured at a time
        if(self.featured):
            try:
                temp = BlogPost.objects.get(featured=True)

                if(self != temp):
                    temp.featured = False
                    temp.save()
            except BlogPost.DoesNotExist:
                pass
        
        super(BlogPost, self).save(*args, **kwargs)

    def  __str__(self):
        return self.title