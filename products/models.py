from django.db import models


#Size choicces
SIZE_CHOICES= (
    ('m','M'),
    ('sm','SM'),
    ('l','L'),
    ('xl','XL'),
    ('xxl','XXL'),
)
# Choice for Gender
GENDER = (
    ('M','M'),
    ('F','F')
)

#Category of Item
Categories_Choices = (
    ('Mens','Mens'),
    ('womens','womens'),
    ('kids','kids'),


)
#product type
Product_type = (
    ('shirt','shirt'),
    ('t-shirt','t-shirt'),
    ('jeans','jeans'),
    ('trousers','trousers'),
)
class Clothing(models.Model):
    brand_name  = models.CharField(max_length=100)
    brand_title = models.CharField(max_length=100)
    item_details = models.TextField(max_length=1000)
    product = models.ImageField(upload_to='products/%y/%m/%d/',blank=True)
    size = models.CharField(max_length=20, choices= SIZE_CHOICES , default='m')
    gender = models.CharField(max_length=20, choices= GENDER , default='M')
    category = models.CharField(max_length=20, choices= Categories_Choices , default='Male')
    product_type = models.CharField(max_length=20, choices= Product_type , default='shirt')
    price = models.FloatField()
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.brand_name

#Size choicces
foot_size= (
    ('uk-5','uk-5'),
    ('uk-6','uk-6'),
    ('uk-7','uk-7'),
    ('uk-8','uk-8'),
    ('uk-9','uk-9'),
    ('uk-10','uk-10'),
    ('uk-11','uk-11'),

)

#product type
footwear_type = (
    ('formal','formal'),
    ('sports','sports'),
    ('casual','casual'),
    ('sandal','sandal'),
    ('sleeper','sleeper'),

)
class Footwear(models.Model):
    brand_name  = models.CharField(max_length=100)
    brand_title = models.CharField(max_length=100)
    item_details = models.TextField(max_length=1000)
    product = models.ImageField(upload_to='footwear/%y/%m/%d/',blank=True)
    size = models.CharField(max_length=20, choices= foot_size , default='m')
    gender = models.CharField(max_length=20, choices= GENDER , default='M')
    category = models.CharField(max_length=20, choices= Categories_Choices , default='Male')
    product_type = models.CharField(max_length=20, choices= footwear_type , default='shirt')
    price = models.FloatField()
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.brand_name
