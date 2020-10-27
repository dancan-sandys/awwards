from django.test import TestCase
from .models import Rating, Profile,Project

class TestProfile(TestCase):

    def setUp(self):
        self.new_profile = Profile(name='Dancan', bio='Yes', Phone='0798940016', email='dancan@gmail.com')

    def tearDown(self):
        Profile.objects.all().delete()

    def testinstance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def testsaving(self):
        profiles = Profile.objects.all()
        self.new_profile.saveprofile()
        self.assertTrue(len(profiles)>0)


class TestProject(TestCase):

    def setUp(self):
        self.new_profile = Profile(name='Dancan', bio='Yes', Phone='0798940016', email='dancan@gmail.com')
        self.new_project = Project(Title = 'Yes', Description='No', User=self.new_profile)

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
    
    def testinstance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def testsaving(self):
        projects = Project.objects.all()
        self.new_profile.saveprofile()
        self.new_project.saveproject()
        self.assertTrue(len(projects)>0)

class TestProject(TestCase):

    def setUp(self):
        self.new_profile = Profile(name='Dancan', bio='Yes', Phone='0798940016', email='dancan@gmail.com')
        self.new_project = Project(Title = 'Yes', Description='No', User=self.new_profile)
        self.new_rate = Rating(Design=10, Usability=20, Content=0,Average=30, Rater=self.new_profile, project=self.new_project)
    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Rating.objects.all().delete()
    
    def testinstance(self):
        self.assertTrue(isinstance(self.new_rate, Rating))

    def testsaving(self):
        ratings = Rating.objects.all()
        self.new_profile.saveprofile()
        self.new_project.saveproject()
        self.new_rate.saverating()
        self.assertTrue(len(ratings)>0)


