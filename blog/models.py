# Zhanbo Yang, zyang710@bu.edu, 

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    '''Encapsulate the idea of one Article by some author.'''

    # every Article has one User:
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # data attributes of an Article:
    title = models.TextField(blank=False)  # non-optional, blank=Flase
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    # image_url = models.URLField(blank=True) ## url as a string
    image_file = models.ImageField(blank=True) # an actual image

    # 10/8 new method:
    def get_comments(self):
        '''Return all of the comments about this article.'''

        comments = Comment.objects.filter(article=self)
        return comments

    def __str__(self):
        '''Return a string representation of this object.'''

        return f'{self.title} by {self.author}'

    # 10/17
    def get_absolute_url(self):
        '''Reutrn the URL that will display an instance of this object.'''
        # self.pk is the primary key to this Article instance
        return reverse('article', kwargs={'pk': self.pk})
    

## new 10/8
class Comment(models.Model):
    '''Encapsulate the idea of a Comment on an Article.'''

    # data attributes of a Comment:
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''Return a string representation of this Comment Object.'''
        return f'{self.text}'