from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, auth
from .models import Booking, Contact, Gallery, BookingHistory
import datetime
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# controller
def showIndex(request, msg):
    msg = msg
    imgs = Gallery.objects.order_by('uploaded_at').all()[:5]
    return render(request, 'Pages/home.html', {'title': 'Homepage | Manang Futsal', 'msg': msg, 'imgs': imgs})


def showHome(request):
    imgs = Gallery.objects.order_by('uploaded_at').all()[:5]
    msg = 'Welcome'
    return render(request, 'Pages/home.html', {'title': 'Homepage | Manang Futsal', 'msg': msg, 'imgs': imgs})


def showAbout(request):
    return render(request, 'Pages/about.html', {'title': 'About | Manang Futsal', })


# check bookings


def checkBooking(request):
    books = Booking.objects.filter(booked_date=datetime.datetime.today())
    t_date = datetime.date.today()
    if request.POST['check-date'] and request.POST['check-time']:
        check_date = request.POST['check-date']
        check_time = request.POST['check-time']
        try:
            Booking.objects.get(booked_date=check_date, book_time=check_time)
            check_fail = 'Time Slot Unavailable'
            return render(request, 'Pages/booking.html',
                              {'title': 'Book | Manang Futsal', 'msg': 'Book here', 'books': books,
                           't_date': t_date, 'c_fail': check_fail})

        except Booking.DoesNotExist:
            check_sucess = 'Time Slot Available'
            return render(request, 'Pages/booking.html',
                          {'title': 'Book | Manang Futsal', 'msg': 'Book here', 'books': books,
                           't_date': t_date, 'c_sucess': check_sucess})
    else:
        check_error = 'Enter Valid Date and Time'
        return render(request, 'Pages/booking.html',
                      {'title': 'Book | Manang Futsal', 'msg': 'Book here', 'books': books,
                       't_date': t_date, 'c_error': check_error})


def booking(request):
    books = Booking.objects.filter(booked_date=datetime.datetime.today())
    t_date = datetime.date.today()

    if request.method == 'GET':
        return render(request, 'Pages/booking.html',
                      {'title': 'Book | Manang Futsal', 'msg': 'Book here', 'books': books,
                       't_date': t_date})
    else:

        # authenticate user
        if request.user.is_authenticated:
            # check if date is inserted
            if request.POST['book-date']:

                choice = request.POST['choice']

                if choice == '1':
                    time = datetime.time(6, 00, 00)
                elif choice == '2':
                    time = datetime.time(7, 00, 00)
                elif choice == '3':
                    time = datetime.time(8, 00, 00)
                elif choice == '4':
                    time = datetime.time(9, 00, 00)
                elif choice == '5':
                    time = datetime.time(10, 00, 00)
                elif choice == '6':
                    time = datetime.time(11, 00, 00)
                elif choice == '7':
                    time = datetime.time(12, 00, 00)
                elif choice == '8':
                    time = datetime.time(13, 00, 00)
                elif choice == '9':
                    time = datetime.time(14, 00, 00)
                elif choice == '10':
                    time = datetime.time(15, 00, 00)
                elif choice == '11':
                    time = datetime.time(16, 00, 00)
                elif choice == '12':
                    time = datetime.time(17, 00, 00)
                elif choice == '13':
                    time = datetime.time(18, 00, 00)
                elif choice == '14':
                    time = datetime.time(19, 00, 00)

                # date = datetime.date(2021, 11, 6)

                date = request.POST['book-date']
                v_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                f_date = datetime.datetime.today() + timedelta(days=3)

                # check if book date is more than 3 days advance

                if v_date > f_date:
                    error_msg = "Booking Limit is 3 days Advance"
                    return render(request, 'Pages/booking.html',
                                  {'title': 'Book | Manang Futsal', 'error_msg': error_msg})
                else:
                    if datetime.datetime.today() > v_date and datetime.datetime.now().time() > time:
                        error_msg = "Date/Time Cannot Be of Past"
                        return render(request, 'Pages/booking.html',
                                      {'title': 'Book | Manang Futsal', 'error_msg': error_msg,
                                       'books': books, 't_date':t_date})
                    else:
                        # check if the booking exists
                        try:
                            # if booking exists throw an error message
                            Booking.objects.get(booked_date=date, book_time=time)
                            warning_msg = "Booking time is not available"
                            return render(request, 'Pages/booking.html',
                                          {'title': 'Book | Manang Futsal', 'warning_msg': warning_msg,
                                           'books': books, 't_date': t_date})
                        except Booking.DoesNotExist:
                            # if booking does not exists
                            book = Booking()
                            c_user = request.user
                            c_contact = Contact.objects.get(user=c_user)
                            book.booked_by = c_user
                            book.book_time = time
                            book.booked_date = date
                            book.contact = c_contact.contact
                            book.save()

                            # trigger update for history
                            history = BookingHistory()
                            history.booked_by = request.user
                            history.booked_time = time
                            history.booked_date = date
                            history.save()

                            msg = "Futsal Booked"
                            return render(request, 'Pages/booking.html', {'title': 'Book | Manang Futsal', 'msg': msg,
                                                                          'books': books, 't_date': t_date})
                    # if Date not inserted
            else:
                warning_msg = "Insert Date"
                return render(request, 'Pages/booking.html', {'title': 'Book | Manang Futsal',
                                                              'warning_msg': warning_msg, 'books': books,
                                                              't_date': t_date})
            # if not logged in
        else:
            msg = "Please Login!!"
            return render(request, 'Pages/login.html', {'title': 'Login | Manang Futsal', 'msg': msg})


# authenticate user
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'GET':
            return render(request, 'Pages/login.html', {'title': 'Login | Manang Futsal', })
        else:
            if request.POST['username'] and request.POST['password']:

                username1 = request.POST['username']
                password1 = request.POST['password']

                user = authenticate(username=username1, password=password1)

                if user is not None:
                    auth.login(request, user)
                    msg = "User Logged in"
                    return redirect('index', msg)
                else:
                    message = "Invalid Login Credentials"
                    return render(request, 'Pages/login.html', {'title': 'Login | Manang Futsal', 'message': message})
            else:
                message = "Must enter Username and Password"
                return render(request, 'Pages/login.html', {'title': 'Login | Manang Futsal', 'message': message})


def logoutUser(request):      # logout user
    if request.user.is_authenticated:
        auth.logout(request)
        imgs = Gallery.objects.order_by('uploaded_at').all()[:5]
        msg = "User Logged out"
        return render(request, 'Pages/home.html', {'title': 'Home | Manang Futsal', 'msg': msg, 'imgs': imgs})
    else:
        return redirect('/')


def cancel(request, id):  # booking cancel
    books = Booking.objects.filter(booked_date=datetime.datetime.today())
    # user is superuser
    if request.user.is_staff:
        # check if booking exists
        try:
            check = Booking.objects.get(pk=id)

            # recording for history
            history = BookingHistory()
            history.booked_time = check.book_time
            history.booked_by = check.booked_by
            history.booked_date = check.booked_date
            history.deleted_at = datetime.datetime.now()
            history.save()

            # booking cancel
            check.delete()
            msg = "Booking successfully canceled"

            return render(request, 'Pages/booking.html', {'title': 'Book | Manang Futsal', 'msg': msg,
                                                          'books': books})
        except Booking.DoesNotExist:
            return redirect('book')

    else:
        redirect('home')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'GET':
            return render(request, 'Pages/register.html')
        else:

            # validation

            if request.POST['your-email']:
                email = request.POST['your-email']
            else:
                message = 'Please Enter Your Email'
                return render(request, 'Pages/register.html', {'message': message})

            if request.POST['your-fname'] and request.POST['your-lname']:
                fname = request.POST['your-fname']
                lname = request.POST['your-lname']
            else:
                message = 'Please Enter Your Name'
                return render(request, 'Pages/register.html', {'message': message})

            if request.POST['phone']:
                contactN = request.POST['phone']
            else:
                message = 'Enter your Phone Number'
                return render(request, 'Pages/register.html', {'message': message})

            if request.POST['password'] and request.POST['re-password']:
                if request.POST['password'] == request.POST['re-password']:
                    password = request.POST['password']
                else:
                    message = 'Passwords Do not Match'
                    return render(request, 'Pages/register.html', {'message': message})
            else:
                message = 'Please Confirm Password'
                return render(request, 'Pages/register.html', {'message': message})

            # registration process
            try:
                user = User.objects.get(username=fname)
                email_v = User.objects.get(email=email)
                message = 'User already exists'
                return render(request, 'Pages/register.html', {'message': message})
            except User.DoesNotExist:
                user = User.objects.create_user(fname, email, password)
                user.first_name = fname
                user.last_name = lname
                user.save()

                log = authenticate(username=fname, password=password)
                auth.login(request, log)

                # contact info
                contact = Contact()
                contact.user = request.user
                contact.contact = contactN
                contact.save()

                return render(request, 'Pages/home.html', {'title': 'Home | Manang Futsal',
                                                           'msg': 'User Registered and Logged in'})