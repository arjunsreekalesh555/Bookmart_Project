from django.db import models

# Create your models here.
class RSAuthor(models.Model):
    name=models.CharField(max_length=250, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class RSBook(models.Model):
    CATEGORY_CHOICES=[
        ('1','Real Story Book'),
        ('2','Fiction Book')
    ]
    GENRE_CHOICES=[
        ('1','Comedy'),
        ('2','Action'),
        ('3', 'Crime'),
        ('4', 'Horror'),
        ('5', 'Romance'),
        ('6', 'Thriller'),
        ('7', 'Adventure'),
        ('8', 'Sports'),
        ('9', 'Inspirational')
    ]
    title=models.CharField(max_length=250, null=True)
    description=models.TextField(null=True)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='rsbook_media')
    quantity=models.IntegerField()
    category=models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    genre=models.CharField(max_length=1, choices=GENRE_CHOICES)
    author=models.ForeignKey(RSAuthor, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return '{}'.format(self.title)
