from django.db import models

# Create your models here.
# menu category
# menu


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    menu_item = models.CharField(max_length=200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(
        MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")


class Customer(models.Model):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self):
        return self.name
