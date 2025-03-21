from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.exceptions import ValidationError


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    ROLE_CHOICES = (
        ('Администратор', 'Administratot'),
        ('Продавец', 'Salesman'),
        ('Покупатель', 'Buyer'),
    )
    user_role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='Administrator')
    image = models.ImageField(upload_to='user_image', null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)


class Brand(models.Model):
    brand_name = models.CharField(max_length=32, null=True, blank=True)


class Model(models.Model):
    model_name = models.CharField(max_length=32, null=True, blank=True)


class Car(models.Model):
    year = models.PositiveSmallIntegerField()
    fuel_type = models.CharField(max_length=32, null=True, blank=True, verbose_name='тип топлива')
    AUTO_CHOICES = (
        ('автомат', 'автомат'),
        ('механика', 'механика')
    )
    transmission = models.CharField(max_length=32, choices=AUTO_CHOICES, null=True, blank=True)
    mileage = models.IntegerField(verbose_name='пробег')
    price = models.PositiveSmallIntegerField()
    description = models.TextField()
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='seller_user')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='category_car')
    brand = models.ForeignKey(Model, on_delete=models.CASCADE, null=True, blank=True, related_name='brand')
    model = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True, related_name='model')
    images = models.ImageField(upload_to='car_image', null=True, blank=True)


class Image(models.Model):
    car_image = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='car_images')
    image = models.ImageField(upload_to='image')

    def __str__(self):
        return self.image


class Auction(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name='car')
    start_price = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    start_time = models.DateField(null=True, blank=True)
    end_time = models.DateField(null=True, blank=True)
    STATUS_CHOICES = (
        ('активен', 'активен'),
        ('завершен', 'завершен'),
        ('отменен', 'отменен'),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, null=True, blank=True)

    def __str__(self):
        return f'{self.min_price} - {self.start_price}'


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, null=True, blank=True, related_name='auction')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='buyer_bid')
    amount = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='размер ставки')
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.created_at

    def clean(self):
        if self.amount < self.auction.min_price:
            raise ValidationError('Ставка должна быть больше минимальной цены!')

        highest_bid = self.auction.bids.order_by('-amount').first()
        if highest_bid and self.amount <= highest_bid.amount:
            raise ValidationError('Ставка должна быть выше предыдущей максимальной ставки!')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class FeedBack(models.Model):
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='seller')
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True, related_name='buyer')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.buyer} - {self.rating}'
