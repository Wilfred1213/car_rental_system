from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()




class Category(models.Model):
    CAR_CATEGORY=[
        ('SEDAN_SALOON', 'Sedan (Saloon)'),
        ('SPORT_UTILITY_VEHICLE_SUV', 'Sport-Utility Vehicle (SUV)'),
        ('CROSSOVER_UTILITY_VEHICLE_CUV', 'Crossover Utility Vehicle (CUV)'),
        ('PICKUP_TRUCK', 'Pickup Truck'),
        ('COUPE', 'Coupe'),
        ('SPORTS_CAR_SUPERCAR', 'Sports Car / Supercar'),
        ('HATCHBACK', 'Hatchback'),
        ('STATION_WAGON_ESTATE', 'Station Wagon (Estate)'),
        ('CONVERTIBLE', 'Convertible'),
        ('MINIVAN', 'Minivan'),
    ]
    name = models.CharField(max_length=255, choices=CAR_CATEGORY)
    image = models.ImageField(upload_to='media', null=True)

# class Pricing(models.Model):
#     car = models.ForeignKey('Cars', on_delete=models.CASCADE, null=True)
#     price = models.BigIntegerField(default=0)
#     fuel = models.CharField(max_length=100, null=True)


    def __str__(self):
        return self.car.name
    
class Cars(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.BigIntegerField(default=0)
    image = models.ImageField(upload_to='media')
    model = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return (f'Category: {self.category.name} -- Car name:{self.name} -- price {self.price}')


class PricingTier(models.Model):
    name = models.CharField(max_length=100)  # e.g. "Hourly", "Daily", "Monthly"
    duration = models.IntegerField()  # e.g. 1 hour, 1 day, 1 month
    price = models.DecimalField(max_digits=5, decimal_places=2)
    fuel_surcharge = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return self.name
                
class CarPricing(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    pricing_tier_hour = models.ForeignKey('PricingTier', on_delete=models.CASCADE)
    pricing_tier_daily = models.ForeignKey('PricingTier', on_delete=models.CASCADE, related_name='daily', null=True)
    pricing_tier_leasing = models.ForeignKey('PricingTier', on_delete=models.CASCADE, related_name='leasing', null=True)
    def __str__(self):
        return (f'Category: {self.car.category.name} -- Car name:{self.car.name} -- price {self.car.price}')

class RentCar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    pick_up_location = models.CharField(max_length=500)
    drop_off_location = models.CharField(max_length=500)
    pick_up_date =models.DateField()
    drop_off_date = models.DateField()
    pick_up_time= models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Cars,on_delete=models.CASCADE, null = True)
   
    def availability(self, pick_up, drop_off):
        bookings = RentCar.objects.filter(
            car=self.car,
            pick_up_date__lte=pick_up,
            drop_off_date__gte=drop_off
        ).exclude(id=self.id)
        return bookings.exists()
    
class Features(models.Model):
    CAR_FEATURE=[
        ('AIRCONDITIONS', 'Airconditions'),
        ('CHILD SEAT', 'Child Seat'),
        ('GPS', 'GPS'),
        ('LUGGAGE', 'Luggage'),
        ('MUSIC', 'Music'),
        ('SEAT BELT', 'Seat Belt'),
        ('SLEEPING BED', 'Sleeping Bed'),
        ('WATER', 'Water'),
        ('BLUETOOTH', 'Bluetooth'),
        ('ONBOARD COMPUTER', 'Onboard computer'),
        
        ('AUDIO INPUT', 'Audio input'),
        ('LONG TERM TRIPS', 'Long Term Trips'),
        ('CAR KIT', 'Car Kit'),
        ('REMOTE CENTRAL LOCKING', 'Remote central locking'),
        ('CLIMATE CONTROL', 'Climate control'),   

    ]
    functions = models.CharField(max_length=255, choices=CAR_FEATURE)
    is_true = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null = True)
    icon = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.functions

class Operations(models.Model):
    gadgets = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    options = models.CharField(max_length=255, null=True)
    icon = models.CharField(max_length=50, null=True) 

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rate = models.IntegerField(default=0)
    comment = models.TextField(max_length=1000)
    car = models.ForeignKey(Cars,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

class RentingInstruction(models.Model):
    icon = models.CharField(max_length=255)
    instruction = models.CharField(max_length=255)

    def __str__(self):
        return self.instruction
    
class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    body =models.TextField(max_length=1000)
    image = models.ImageField(upload_to='media')

class LatestService(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body =models.TextField(max_length=1000)

    def __str__(self):
        return self.title

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    body =models.TextField(max_length=3000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    email =models.EmailField(max_length=255)
    message = models.TextField(max_length=500)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f'{self.name} -- {self.email}'


