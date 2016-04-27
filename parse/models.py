from django.db import models

# Create your models here.
from django.db import models

# class article_list(models.Model):
#     title_text = models.CharField(max_length = 200)
#     pub_date = models.CharField(max_length= 50)
#     abstract = models.CharField(max_length=400)
#     link = models.CharField(max_length=400)


class article(models.Model):
    link = models.CharField(max_length=400)
    title =models.CharField(max_length=200)
    tips = models.CharField(max_length = 100)
    pub_date = models.CharField(max_length= 50)
    abstract = models.CharField(max_length=400)
    content = models.TextField
    def __str__(self):
        return self.title




