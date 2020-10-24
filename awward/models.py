from django.db import models

# Create your models here.

class Profile(models.Model):
    profilepic = models.CharField(max_length=30)
    bio = models.TextField(max_length=500)
    Phone = models.IntegerField()
    email = models.EmailField(max_length=20)

    def saveprofile(self):
        self.save()

    def deleteprofile(self):
        self.delete()

    



class Project(models.Model):
    Title = models.CharField(max_length=30)
    Landing = models.CharField(max_length=30)
    Description = models.TextField(max_length=500)
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