from django.db import models
from account.models import User
from django.utils import timezone
from django.urls import reverse



class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(status='p')


class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category', args=[self.slug])


class Post(models.Model):
    STATUS_CHOICES = (
        ('d','draft'),
        ('p','published'),
        ('i','investigate'),
        ('r','reject'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    objects = models.Manager()
    published = PublishManager()


    def get_absolute_url(self):
        return reverse('blog:post_detial', args=[self.slug])
