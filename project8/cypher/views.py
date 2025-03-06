from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import random
import string
import base64
from django.conf import settings
import pyAesCrypt
from cryptography.fernet import Fernet
from django.conf import settings
from organisation.models import *
from .Encrypting import *
from adminstator.models import *
import pikepdf
from django.core.mail import send_mail

def cypher_index(request):
    return render(request, 'cypher/cypher_index.html')





def Cypherr_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        gender = request.POST['gender']
        cypher_register(username=username, email=email, password=password, contact=contact, address=address, gender=gender
                     ).save()
        messages.info(request, "SUCCESSFULLY REGISTERED READY FOR LOGIN")
        return redirect('/Cypher_login/')
    return render(request, 'cypher/cypher_register.html')









def Cypher_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            emp = cypher_register.objects.get(email=email, password=password)
            request.session['cypher'] = emp.email
            print('hi')
            messages.info(request, "SUCCESSFULLY LOGIN")
            return redirect('/cypher_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'cypher/cypher_login.html')


def view_file_domain(request):
    datas=O_details.objects.all()
    return render(request, 'cypher/view_org_file.html',{'datas':datas})


def Encrypt_file(request):
    datas=O_details.objects.all()
    return render(request, 'cypher/encrypt_file.html',{'datas':datas})


def encryption(request,id):
    datas = O_details.objects.get(id=id)
    r = datas.id
    file = datas.file
    print(file)

    location= f'{settings.MEDIA_ROOT}/{file}'
    old_pdf = pikepdf.Pdf.open(location)
    no_ext = pikepdf.Permissions(extract=False)
    old_pdf.save("yes11.pdf", encryption=pikepdf.Encryption(
        user="123asd", owner="wscube", allow=no_ext
    ))
    f = open("yes11.pdf", "r")

    # print(f.read(5))

    # x=old_pdf.save()
    # print(x)
    st = O_details.objects.filter(id=r).update(file2=f)
    return redirect('/Encrypt_file/')

    # encryptor.file_decrypt(loaded_key, 'enc_final.csv', 'dec_final.csv')



def admin_update(request):
    datas =O_details.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        adminfile = request.FILES['adminfile']
        cypher_admin_update(name=name, email=email, adminfile=adminfile
                        ).save()
    return render(request, 'cypher/cypher_update_form.html',{'datas':datas})


def view_admin(request):
    datas = O_purpose.objects.filter(boolean=True)
    return render(request, 'cypher/view_admin_request.html',{'datas':datas})





def admin_send_mail(request,id):
    datas=admin_rqst.objects.get(id=id)
    # t= datas.id_donor
    send_mail(
        'Subject here',
        f'WELCOME!!! YOUR FILE DECRYPT IS 123asd YOU CAN DECRYPT THE PDF FILE BY ENTERING  ,  ',
        'sarath@gmail.com',
        [datas.email],
        fail_silently=False,
    )
    messages.info(request, "wallet id successfully forwarded to donor mail")

    # datas.save()
    return redirect('/view_admin/')



def Cypher_logout(request):
    if 'cypher' in request.session:
        request.session.pop('cypher',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin/')


def from_testing(request):
    datas = O_purpose.objects.filter(boolean=True)
    return render(request, 'cypher/view_predicted_Data.html',{'datas':datas})



def enc(request,id):
    get = O_purpose.objects.get(id=id)
    # publicKey, privateKey = rsa.newkeys(512)
    # print(privateKey)
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
    inputvar.append(a)
    inputvar.append(b)
    inputvar.append(c)
    inputvar.append(d)
    inputvar.append(e)
    enc= []
    for i in inputvar:
        encoded_value = base64.b64encode(i.encode("ascii", "strict"))
        enc.append(encoded_value)

        # print(a)

        # decMessage = rsa.decrypt(encMessage, privateKey).decode()
        # print("decrypted string: ", decMessage)
    #     datas = mechanical_analysis.objects.get(id=id)
    #     datas.car_encrypt = a
    #     datas.save()
    print(enc)
    a = enc[0]
    b = enc[1]
    c = enc[2]
    d = enc[3]
    e = enc[4]
    st = O_purpose.objects.filter(id=r).update(organisation=a, type=b,purpose=c,quantaity=d,solutions=e)
    print(a, b)
    messages.info(request, "data encrypted successfully")

    return redirect('/view_admin/')



def ENCRYPTED(request):
    datas = O_purpose.objects.filter(boolean=True)
    return render(request, 'cypher/view_encypted.html',{'datas':datas})


def send_admin1(request,id):
    datas = O_purpose.objects.get(id=id)
    datas.boolean1 = True
    datas.save()
    messages.info(request,'DATA FORWARDED TO ADMIN SUCCESSFULLY')
    return redirect('/forwarded_data/')


def forwarded_data(request):
    datas = O_purpose.objects.filter(boolean1=True)
    return render(request, 'cypher/view_forwarded.html',{'datas':datas})

