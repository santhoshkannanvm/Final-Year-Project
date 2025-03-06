from django.shortcuts import render,redirect
from .models import *
from .models import O_purpose
from adminstator.models import *
from django.contrib import messages
import base64
import rsa
def organisation_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        gender = request.POST['gender']
        org_register(username=username, email=email, password=password, contact=contact, address=address,gender=gender
                      ).save()
        messages.info(request, "SUCCESSFULLY REGISTERED READY FOR LOGIN")
        return redirect('/organisation_register/')
    return render(request, 'organisation/org_register.html')




def organisation_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        emp = org_register.objects.get(email=email, password=password)
        # data= org_register.objects.all()
        x = emp.access
        print(x)
        request.session['organisation'] = emp.email
        if x == True:
            print('hi')
            messages.info(request, "SUCCESSFULLY LOGIN")
            return redirect('/org_index/')
        else:
            print('false')
            messages.info(request, "NEED ADMIN APPROVAL")




    return render(request, 'organisation/org_login.html')





    return render(request,'login/index.html')



def org_index(request):
    return render(request, 'organisation/org_index.html')


def org_details(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        city = request.POST['city']
        state = request.POST['state']
        file = request.FILES['file']
        O_details(name=name, email=email, number=number, city=city, state=state,file=file
                      ).save()
        messages.info(request, "SUCCESSFULLY DETAILS UPDATED")
        return redirect('/org_index/')

    return render(request, 'organisation/organisation_details.html')



def org_purpose_Details(request):
    datas = O_purpose.objects.filter(boolean=True)
    if request.method == 'POST':
        organisation = request.POST['organisation']
        type = request.POST['type']
        purpose = request.POST['purpose']
        quantaity = request.POST['quantaity']
        certified = request.POST['certified']
        query = request.POST['query']
        O_purpose(organisation=organisation, type=type, purpose=purpose, quantaity=quantaity, certified=certified,
                      query=query).save()
        messages.info(request, "SUCCESSFULLY DETAILS UPDATED")
        return redirect('/org_purpose_Details/')
    return render(request, 'organisation/org_purpose.html')






def dec11(request,id):
    get = O_purpose.objects.get(id=id)
    publicKey, privateKey = rsa.newkeys(512)

    r = get.id
    inputvar = []
    get.save()

    a = get.organisation
    b = get.type
    c = get.purpose
    d = get.quantaity
    e = get.solutions
    print(a)
    print(b)
    de=[]

    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)

    k = inputvar[0].lstrip('b')
    a = inputvar[1].lstrip('b')
    s = inputvar[0].lstrip('b')
    S = inputvar[1].lstrip('b')
    u = inputvar[0].lstrip('b')


    # inputvar.append(c)
    # inputvar.append(e)
    # inputvar.append(d)
    x = []
    m = [k,a,s,S,u]
    for i in m:
        msg = base64.b64decode(i)
        print('hello', msg)
        decoded_value = msg.decode("ascii", "strict")
        print('hi', decoded_value)
        de.append(decoded_value)
        print(de)

    # print()

        # print('l',de)
    # print(decoded_value)
    # print(enc)
    a = de[0]
    b = de[1]
    c = de[2]
    d = de[3]
    e = de[4]
    # f = de[5]
    st = O_purpose.objects.filter(id=r).update(organisation=a, type=b,purpose=c,quantaity=d,solutions=e)
    print(a, b)
    messages.info(request, "PAYMENT SUCCESSFULLY YOU CAN VIEW NOW!!")
    return redirect('/org_purpose_Details/')




def org_logout(request):
    if 'organisation' in request.session:
        request.session.pop('organisation',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/')


def pay(request):
    datas = admin_rqst.objects.all()
    return render(request, 'organisation/view_amount.html',{'datas':datas})


def view_DAta(request):
    datas = O_purpose.objects.filter(boolean1=True)
    return render(request, 'organisation/final_data.html',{'datas':datas})