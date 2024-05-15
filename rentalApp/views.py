from django.shortcuts import render, redirect
from rentalApp.models import Cars, BlogComment, PricingTier, CarPricing, Category,LatestService,Blog, AboutUs, RentingInstruction, RentCar, Operations, Features, Review
from django.contrib import messages
from rentalApp.forms import RentCarForm, bookingForm
from datetime import datetime
from django.db.models import Count
from django.db.models import Q
from django.core.paginator import Paginator

def index(request):
    all_cars = Cars.objects.all()
    blogs= Blog.objects.annotate(count_msg =Count('blogcomment')).order_by('-date')[0:3]
    instructions = RentingInstruction.objects.all()
     
    about = AboutUs.objects.first()
    latest_service =LatestService.objects.all()

    reviews = Review.objects.all()
    if request.method =='POST':
        form = RentCarForm(request.POST)

        car_id = form.data.get('car')
        car = Cars.objects.get(id=car_id)
        category = car.category  

        if form.is_valid():
            book=form.save(commit=False)
            book.user = request.user
            book.category = category
            book.car = car

            rent_car = RentCar(car=car, category=category)  # Create a new RentCar object
            rent_car.pick_up_date = book.pick_up_date
            rent_car.drop_off_date = book.drop_off_date

            if rent_car.availability(book.pick_up_date, book.drop_off_date):
                messages.info(request, 'This car is not available for the selected dates.')
                return redirect('index')
            book.save()
            messages.info(request, 'You just booked this car')
            return redirect('index') 
            
    form = RentCarForm()

    context = {
        'form':form,
        'cars':all_cars,
        'instructions':instructions,
        'abouts':about,
        'latests':latest_service,
        'reviews':reviews,
        'blogs':blogs
    }

    return render(request, 'rentalApp/index.html', context)

def services(request):
    return render(request, 'rentalApp/services.html', {})


# def pricing(request):
#     cars = Cars.objects.all()
#     pricing_tiers = PricingTier.objects.all()
#     car_pricings = CarPricing.objects.all()

#     # Group car pricings by car
#     car_pricings_grouped = {}
#     for car_pricing in car_pricings:
#         car = car_pricing.car
#         if car not in car_pricings_grouped:
#             car_pricings_grouped[car] = []
#         car_pricings_grouped[car].append(car_pricing)

#     context = {
#         'cars': cars,
#         'pricing_tiers': pricing_tiers,
#         'car_pricings_grouped': car_pricings_grouped,
#     }
#     return render(request, 'rentalApp/pricing.html', context)

def pricing(request):
    # price = Pricing.objects.all()
    # car = Cars.objects.prefetch_related('carpricing_set__pricing_tier').all()
    price = CarPricing.objects.all()
    context = {
        'prices':price
    }
    return render(request, 'rentalApp/pricing.html', context)

def contact(request):
    return render(request, 'rentalApp/contact.html')

def car(request):
    all_car =Cars.objects.all()

    paginator = Paginator(all_car, 9)  # Show 9 blogs per page
    page = request.GET.get('page')
    all_car = paginator.get_page(page)

    context = {
        'cars': all_car,
    }
    return render(request, 'rentalApp/car.html', context)

def car_detail(request, car_id):
    carid = Cars.objects.get(id=car_id)

    category = carid.category
    related_cars = Cars.objects.filter(category=category).exclude(id = car_id)
    reviews = Review.objects.filter(car = carid)
    gadgets = Operations.objects.filter(category=category)
    features = Features.objects.filter(category=category)

    average_rating = sum([review.rate for review in reviews]) / len(reviews) if reviews else 0

    rating_1_count = reviews.filter(rate=1).count()
    rating_1_percentage = (rating_1_count / len(reviews)) * 100 if len(reviews) > 0 else 0
    rating_2_count = reviews.filter(rate=2).count()
    rating_2_percentage = (rating_2_count / len(reviews)) * 100 if len(reviews) > 0 else 0
    rating_3_count = reviews.filter(rate=3).count()
    rating_3_percentage = (rating_3_count / len(reviews)) * 100 if len(reviews) > 0 else 0
    rating_4_count = reviews.filter(rate=4).count()
    rating_4_percentage = (rating_4_count / len(reviews)) * 100 if len(reviews) > 0 else 0
    rating_5_count = reviews.filter(rate=5).count()
    rating_5_percentage = (rating_5_count / len(reviews)) * 100 if len(reviews) > 0 else 0

    context = {
        'car': carid,
        'gadgets': gadgets,
        'features': features,
        'related': related_cars,
        'reviews': reviews,

        'average_rating': average_rating,
        'rating_1_count': rating_1_count,
        'rating_1_percentage': rating_1_percentage,
        'rating_2_count': rating_2_count,
        'rating_2_percentage': rating_2_percentage,
        'rating_3_count': rating_3_count,
        'rating_3_percentage': rating_3_percentage,
        'rating_4_count': rating_4_count,
        'rating_4_percentage': rating_4_percentage,
        'rating_5_count': rating_5_count,
        'rating_5_percentage': rating_5_percentage,

    }
    return render(request, 'rentalApp/car_single.html', context)

# def blog(request):
#     return render(request, 'rentalApp/blog.html')

def review(request, car_id):
    user = request.user
    car = Cars.objects.get(id =car_id)
    reviews = Review.objects.filter(car = car)

    if request.method =='POST':
        comment = request.POST.get('comment')
        rate= request.POST.get('rate')

        save_data = Review(user = user, comment = comment, rate = rate, car = car)
        save_data.save()

        messages.info(request, 'Thank you for rating us')
        return redirect('review', car_id)



    context = {
        'car': car,
        'reviews':reviews,
    }

    return render(request, 'rentalApp/review.html', context)

def booking(request, car_id):
    get_car = Cars.objects.get(id=car_id)
    instructions = RentingInstruction.objects.all()
    cars = Cars.objects.all()
    if request.method == 'POST':
        form = bookingForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.car = get_car
            book.category = get_car.category

            # Check if the car is already booked for the selected dates
            rent_car = RentCar(car=get_car)
            rent_car.pick_up_date = book.pick_up_date
            rent_car.drop_off_date = book.drop_off_date
            if rent_car.availability(book.pick_up_date, book.drop_off_date):
                messages.info(request, 'This car is not available for the selected dates.')
                return redirect('booking', car_id)

            # If the car is available, save the booking
            book.save()
            messages.info(request, 'You just booked this car')
            return redirect('booking', car_id)
    form = bookingForm()
    context = {
        'form': form,
        'car': get_car,
        'instructions':instructions,
        'cars':cars
    }
    return render(request, 'rentalApp/booking.html', context)



def blog(request):
    blogs = Blog.objects.annotate(count_msg=Count('blogcomment'))
    paginator = Paginator(blogs, 2)  # Show 2 blogs per page
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {
        'blogs': blogs,
    }
    return render(request, 'rentalApp/blog.html', context)

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id = blog_id)

    all_blogs = Blog.objects.annotate(count_msg=Count('blogcomment'))[:3]

    blog_search=None
    if request.method =='GET':
        search_query = request.GET.get('search')
        if search_query:
            blog_search = Blog.objects.filter(Q(title__icontains =search_query))if search_query else None

    comment = BlogComment.objects.filter(blog = blog).order_by('-date')
    comments_count = comment.aggregate(comment_count = Count('message'))
    categories = Category.objects.annotate(num_cars=Count('cars'))

    # categories = Category.objects.all()


    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        save_comment = BlogComment(user = request.user, blog = blog, name=name, email = email, message=message)
        save_comment.save()
        messages.info(request, 'Thanks for commenting on this car')
        return redirect('blog_detail', blog_id)
    context = {
        'blog':blog,
        'comments':comment,
        'blogs':all_blogs,
        'searches':blog_search,
        'categories':categories,
        'comments_count':comments_count
        
    }  
    return render(request, 'rentalApp/blog_single.html', context)


def category_detail(request, cat_id):
    cat_ids = Category.objects.get(id = cat_id)
    cars = Cars.objects.filter(category = cat_ids)
    context = {
        'related':cars,
        'cat_id':cat_ids
        
    }  
    return render(request, 'rentalApp/category.html', context)

def about(request):
    about_us = AboutUs.objects.first()

    context = {
        'abouts':about_us
    }
    return render(request, 'rentalApp/about.html', context)



