from django.shortcuts import render
from .models import book
from .models import card
#from .models import payment
from .models import UserRegister
from .models import Contact
from .models import availablerooms
#from .models import Cancel
# Create your views here.


'''cancel ki database add chai
auto field
room number add chai
db book module lo change paru to name

display lo card type and cvv hide chai'''



def openHomePage(request):
    type="Home"
    return render(request,'index.html',{"type":type})


def openServicesPage(request):
    type=request.GET.get("type")
    return render(request,'index.html',{"type":type})


def openUser(request):
    type=request.GET.get("type")
    return render(request,'index.html',{"type":type})


def loginUser(request):
    username = request.POST.get("email")
    password = request.POST.get("pass")
    res = UserRegister.objects.filter(email_id=username, password=password)
    # print(res)
    if not res:
        return render(request, 'index.html', {"type": 'h_user', "message": "Invalid User"})
    else:
        for x in res:
            print(x)
        return render(request, 'index2.html', {"type": type, "name": x})

def openSignUpPage(request):
    type = request.GET.get("type")
    return render(request, 'index.html', {"type": type})


def registerUser(request):
    u_fname = request.POST.get('u_fname')
    u_lname = request.POST.get('u_lname')
    u_email = request.POST.get('u_email')
    u_pass = request.POST.get('u_pass')
    u_rpass = request.POST.get('u_rpass')
    u_cno = request.POST.get('u_cno')
    u_add = request.POST.get('u_add')
    # print(u_fname,u_lname,u_email,u_pass,u_cno,u_add)
    ur = UserRegister(fname=u_fname, lname=u_lname, email_id=u_email, password=u_pass, rpassword=u_rpass,
                      contact_no=u_cno, address=u_add)
    ur.save()
    return render(request, 'index.html', {"type": "h_user", "message": "User Register Successfully"})


def openUserHomePage(request):
    type="home"
    return render(request, 'index2.html', {"type":type})


def openBookingPage(request):
    type=request.GET.get("type")
    res = availablerooms.objects.values('room_type')
    room= ["Select"]
    for x in res:
        room.append(x["room_type"])
    return render(request, 'index2.html', {"type": type, "room": room})
def oopenbookingPage(request):
    rm= request.POST.get('roomm')
    name = request.POST.get('name')
    check_in = request.POST.get('check_in')
    check_out = request.POST.get('check_out')
    contact_no = request.POST.get('contact_no')
    address = request.POST.get('address')
    card_no = request.POST.get('card_no')
    cvv = request.POST.get('cvvno')
    card_type = request.POST.get('roo')
    dr=book(rom=rm,paru=name,cin=check_in,cout=check_out,cno=contact_no,addr=address,cnum=card_no,cv=cvv,cord_type=card_type)
    dr.save()
    return render(request, "index2.html", {"type":'payment'})

def opendisplay(request):
    recs = book.objects.filter()
    return render(request,'index2.html',{"type":'display','records':recs})





#================================================
def openCancelPage(request):
    type=request.GET.get("type")
    return render(request,'index2.html',{"type":type})

def CancelPage(request):
    u_name=request.POST.get('u_name')
    u_room=request.POST.get('u_room')
    u_id=request.POST.get('u_id')
    ucan=display(USERNAME=u_name,ROOM_NO=u_room,CUSTOMER_ID=u_id)
    ucan.save()
    return render(request,'index2.html',{"type":'u_cancel',"message":"Successfully Room Canceled"})

#=========================================
def openContact(request):
    type = request.GET.get("type")
    return render(request, "index.html", {"type": type})

def ContactPage(request):
    u_name=request.POST.get('u_name')
    u_email=request.POST.get('u_email')
    u_phone=request.POST.get('u_phone')
    u_mess=request.POST.get('u_mess')
    #print(u_name,u_email,u_phone,u_phone,u_mess)
    uc=Contact(name=u_name,Email_id=u_email,phone_no=u_phone,message=u_mess)
    uc.save()

    return render(request,'index.html',{"type":'contact',"message":'Successfully message sent'})

