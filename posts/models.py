from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse

User = get_user_model()

# POST MANAGER
class PostManager(models.Manager):
  def get_posts(self, *args, **kwargs):
    return self.all()

  def get_post(self, post_id, *args, **kwargs):
    return get_object_or_404(self, id=post_id)

  def get_user_posts(self, owner, *args, **kwargs):
    return self.filter(owner=owner)

  def get_user_post(self, post_id, user, *args, **kwargs):
    return get_object_or_404(self, pk=post_id, owner=user)


# POST MODEL
class Post(models.Model):
  descriptions = models.CharField(max_length=150,blank=False,null=True)
  documents = models.FileField(upload_to='documents/',blank=False,null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
    User,
    default=1,
    on_delete=models.CASCADE,
    null=True
  )

  objects = PostManager()

  def __str__(self, *args, **kwargs):
    return self.descriptions
  
  def get_absolute_url(self, *args, **kwargs):
    return reverse('posts:posts-detail', kwargs={'id': self.pk})
  
  def get_delete_url(self, *args, **kwargs):
    return reverse('posts:posts-delete', kwargs={'id': self.pk})

  def get_update_url(self, *args, **kwargs):
    return reverse('posts:posts-update', kwargs={'id': self.pk})