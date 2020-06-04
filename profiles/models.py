from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.urls import reverse
from datetime import datetime

User  = get_user_model()


GENDER_CHOICES = [
  ('Male', 'Male'),
  ('Female', 'Female')
]



PROFESSION_CHOICES = [
  ('Student or Learning', 'Student or Learning'),
  ('Instructor or Teacher', 'Instructor or Teacher'),
  ('Other', 'Other')
]

DEGREE_CHOICES = [
  ('IT', 'Information Technologies'),
  ('Bussiness Managment', 'Bussiness Managment'),
  ('Digital Marketing', 'Digital Marketing'),
  ('Computer Science', 'Computer Science'),
  ('Civil Engineering', 'Civil Engineering'),
  ('AI', 'Artificial & Inteligence'),
  ('Other', 'Other')
]

# PROFILE MODEL MANAGER
class ProfileManager(models.Manager):
  def get_auth_profile(self, profile, user, *args, **kwargs):
    return get_object_or_404(self, pk=profile, user=user)

  def check_auth_profile(self, user, *args, **kwargs):
    try:
      obj = self.get(user=user)
      if obj:
        return obj
    except Profile.DoesNotExist:
      return None
    

# PROFILE MODEL
class Profile(models.Model):
  user = models.OneToOneField(
    User,
    default=1,
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=100)
  contact_number = models.CharField(max_length=15,unique=True)
  gender = models.CharField(
    max_length=5,
    default=1,
    choices=GENDER_CHOICES
  )
  linkedin = models.URLField(max_length=283, blank=True, null=True)
  # company = models.CharField(max_length=120)
  profession = models.CharField(
    max_length=120,
    default='Web Developer',
    choices=PROFESSION_CHOICES
  )
  country = models.CharField(max_length=100)
  skills = models.CharField(max_length=300, choices=None)
  image = models.ImageField(
    upload_to='profiles/',
    blank=True,
    default='media/profiles/default-user.jpg'
  )
  created_at = models.DateTimeField(auto_now_add=True)

  objects = ProfileManager()
  @property
  def get_photo_url(self):
    if self.image and hasattr(self.image, 'url'):
      return self.image.url
    else:
      return "/media/profiles/"


  def __str__(self, *args, **kwargs):
    return self.name

  def get_absolute_url(self, *args, **kwargs):
    return reverse('profiles:profiles-detail', kwargs={'id':self.pk})

  def get_create_url(self, *args, **kwargs):
    return reverse('profiles:profiles-create')
  
  def get_update_url(self, *args, **kwargs):
    return reverse('profiles:profiles-update', kwargs={'id':self.pk})

  def get_delete_url(self, *args, **kwargs):
    return reverse('profiles:profiles-delete', kwargs={'id':self.pk})

  def get_education_url(self, *args, **kwargs):
    return reverse('profiles:educations-list', kwargs={'id':self.pk})

  def get_experience_url(self, *args, **kwargs):
    return reverse('profiles:experiences-list', kwargs={'id':self.pk})

  def get_education_create_url(self, *args, **kwargs):
    return reverse('profiles:educations-create', kwargs={'id':self.pk})
  
  def get_experience_create_url(self, *args, **kwargs):
    return reverse('profiles:experiences-create', kwargs={'id':self.pk})
  

# EDUCATION MODEL MANAGER
class EducationManager(models.Manager):
  def get_profile_education(self, profile, education):
    return get_object_or_404(Education, profile=profile, pk=education)


# EDUCATION MODEL
class Education(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
  college = models.CharField(max_length=120, default='Info Tech', null=True)
  degree = models.CharField(
    max_length=120,
     default=1,
    choices=DEGREE_CHOICES
  )
  started_at = models.CharField(max_length=4, null=True)
  ended_at = models.CharField(max_length=4, null=True)
  bio = models.TextField(blank=True, default='Hello buddies..!')
  is_currently_studying = models.BooleanField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)

  objects = EducationManager()

  def __str__(self):
    return self.profile.name

  def get_absolute_url(self, *args, **kwargs):
    return reverse(
      'profiles:educations-detail',
      kwargs={'profile_id': self.profile.pk, 'education_id': self.pk}
    )

  def get_update_url(self, *args, **kwargs):
    return reverse(
      'profiles:educations-update',
      kwargs={'profile_id': self.profile.pk, 'education_id': self.pk}
    )

  def get_delete_url(self, *args, **kwargs):
    return reverse(
      'profiles:educations-delete',
      kwargs={'profile_id': self.profile.pk, 'education_id': self.pk}
    )


# EXPERIENCES MODEL MANAGER
class ExperienceManager(models.Manager):
  def get_profile_experience(self, profile, experience):
    return get_object_or_404(Experience, profile=profile, pk=experience)


# EXPERIENCES MODEL
class Experience(models.Model):
  profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
  college = models.CharField(max_length=120, default='IFS', null=True)
  profession = models.CharField(
    max_length=120,
    default=1,
    choices=PROFESSION_CHOICES
  )
  research = models.TextField(blank=True,default='')
  is_currently_teacher = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True, null=True)

  objects = ExperienceManager()

  def __str__(self, *args, **kwargs):
    return self.profile.name

  def get_absolute_url(self, *args, **kwargs):
    return reverse(
      'profiles:experiences-detail',
      kwargs={'profile_id': self.profile.pk, 'experience_id': self.pk}
    )

  def get_update_url(self, *args, **kwargs):
    return reverse(
      'profiles:experiences-update',
      kwargs={'profile_id': self.profile.pk, 'experience_id': self.pk}
    )

  def get_delete_url(self, *args, **kwargs):
    return reverse(
      'profiles:experiences-delete',
      kwargs={'profile_id': self.profile.pk, 'experience_id': self.pk}
    )


