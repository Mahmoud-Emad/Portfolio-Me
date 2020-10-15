from django.db import models
from django.utils.text import slugify



class TestMe(models.Model):
    Name = models.CharField(max_length=100,verbose_name="Name Of Tester")
    text = models.TextField(max_length=500,verbose_name="Code Of Issue")
    email = models.EmailField(max_length=254,verbose_name="Email Of Tester")
    slug = models.SlugField(blank=True,null=True,max_length=1000)
    def __str__(self):
        return self.Name + str(" < | > ") + str(self.email)
    def save(self,*args, **kwargs):
        y = self.Name
        x = int('100080000')
        f = str('40451')
        r = int(x) * int (f)
        self.slug = slugify(str(y)+ str(r))
        super(TestMe,self).save(*args, **kwargs)


choice_list = (
    ('Ecommerce','Ecommerce'),
    ('Job Board','Job Board'),
    ('Doctors community','Doctors community'),
    ('The city of moves','The city of moves'),

)

class ProjectsModel(models.Model):
    Name = models.CharField(max_length=100,verbose_name="Name Of Project")
    Image = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="Main Image")
    Image_Ditail = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="Top Image Ditail")
    Image2 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image Size 218 x 243")
    Image3 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image Size 218 x 243")
    Image4 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image Size 218 x 243")
    Image5 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image Size 218 x 243")
    Image6 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image Size 218 x 243")
    Image7 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image Size 218 x 243")
    Image8 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image Size 218 x 243")
    Image9 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image Size 218 x 243")
    Image10 = models.ImageField(max_length=1000,null=True ,blank=True,verbose_name="More Image Size 218 x 243")
    Discraption = models.TextField(max_length=600,verbose_name="Discraption Of Project")
    Category =  models.CharField(choices=choice_list,max_length=255)
    Live =  models.URLField(max_length=500, blank=True ,verbose_name="Live Of Project")
    slug = models.SlugField(null=True ,blank=True)

    def __str__(self):
        return self.Name + str(" < | > ") + str(self.Category)
    def save(self,*args, **kwargs):
        y = self.Name
        x = int('100080000')
        z = int('540')
        c = self.Category
        r = int(x) * int (z)
        self.slug = slugify(str("name-") +str(y) +str("-id-") + str(r) +str("-part-of") +str(c) )
        super(ProjectsModel,self).save(*args, **kwargs)



class Comments(models.Model):
    Name = models.CharField(max_length=200)
    Position = models.CharField(max_length=200,null=True ,blank=True)
    Comment = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.Name + '  |  ' + str(self.date) + ' | ' + self.Position 


class ContactModel(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=254)
    Message = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Name + '  |  '  + self.Email 