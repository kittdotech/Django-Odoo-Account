from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
import oerplib
# Create your views here.
def index(request):
    return render(request,"oerp_account/page1.html")

def islogin(request):
    #del request.session['odoouser']
    data={}
    if 'odoouser' in request.session:
        data['status']=True
        data['odoousername']=request.session['odoousername']
    else:
        data['status']=False
    return HttpResponse(json.dumps(data), content_type = "application/json")

def odooconnect(request):
    data={}
    print request.GET['odooserver']
    try:
        oerp = oerplib.OERP(server=request.GET['odooserver'],protocol='xmlrpc', port=request.GET['odooport'])
    except:
        data['status']=False

        return HttpResponse(json.dumps(data), content_type = "application/json")
    data['status']=True
    request.session['odooserver']=request.GET['odooserver']
    request.session['odooport']=request.GET['odooport']

    data['dblist']=oerp.db.list()

    return HttpResponse(json.dumps(data), content_type = "application/json")

def odoologin(request):
    data={}
    print request.POST['odoouser']
    try:
        oerp = oerplib.OERP(server=request.session['odooserver'],protocol='xmlrpc', port=request.session['odooport'])
        user = oerp.login(user=request.POST['odoouser'], passwd=request.POST['odoopass'],database=request.POST['odoodb'])
    except:
        data['status']=False

        return HttpResponse(json.dumps(data), content_type = "application/json")
    data['status']=True
    data['odoousername']=user.name
    request.session['odoousername']=user.name
    request.session['odoodb']=request.POST['odoodb']
    request.session['odoouser']=request.POST['odoouser']
    request.session['odoopass']=request.POST['odoopass']


    return HttpResponse(json.dumps(data), content_type = "application/json")


def listaccountcodes(request):
    data={}
    if 'odoouser' in request.session:
        data['list']={}
        data['status']=True
        oerp = oerplib.OERP(server=request.session['odooserver'], database=request.session['odoodb'], protocol='xmlrpc', port=request.session['odooport'])
        user = oerp.login(user=request.session['odoouser'], passwd=request.session['odoopass'])
        account_ids = oerp.search('account.account', [])
        account_det=oerp.browse('account.account',account_ids)
        for rec in account_det:
            data['list'][rec.code]=rec.name
    else:
        data['status']=False
    return HttpResponse(json.dumps(data), content_type = "application/json")

def odooaccnew(request):
    data={}
    if 'odoouser' in request.session:
        data['inttype']={}
        data['status']=True
        oerp = oerplib.OERP(server=request.session['odooserver'], database=request.session['odoodb'], protocol='xmlrpc', port=request.session['odooport'])
        user = oerp.login(user=request.session['odoouser'], passwd=request.session['odoopass'])
        acctype_ids = oerp.search('account.account.type', [])
        acctype_det=oerp.browse('account.account.type',acctype_ids)
        for rec in acctype_det:
            data['inttype'][rec.id]=rec.name
    else:
        data['status']=False
    return HttpResponse(json.dumps(data), content_type = "application/json")



def odoocreatenew(request):
    data={}
    if 'odoouser' in request.session:
        try:
            oerp = oerplib.OERP(server=request.session['odooserver'], database=request.session['odoodb'], protocol='xmlrpc', port=request.session['odooport'])
            user = oerp.login(user=request.session['odoouser'], passwd=request.session['odoopass'])
            account_id = oerp.create('account.account', {'code': request.GET['code'], 'name': request.GET['name'],'type': request.GET['type'],'user_type': request.GET['user_type']})
            data['status']=True
        except Exception,e:
            data['status']=False
            data['details']=str(e)
    else:
        data['status']=False
    return HttpResponse(json.dumps(data), content_type = "application/json")




def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return HttpResponseRedirect("/")
