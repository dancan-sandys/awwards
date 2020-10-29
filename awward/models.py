from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=80)
    profilepic = models.ImageField(upload_to = 'profiles/')
    bio = models.TextField()
    Phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    def saveprofile(self):
        self.save()

    def deleteprofile(self):
        self.delete()

    



class Project(models.Model):
    Title = models.CharField(max_length=30)
    Landing = models.ImageField(upload_to = 'landings/')
    Description = models.TextField()
    User = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def saveproject(self):
        self.save()

    def deleteproject(self):
        self.delete()
    
     

    
class Rating(models.Model):
    Design = models.IntegerField()
    Usability = models.IntegerField()
    Content = models.IntegerField()
    Average = models.IntegerField()
    Rater = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def saverating(self):
        self.save()

    