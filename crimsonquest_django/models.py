from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser):
    userID = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True, default='')
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.fullName
    



class Campus(models.Model):
    campusID = models.AutoField(primary_key=True)
    campusName = models.CharField(max_length=255)
    campusInfo = models.TextField()

    def __str__(self):
        return f"{self.campusName} ({self.campusID})"

class locationCategory(models.Model):
    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.categoryName} ({self.categoryID})"


class College(models.Model):
    collegeID = models.AutoField(primary_key=True)
    collegeName = models.CharField(max_length=255)
    collegeMap = models.ImageField(upload_to='college_images/', null=True, blank=True)
    collegePic1 = models.ImageField(upload_to='college_images/', null=True, blank=True)
    collegePic2 = models.ImageField(upload_to='college_images/', null=True, blank=True)
    collegePic3 = models.ImageField(upload_to='college_images/', null=True, blank=True)
    collegeInfo = models.TextField()
    campusID = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.collegeName} ({self.collegeID})"


class Facilities(models.Model):
    facilityID = models.AutoField(primary_key=True)
    facilityName = models.CharField(max_length=255)
    facilityMap = models.ImageField(upload_to='facility_images/', null=True, blank=True)
    facilityPic1 = models.ImageField(upload_to='facility_images/', null=True, blank=True)
    facilityPic2 = models.ImageField(upload_to='facility_images/', null=True, blank=True)
    facilityPic3 = models.ImageField(upload_to='facility_images/', null=True, blank=True)
    facilityInfo = models.TextField()
    campusID = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.facilityName} ({self.facilityID})"


class Highschool(models.Model):
    hsID = models.AutoField(primary_key=True)
    hsName = models.CharField(max_length=255)
    hsMap = models.ImageField(upload_to='highschool_images/', null=True, blank=True)
    hsPic1 = models.ImageField(upload_to='highschool_images/', null=True, blank=True)
    hsPic2 = models.ImageField(upload_to='highschool_images/', null=True, blank=True)
    hsPic3 = models.ImageField(upload_to='highschool_images/', null=True, blank=True)
    hsInfo = models.TextField()
    campusID = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.hsName} ({self.hsID})"


class Elementary(models.Model):
    elemID = models.AutoField(primary_key=True)
    elemName = models.CharField(max_length=255)
    elemMap = models.ImageField(upload_to='highschool_images/', null=True, blank=True)
    elemPic1 = models.ImageField(upload_to='highschool_images/', null=True, blank=True)
    elemPic2 = models.ImageField(upload_to='highschool_images/', null=True, blank=True)
    elemPic3 = models.ImageField(upload_to='highschool_images/', null=True, blank=True)
    elemInfo = models.TextField()
    campusID = models.ForeignKey(Campus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.elemName} ({self.elemID})"
    

class Course(models.Model):
    courseID = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=255)
    courseInfo = models.TextField()
    coursePic = models.ImageField(upload_to='highschool_images/', null=True, blank=True)
    collegeID = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.courseName} ({self.courseID})"
    

