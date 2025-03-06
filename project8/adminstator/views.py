from django.shortcuts import render,redirect
from django.contrib import messages
from organisation.models import *
from cypher.models import *
from .models import *
import os
from django.conf import settings
from django.http import HttpResponse, Http404



def a_index(request):
    return render(request, 'admin/admin_index.html')





def admin_login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        if username == "admin@gmail.com" and password == "admin@1234":
            request.session['admin'] = 'admin@gmail.com'
            messages.info(request, "LOGIN SUCCESSFULL")
            return redirect('/a_index/')
        elif username != "admin@gmail.com":
            messages.error(request, "Wrong Admin Email")
            return redirect('/admin_login/')
        elif password != "admin":
            messages.error(request, "Wrong Admin Password")
            return render(request, 'admin/admin_login.html')
    return render(request, 'admin/admin_login.html')









def download(request, id):
    data = O_details.objects.get(id=id)
    file = data.file2
    file_path = f'{settings.MEDIA_ROOT}/{file}'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            messages.info(request, "successfully image Downloaded")
            return response
    raise Http404


def view_org_file_admin(request):
    datas = org_register.objects.all()
    return render(request, 'admin/view_org_file_admin.html',{'datas':datas})




def admin_request(request):
    if request.method == 'POST':
        email = request.POST['email']
        Purpose = request.POST['Purpose']
        admin_rqst(email=email, Purpose=Purpose
                        ).save()
        messages.info(request, "SUCCESSFULLY REGISTERED READY FOR LOGIN")
        return redirect('/admin_request/')
    return render(request, 'admin/view_org_file_admin.html')




def view_org_details(request):
    datas = O_details.objects.all()
    return render(request, 'admin/view_org_details.html',{'datas':datas})

def view_org_details_approved(request):
    datas = O_details.objects.all()
    return render(request, 'admin/view_org_details_approved.html',{'datas':datas})




def org_send_mail(request,id):
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





def A_logout(request):
    if 'admin' in request.session:
        request.session.pop('administrator',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/A_logout/')


def access_o(request,id):
    data = org_register.objects.get(id=id)
    data.access=True
    data.save()
    t=data.username
    messages.info(request,f'GRANT ACCESS SUCCESSFLLY TO {t}')
    return redirect('/view_org_file_admin/')

def clear(request,id):
    data = O_details.objects.get(id=id)
    data.delete()
    messages.info(request,'DATA CLEARED SUCCESSFULLY')
    return redirect('/view_org_details/')



def payslip(request):
    if request.method == 'POST':
        organisation = request.POST['organisation']
        amount = request.POST['amount']
        admin_rqst(organisation=organisation, amount=amount
                        ).save()
        messages.info(request, "SUCCESSFULLY PAYSLIP SENT")
        return redirect('/payslip/')
    return render(request, 'admin/payslip.html')