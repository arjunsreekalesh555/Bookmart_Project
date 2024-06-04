from django.conf import settings
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.urls import reverse
from rsbooks_app.models import *
from .models import RSBook, Cart, cartItem
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from rsbooks_app.forms import RSAuthorForm, RSBookForm
import stripe
# Create your views here.
def listBook(request):
    books=RSBook.objects.all()
    comedy_books=RSBook.objects.filter(genre='1')
    comedy_books_count=comedy_books.count()
    action_books=RSBook.objects.filter(genre='2')
    action_books_count=action_books.count()
    crime_books=RSBook.objects.filter(genre='3')
    crime_books_count=crime_books.count()
    horror_books=RSBook.objects.filter(genre='4')
    horror_books_count=horror_books.count()
    romance_books=RSBook.objects.filter(genre='5')
    romance_books_count=romance_books.count()
    thriller_books=RSBook.objects.filter(genre='6')
    thriller_books_count=thriller_books.count()
    adventure_books=RSBook.objects.filter(genre='7')
    adventure_books_count=adventure_books.count()
    sports_books=RSBook.objects.filter(genre='8')
    sports_books_count=sports_books.count()
    inspirational_books=RSBook.objects.filter(genre='9')
    inspirational_books_count=inspirational_books.count()

    #pagination-Paginator(var books are stored, how much books
    paginator=Paginator(books, 6) #how much books to show from paginator
    page_number=request.GET.get('page') #get corresponding pagenumber

    try:
        page=paginator.get_page(page_number) #to get correct page number

    except EmptyPage: #if incorrect page number, sjows an empty screen
        page=paginator.page(page_number.num_pages)

    context={
        'books': books,
        'page': page,
        'comedy_books':comedy_books,
        'comedy_books_count':comedy_books_count,
        'action_books':action_books,
        'action_books_count':action_books_count,
        'crime_books':crime_books,
        'crime_books_count':crime_books_count,
        'horror_books':horror_books,
        'horror_books_count': horror_books_count,
        'romance_books': romance_books,
        'romance_books_count': romance_books_count,
        'thriller_books':thriller_books,
        'thriller_books_count': thriller_books_count,
        'adventure_books':adventure_books,
        'adventure_books_count': adventure_books_count,
        'sports_books':sports_books,
        'sports_books_count': sports_books_count,
        'inspirational_books': inspirational_books,
        'inspirational_books_count': inspirational_books_count,
    }

    return render(request, 'user/userlist.html', context)

def detailView(request, book_id):
    book=RSBook.objects.get(id=book_id)

    return render(request, 'user/userdetails.html', {'book':book})

def searchBook(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=RSBook.objects.filter(Q(title__icontains=query))
    else:
        books=[]

    return render(request, 'user/usersearch.html', {'books':books, 'query':query})

def add_to_cart(request, book_id):
    book=RSBook.objects.get(id=book_id)

    if book.quantity>0:
        cart, created=Cart.objects.get_or_create(user=request.user)
        cart_item, item_created=cartItem.objects.get_or_create(cart=cart, book=book)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

    return redirect('viewcart')

def view_cart(request):
    cart, created=Cart.objects.get_or_create(user=request.user)
    cart_items=cart.cartitem_set.all()
    cart_item=cartItem.objects.all()
    total_price=sum(item.book.price * item.quantity for item in cart_items)
    total_items=cart_items.count()

    context={
        'cart_items':cart_items,
        'cart_item':cart_item,
        'total_price':total_price,
        'total_items':total_items
    }

    return render(request, 'user/cart.html', context)

def increase_quantity(request, item_id):
    cart_item=cartItem.objects.get(id=item_id)

    if cart_item.quantity < cart_item.book.quantity:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('viewcart')

def decrease_quantity(request, item_id):
    cart_item=cartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:

        cart_item.quantity -= 1
        cart_item.save()

    return redirect('viewcart')

def remove_from_cart(request, item_id):
    try:
        cart_item=cartItem.objects.get(id=item_id)
        cart_item.delete()

    except cart_item.DoesNotExist:
        pass

    return redirect('viewcart')

#checkout session
def createCheckout(request):
    cartitems=cartItem.objects.all()

    if cartitems:
        stripe.api_key=settings.STRIPE_SECRET_KEY

        if request.method=='POST':
            lineitems=[]

            for cartitem in cartitems:
                lineitem={
                    'price_data':{
                        'currency':'INR',
                        'unit_amount':int(cartitem.book.price * 100), #change into paisa
                        'product_data':{
                            'name':{cartitem.book.title}
                        },
                    },
                         "quantity":1
                }
                lineitems.append(lineitem)

            if lineitems:
                checkout_session=stripe.checkout.Session.create(
                    payment_method_types=['card'],
                    line_items=lineitems,
                    mode='payment',
                    success_url=request.build_absolute_uri(reverse('success')),
                    cancel_url=request.build_absolute_uri(reverse('cancel')),

                )

                return  redirect(checkout_session.url, code=303)

# success url
def success(request):
    cartitems=cartItem.objects.all()

    for cartitem in cartitems:
        product=cartitem.book

        if product.quantity >= cartitem.quantity:
            product.quantity -= cartitem.quantity
            product.save()

    cartitems.delete()

    return render(request, 'user/success.html')

# cancel url
def cancel(request):

    return render(request, 'user/cancel.html')

