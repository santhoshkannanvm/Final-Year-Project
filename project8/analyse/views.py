from django.shortcuts import render,redirect
from .models import *
from process.models import *
from organisation.models import *
from django.contrib import messages

def analyse_index(request):
    return render(request, 'analyse/analyse_index.html')




def analyse_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        gender = request.POST['gender']
        Analyse_register(username=username, email=email, password=password, contact=contact, address=address,gender=gender
                      ).save()
        messages.info(request, "SUCCESSFULLY REGISTERED READY FOR LOGIN")
        return redirect('/analyse_login/')
    return render(request, 'analyse/analyse_register.html')




def analyse_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            emp = Analyse_register.objects.get(email=email, password=password)
            request.session['analyse'] = emp.email
            print('hi')
            messages.info(request, "SUCCESSFULLY LOGIN")
            return redirect('/analyse_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'analyse/analyse_login.html')



def view_PREDICTED(request):
    datas = O_purpose.objects.all()
    return render(request, 'analyse/view_predicted.html',{'datas':datas})

def find_report(request,id):
    datas = r_isotope.objects.get(id=id)
    x=datas.result
    y=int(x)
    print(x)
    if y >400:
        messages.info(request,'ISTOPE TESTTING COMPLETE SUCCESSFULLY REPORTED HARMFUL')
        ka='HARMFUL'
        st = r_isotope.objects.filter(id=id).update(solutions=ka)
    elif y <400:
        messages.info(request,'ISTOPE TESTTING COMPLETE SUCCESSFULLY REPORTED SAFE')
        ka='SAFE'
        st = r_isotope.objects.filter(id=id).update(solution=ka)

    return redirect('/view_data_final.html/ Q')


def view_report(request):
    datas = r_isotope.objects.all()
    return render(request, 'analyse/view_data.html',{'datas':datas})

def view_final_report(request):
    datas = r_isotope.objects.all()
    return render(request, 'analyse/view_data_final.html',{'datas':datas})

def send_predicted_data(request):
    datas = O_purpose.objects.filter(boolran=True)
    datas.boolean=True
    datas.save()
    messages.info('DATAS FORWARD TO TECHNICAL SUCCESSFULLY')
    return redirect('/view_PREDICTED/')



def analyse_logout(request):
    return redirect('/')