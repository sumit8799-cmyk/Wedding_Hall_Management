from django.db import models

# Create your models here.
#_--__----__----_---__---___-----__----___---___---___---___---_____---___--____---___---__------___-----____------

# (ADMIN TABLE CREATES )

class Admin (models.Model):
     """admin/Admin information"""
     emailAddress = models.EmailField(max_length=175, unique=True)
     password = models.CharField(max_length=175)
     hallName = models.CharField(max_length=175)
     adminName = models.CharField(max_length=175)
     mobileNumber = models.CharField(max_length=175)
     image = models.ImageField(max_length=175, blank=True, null=True)

     class Meta:
          db_table = 'admin' 

     def __str__(self):
        return f"{self.adminName} - {self.hallName}"
     
#_--__----__----_---__---___-----__----___---___---___---___---_____---___--____---___---__------___-----____------
#USER TABLE CREATE

class User (models.Model):
    """user/user information"""
    userName = models.CharField(max_length=175)
    emailAddress = models.EmailField(max_length=175)
    mobileNumber = models.CharField(max_length=175)
    homeAddress = models.TextField(max_length=175)
    subject = models.TextField(max_length=175)
    status = models.CharField(max_length=175, default='Registered')
    reason = models.TextField(max_length=255, null=True)

    class Meta:
        db_table = 'User'

    def __str__(self):
         return f"{self.userName} - {self.emailAddress} - {self.mobileNumber} - {self.homeAddress} - {self.subject}"


#_--__----__----_---__---___-----__----___---___---___---___---_____---___--____---___---__------___-----____------

class HomePage (models.Model):
    """HomePage/user information"""
    logo = models.ImageField(max_length=175, null=True, upload_to='homepage/')
    image = models.ImageField(max_length=175, null=True, upload_to='homepage/')
    heading = models.CharField(max_length=175)
    description = models.TextField(max_length=175)
    secondHeading = models.CharField(max_length=175)
    secondDescription = models.TextField(max_length=175)
    thirdHeading = models.CharField(max_length=175)
    thirdDescription = models.TextField(max_length=175) 

    class Meta:
        db_table = 'HomePage'
    def __str__(self):
         return super().__str__()

#_--__----__----_---__---___-----__----___---___---___---___---_____---___--____---___---__------___-----____------

class AboutPage (models.Model):
    """AboutPage/about information"""
    BackgroundImage = models.ImageField(max_length=175, null=True, upload_to='about/')
    FirstImage = models.ImageField(max_length=175, null=True, upload_to='about/')
    Heading = models.CharField(max_length=175)
    Description = models.TextField(max_length=175)
    SecondImage = models.ImageField(max_length=175, null=True, upload_to='about/')

    class Meta:
        db_table = 'AboutPage'

    def __str__(self):
        return super().__str__()

#_--__----__----_---__---___-----__----___---___---___---___---_____---___--____---___---__------___-----____------

class GalleryPage (models.Model):
    """GalleryPage/gallery information """
    BackgroundImage = models.ImageField(max_length=175, null=True, upload_to='gallery/')
    oneImage = models.ImageField(max_length=175, null=True, upload_to='gallery/')
    secondImage = models.ImageField(max_length=175, null=True, upload_to='gallery/')
    thirdImage = models.ImageField(max_length=175, null=True, upload_to='gallery/')
    fourthImage = models.ImageField(max_length=175, null=True, upload_to='gallery/')

    class Meta:
        db_table = 'GalleryPage'
    def __str__(self):
        return super().__str__()
    
#_--__----__----_---__---___-----__----___---___---___---___---_____---___--____---___---__------___-----____------

class CounterSection (models.Model):
    """CounterSection/ counter information"""
    NumberOfWedding = models.CharField(max_length=175)
    NumberOfBirthday = models.CharField(max_length=175)
    NumberOfFerewell = models.CharField(max_length=175)
    NumberOfSeminar = models.CharField(max_length=175)

    class Meta:
        db_table = 'CounterSection'

    def __str__(self):
        return super().__str__()

#_--__----__----_---__---___-----__----___---___---___---___---_____---___--____---___---__------___-----____------

class Contact (models.Model):
    """ContactPage/ conatact Information"""
    BackgroundImage = models.ImageField(max_length=175, null=True)
    Address = models.TextField(max_length=175)
    MobeliNumbar = models.CharField(max_length=175)
    EmailAddress = models.EmailField(max_length=175)

    class Meta:
        db_table = 'ContactPage'

    def __str__(self):
        return super().__str__()

#_--__----__----_---__---___-----__----___---___---___---___---_____---___--____---___---__------___-----____------
