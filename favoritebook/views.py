from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Book
from loginapp.models import User
import datetime
import bcrypt


def check_for_methodPOST(request):
    if request.method != 'POST':
        return redirect('/')


def check_for_user(request):
    if not 'userid' in request.session:
        return redirect('/')
    else:
        global logged_in_user
        logged_in_user = User.objects.get(email=request.session['userid'])


def booklist(request):
    check_for_user(request)
    context = {
        "logged_in_user": logged_in_user,
        "books": Book.objects.all()
    }
    return render(request, "success.html", context)


def addbook(request):
    check_for_methodPOST(request)
    check_for_user(request)
    if Book.objects.filter(title=request.POST['title']):
        messages.error(
            request, "A book with this title already exists", extra_tags='duplicate')
        return redirect('/books')
    book_errors = Book.objects.book_validator(request.POST)
    if len(book_errors) > 0:
        for key, value in book_errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/books')
    Book.objects.create(
        title=request.POST['title'], desc=request.POST['desc'], uploaded_by_id=logged_in_user)
    newbook = Book.objects.last()
    newbook.favorited_by.set([logged_in_user])
    return redirect('/books/' + str(newbook.id))


def addfavorite(request, bookid):
    check_for_methodPOST(request)
    check_for_user(request)
    thisbook = Book.objects.get(id=bookid)
    thisbook.favorited_by.add(logged_in_user)
    return redirect('/books/' + str(bookid))


def bookdetail(request, bookid):
    check_for_user(request)
    thisbook = Book.objects.get(id=bookid)
    context = {
        "thisbook": thisbook,
        "logged_in_user": logged_in_user,
        "favorited_by_list": Book.objects.get(id=bookid).favorited_by.all()
    }
    return render(request, "bookdetail.html", context)


def bookdelete(request, bookid):
    check_for_user(request)
    check_for_methodPOST(request)
    thisbook = Book.objects.get(id=bookid)
    if not thisbook.uploaded_by_id.id == logged_in_user.id:
        messages.error(request, "You cannot delete this book.",
                       extra_tags='bookowner')
        return redirect('/books/' + str(bookid))
    else:
        thisbook.delete()
    return redirect('/books')


def bookupdate(request, bookid):
    check_for_user(request)
    check_for_methodPOST(request)
    thisbook = Book.objects.get(id=bookid)
    if not logged_in_user.id == thisbook.uploaded_by_id.id:
        messages.error(request, "You cannot delete this book.",
                       extra_tags='bookowner')
        return redirect('/books/' + str(bookid))
    book_errors = Book.objects.book_validator(request.POST)
    if len(book_errors) > 0:
        for key, value in book_errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/books/' + str(bookid))
    thisbook.desc = request.POST['desc']
    thisbook.title = request.POST['title']
    thisbook.save()
    return redirect('/books/' + str(bookid))


def unfavorite(request, bookid):
    check_for_methodPOST(request)
    check_for_user(request)
    thisbook = Book.objects.get(id=bookid)
    thisbook.favorited_by.remove(logged_in_user)
    return redirect('/books/' + str(bookid))
