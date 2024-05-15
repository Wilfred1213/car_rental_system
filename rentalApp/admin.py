from django.contrib import admin

from rentalApp.models import Cars, CarPricing, PricingTier, BlogComment, Category, Blog, LatestService, AboutUs, RentingInstruction, RentCar, Features, Review, Operations

# Register your models here.
admin.site.register(Cars)
admin.site.register(Category)
admin.site.register(RentCar)
admin.site.register(CarPricing)
admin.site.register(PricingTier)
admin.site.register(Features)
admin.site.register(Review)
admin.site.register(Operations)
admin.site.register(RentingInstruction)
admin.site.register(AboutUs)
admin.site.register(LatestService)
admin.site.register(Blog)
admin.site.register(BlogComment)
