from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from .forms import RSAuthorForm, RSBookForm

# Create your views here.
def createRSBook(request):
    books=RSBook.objects.all()

    if request.method=='POST':
        form=RSBookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('createbook')

    else:
        form=RSBookForm()

    return render(request, 'admin/create.html', {'books':books, 'form':form})


def createRSAuthor(request):
    if request.method == 'POST':
        form=RSAuthorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('createbook')

    else:
        form=RSAuthorForm()

    return render(request, 'admin/author.html', {'form': form})

def listBooks(request):
    books=RSBook.objects.all()

    paginator=Paginator(books, 6)
    page_number=request.GET.get('page')

    try:
        page=paginator.get_page(page_number)

    except EmptyPage:
        page=paginator.page(page_number.num_pages)



    return render(request, 'admin/listbook.html', {'books':books, 'page':page})

def bookDetails(request, book_id):
    book=RSBook.objects.get(id=book_id)

    return render(request, 'admin/details.html', {'book':book})

def deleteBook(request, book_id):
    book=RSBook.objects.get(id=book_id)

    if request.method=='POST':
        book.delete()

        return redirect('/')

    return render(request, 'admin/delete.html', {'book':book})

def updateBook(request, book_id):
    book=RSBook.objects.get(id=book_id)

    if request.method=='POST':
        form=RSBookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form=RSBookForm(instance=book)
    return render(request, 'admin/update.html', {'form':form})

def searchBook(request):
    query=None
    books=None

    if 'q' in request.GET:
        query=request.GET.get('q')
        books=RSBook.objects.filter(Q(title__icontains=query))
    else:
        books=[]

    return render(request, 'admin/searchbook.html', {'books': books, 'query': query})


def real_story_books(request):
    query = request.GET.get('r', None)
    books = RSBook.objects.filter(category='1')

    if query:
        books = books.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'admin/search_real_books.html', {'books': books, 'query': query})


def fiction_books(request):
    query = request.GET.get('f', None)
    books = RSBook.objects.filter(category='2')

    if query:
        books = books.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'admin/search_fiction_books.html', {'books': books, 'query': query})

#for author drop down
def author(request):
    authors=RSAuthor.objects.all()

    if request.method=='POST':
        new_author_name=request.POST.get('author_name')
        if new_author_name:
            RSAuthor.objects.create(name=new_author_name)
            return redirect('author')

    return render(request, 'user/author.html', {'authors': authors})


from .models import RSBook


def realstoryBook(request):
    real_story=RSBook.objects.filter(category='1')

    return render(request, 'user/category1.html', {'real_story':real_story})


def fictionBook(request):
    fiction_story=RSBook.objects.filter(category='2')

    return render(request, 'user/category2.html', {'fiction_story': fiction_story})

def comedy(request):
    comedy_books=RSBook.objects.filter(genre='1')
    comedy_books_count=comedy_books.count()

    return render(request, 'user/comedy.html', {'comedy_books':comedy_books, 'comedy_books_count':comedy_books_count})

def action(request):
    action_books=RSBook.objects.filter(genre='2')
    action_books_count=action_books.count()

    return render(request, 'user/action.html', {'action_books':action_books, 'action_books_count':action_books_count})

def crime(request):
    crime_books=RSBook.objects.filter(genre='3')
    crime_books_count=crime_books.count()

    return render(request, 'user/crime.html', {'crime_books':crime_books, 'crime_books_count':crime_books_count})

def horror(request):
    horror_books=RSBook.objects.filter(genre='4')
    horror_books_count=horror_books.count()

    return render(request, 'user/horror.html', {'horror_story':horror_books, 'horror_books_count':horror_books_count})


def romance(request):
    romance_books=RSBook.objects.filter(genre='5')
    romance_books_count=romance_books.count()

    return render(request, 'user/romance.html', {'romance_books':romance_books, 'romance_books_count':romance_books_count})

def adventure(request):
    adventure_books=RSBook.objects.filter(genre='6')
    adventure_books_count=adventure_books.count()

    return render(request, 'user/adventure.html', {'adventure_books':adventure_books, 'adventure_books_count':adventure_books_count})

def thriller(request):
    thriller_books=RSBook.objects.filter(genre='7')
    thriller_books_count=thriller_books.count()

    return render(request, 'user/thriller.html', {'thriller_books':thriller_books, 'thriller_books_count':thriller_books_count})

def sports(request):
    sports_books=RSBook.objects.filter(genre='8')
    sports_books_count=sports_books.count()

    return render(request, 'user/sports.html', {'sports_books':sports_books, 'sports_books_count':sports_books_count})

def inspirational(request):
    inspirational_books=RSBook.objects.filter(genre='9')
    inspirational_books_count=inspirational_books.count()

    return render(request, 'user/inspirational.html', {'inspirational_books':inspirational_books, 'inspirational_books_count':inspirational_books_count})


def main(request):

    return render(request, 'admin/main.html')

def genre(request):
    comedy_books=RSBook.objects.filter(genre='1')
    action_books=RSBook.objects.filter(genre='2')
    crime_books=RSBook.objects.filter(genre='3')
    horror_books=RSBook.objects.filter(genre='4')
    romance_books=RSBook.objects.filter(genre='5')
    thriller_books=RSBook.objects.filter(genre='6')
    adventure_books=RSBook.objects.filter(genre='7')
    sports_books=RSBook.objects.filter(genre='8')
    inspirational_books=RSBook.objects.filter(genre='9')

    context={

        'comedy_books':comedy_books,
        'action_books':action_books,
        'crime_books':crime_books,
        'horror_books':horror_books,
        'romance_books': romance_books,
        'thriller_books':thriller_books,
        'adventure_books':adventure_books,
        'sports_books':sports_books,
        'inspirational_books': inspirational_books,

    }

    return render(request, 'user/genre.html', context)

