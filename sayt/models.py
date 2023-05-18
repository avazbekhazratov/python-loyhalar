from django.db import models
from sayt.auth_models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128)
    is_menu = models.BooleanField()

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=256)
    short_desc = models.TextField()
    desc = models.TextField()
    img = models.ImageField()
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    view = models.IntegerField(default=0)
    ctg = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.view = View.objects.filter(new_id=self.id).count()

        return super(News, self).save(*args, **kwargs)


class Contact(models.Model):
    ism = models.CharField(max_length=125)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    is_trash = models.BooleanField(default=False)
    is_view = models.BooleanField(default=False)
    contacted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.ism} |   Trash: {self.is_trash} |   Viewed | {self.is_view} |   Contacted | {self.contacted}'


class View(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    new = models.ForeignKey(News, on_delete=models.CASCADE, related_name="new_view")

    # class Meta:


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    new = models.ForeignKey(News, on_delete=models.CASCADE)
    trash = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.trash} | {self.comment}"






