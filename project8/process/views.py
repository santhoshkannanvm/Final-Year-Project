from django.shortcuts import render,redirect
from organisation.models import *
from django.contrib import messages
from .models import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import GradientBoostingClassifier

def process_index(request):
    return render(request, 'process/process_index.html')



def Process_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        address = request.POST['address']
        gender = request.POST['gender']
        process_register(username=username, email=email, password=password, contact=contact, address=address,gender=gender
                      ).save()
        messages.info(request, "SUCCESSFULLY REGISTERED READY FOR LOGIN")
        return redirect('/Process_login/')
    return render(request, 'process/process_register.html')




def Process_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            emp = process_register.objects.get(email=email, password=password)
            request.session['process'] = emp.email
            print('hi')
            messages.info(request, "SUCCESSFULLY LOGIN")
            return redirect('/process_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'process/process_login.html')





def view_o_detail(request):
    datas = O_purpose.objects.all()
    return render(request, 'process/view_org_details.html',{'datas':datas})





def get_input(request, id):
    # if 'user' in request.session:
    get = O_purpose.objects.get(id=id)
    r=get.id
    inputvar = []
    get.save()
    type= get.type
    purpose= get.purpose
    # COMMUNICATION_BREAKDOWN= get.COMMUNICATION_BREAKDOWN
    # INADEQUATE=get.INADEQUATE
    # PLANNING= get.PLANNING
    # TEAM_MEMBER_PROCASTINATION= get.TEAM_MEMBER_PROCASTINATION
    # CLIENT_CHANGES_IN_PROJECT = get.CLIENT_CHANGES_IN_PROJECT
    # EXTERNAL_CHANGES = get.EXTERNAL_C
    #
    # ANGES




    inputvar.append(type)
    inputvar.append(purpose)
    # inputvar.append(INADEQUATE)
    # inputvar.append(PLANNING)
    # inputvar.append(TEAM_MEMBER_PROCASTINATION)
    # inputvar.append(CLIENT_CHANGES_IN_PROJECT)
    # inputvar.append(EXTERNAL_CHANGES)





    print('input:', inputvar)
    ka = algo(inputvar,r)
    print('OUTPUT:',ka)
    st = O_purpose.objects.filter(id=r).update(solutions=ka)
    return redirect('/view_o_detail_PREDICTED/')


def algo(datas,r):
    data = pd.read_csv('a_project_8.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = GradientBoostingClassifier()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    print(12334455)
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
        # return redirect('/loader/')
    return predicted[0]




def view_o_detail_PREDICTED(request):
    datas = O_purpose.objects.filter(boolean=False)
    return render(request, 'process/view_org_details_predicted.html',{'datas':datas})



def process_video_1(request):
    return render(request, 'process/video_process_1.html')



def view_completed_isotope(request):
    datas = O_purpose.objects.all()
    return render(request, 'process/view_isotope_process.html',{'datas':datas})





def process_logout(request):
    if 'process' in request.session:
        request.session.pop('process',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/')





def loader(request):
    return render(request, 'process/loader.html')



def redirect1(request):
    return render(request, 'process/redicting.html')

def send_isotope(request,id):
    data = O_purpose.objects.get(id=id)
    data.boolean = True
    data.save()
    messages.info(request,'ISOTOPE DATA SUCCESSFULLY SENT')
    return redirect('/view_o_detail_sent/')


def view_o_detail_sent(request):
    datas = O_purpose.objects.filter(boolean=True)
    return render(request, 'process/view_org_details_forwarded.html',{'datas':datas})

def radioactive(request):
    if request.method == 'POST':
        team = request.POST['team']
        time = request.POST['time']
        result = request.POST['result']
        r_isotope(team=team, time=time, result=result).save()
        messages.info(request,'DETAILS FORWARDED SUCCESSFULLY')
    return render(request,'process/radioactive.html')