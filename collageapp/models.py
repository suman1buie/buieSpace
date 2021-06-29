from django.db import models
from django.contrib.auth.models import User



class Catagory(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

 
class Trade(models.Model):
    dep = models.CharField(max_length=30)
    def __str__(self):
        return self.dep


class Year(models.Model):
    year = models.CharField(max_length=40)
    def __str__(self):
        return self.year


class Semester(models.Model):
    sem = models.CharField(max_length=50)
    def __str__(self):
        return self.sem



class Subject(models.Model):
    name = models.CharField(max_length=50)
    subjectcode = models.CharField(max_length=20,null=True,blank=True)
    def __str__(self):
        return self.name


class Sellybus(models.Model):
    subject = models.ForeignKey(to=Subject,on_delete = models.CASCADE,null=True,blank=True)
    sellybus = models.FileField(upload_to='files/')
    
    def __str__(self):
        return str(self.subject)



class Question(models.Model):
    subject = models.ForeignKey(to=Subject,on_delete = models.CASCADE,null=True,blank=True)
    question = models.FileField(upload_to='files/')
    year = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return str(self.subject)
    

class Metarial(models.Model):
    subject = models.ForeignKey(to=Subject,on_delete = models.CASCADE,null=True,blank=True)
    notes = models.FileField(upload_to='files/')
    chapter = models.CharField(max_length=100,blank=True,null=True)
    def __str__(self):
        return str(self.subject)
    

class Study(models.Model):
    sem = models.ForeignKey(to=Semester,on_delete = models.CASCADE,null=True,blank=True)
    year = models.ForeignKey(to=Year,on_delete=models.CASCADE,null=True,blank=True)
    department = models.ForeignKey(to=Trade,on_delete = models.CASCADE,null=True,blank=True)
    subject = models.ForeignKey(to=Subject,on_delete = models.CASCADE,null=True,blank=True)
    paperCode = models.CharField(max_length=40,null=True,blank=True)
    creditPoint = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return str(self.subject)



class Academic(models.Model):
    catagory = models.ForeignKey(to=Catagory,on_delete = models.CASCADE,null=True,blank=True)
    sem = models.ForeignKey(to=Semester,on_delete = models.CASCADE,null=True,blank=True)
    year = models.ForeignKey(to=Year,on_delete=models.CASCADE,null=True,blank=True)
    department = models.ForeignKey(to=Trade,on_delete = models.CASCADE,null=True,blank=True)
    descriptions = models.CharField(max_length=200,null=True,blank=True)
    file = models.FileField(upload_to='files/')
    cr_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return str(self.catagory)   


class Atrical(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    uploded_by = models.ForeignKey(to=User,on_delete=models.CASCADE,blank=True,null=True)
    cr_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    image = models.ImageField(upload_to="images//",blank=True,null=True)
    def __str__(self):
        return self.title

    

class UserProfile(models.Model):
    user = models.OneToOneField(to = User,on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 30,null=True,blank=True)
    last_name = models.CharField(max_length = 30,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    profile_pic = models.ImageField(upload_to = 'profileImage//',null=True,blank=True)
    socal_link = models.CharField(max_length=100,null=True,blank=True)
    ph_no = models.CharField(max_length=10,null=True,blank=True)
    department = models.CharField(max_length=50,null=True,blank=True)
    roll = models.IntegerField(null=True,blank=True)
    passoutyr = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
