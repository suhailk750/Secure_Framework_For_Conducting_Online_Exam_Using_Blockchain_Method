from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from online_exam.models import *
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def main(request):
    return render(request,"index.html")


def logincode(request):
    uname=request.POST['username']
    pw=request.POST['password']
    try:
        ob=login.objects.get(username=uname,password=pw)
        if ob.type == 'admin':
            request.session['lid'] = ob.id
            ob1=auth.authenticate(username='admin',password='admin')
            auth.login(request,ob1)
            return HttpResponse('''<script>alert("welcome  to adminhome ");window.location='/adminpage'</script>''')
        elif ob.type == 'staff':
            request.session['lid'] = ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            auth.login(request, ob1)
            return HttpResponse('''<script>alert("welcome staff ");window.location='/staffs'</script>''')
        elif ob.type == 'student':
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username='admin', password='admin')
            auth.login(request, ob1)
            return HttpResponse('''<script>alert("welcome student ");window.location='/students'</script>''')
        else:
            return HttpResponse('''<script>alert("invalid ");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("invalid ");window.location='/'</script>''')
@login_required(login_url='/')
def staffp(request):
    return render(request,"staffpost.html")

@login_required(login_url='/')
def viewstaff(request):
    ob = staff.objects.all()
    return render(request,"viewstaff.html",{'val':ob})

@login_required(login_url='/')
def staffadd(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['phone']
    gender = request.POST['gender']
    department = request.POST['department']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']

    ob = login()
    ob.username = username
    ob.password = password
    ob.type = 'staff'
    ob.save()

    sob = staff()
    sob.fname = fname
    sob.lname = lname
    sob.department = department
    sob.phone = phone
    sob.gender = gender
    sob.place = place
    sob.post = post
    sob.pin = pin
    sob.email = email
    sob.lid = ob
    sob.save()

    return HttpResponse('''<script>alert("Registration Successfull");window.location='/viewstaff'</script> ''')


@login_required(login_url='/')
def deletestaff(request,id):
    ob=staff.objects.get(lid__id=id)
    ob.delete()
    ob1=login.objects.get(id=id)
    ob1.delete()
    return HttpResponse('''<script>alert("Delete Successfull");window.location='/staffadd'</script> ''')


@login_required(login_url='/')
def postdepartment(request):
    return render(request,"post department.html")

@login_required(login_url='/')
def postdept(request):
    departments = request.POST['department']

    dob = department()
    dob.department = departments
    dob.save()


    return HttpResponse('''<script>alert("Add Successfull");window.location='/viewdept'</script> ''')

def viewdept(request):
    ob = department.objects.all()
    return render(request,"viewdepartment.html",{'val':ob})


@login_required(login_url='/')
def deletedepartment(request,id):
    ob=department.objects.get(id=id)
    ob.delete()

    return HttpResponse('''<script>alert("Delete Successfull");window.location='/viewdept'</script> ''')


@login_required(login_url='/')
def studentpost(request):
    ob = department.objects.all()
    return render(request,"studentpost.html",{'val':ob})


@login_required(login_url='/')
def studadd(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    phone = request.POST['phone']
    gender = request.POST['gender']
    departments = request.POST['select']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    email = request.POST['email']
    username = request.POST['username']
    password = request.POST['password']
    ob = login()
    ob.username = username
    ob.password = password
    ob.type = 'student'
    ob.save()

    stob = student()
    stob.fname = fname
    stob.lname = lname
    stob.phone = phone
    stob.gender = gender
    stob.dept_id = department.objects.get(id=departments)
    stob.place = place
    stob.post = post
    stob.pin = pin

    stob.email = email
    stob.lid = ob
    stob.save()

    return HttpResponse('''<script>alert("Registration Successfull");window.location='/viewstud'</script> ''')


@login_required(login_url='/')
def deletestud(request,id):
    ob=student.objects.get(lid__id=id)
    ob.delete()
    ob1=login.objects.get(id=id)
    ob1.delete()
    return HttpResponse('''<script>alert("Delete Successfull");window.location='/viewstud'</script> ''')


@login_required(login_url='/')
def viewstud(request):
    ob=student.objects.all()
    return render(request,"viewstudent.html",{'val':ob})


@login_required(login_url='/')
def viewstudadmin(request):
    ob=student.objects.all()
    return render(request, "view stud admin.html", {'val': ob})


@login_required(login_url='/')
def postnotification(request):
    return render(request,"post notification.html")

@login_required(login_url='/')
def viewnotification(request):
    ob = notifications.objects.all()
    return render(request,"viewnotification.html",{'val':ob})

@login_required(login_url='/')
def studentviewnotifi(request):
    ob = notifications.objects.all()
    return render(request,"studentviewnotifi.html",{'val':ob})

@login_required(login_url='/')
def deletenotification(request,id):
    ob=notifications.objects.get(id=id)
    ob.delete()

    return HttpResponse('''<script>alert("Delete Successfull");window.location='/viewnotification'</script> ''')

@login_required(login_url='/')
def sendnotification(request):
    notification = request.POST['notification']


    ob = notifications()
    ob.notification = notification
    ob.date = datetime.today()
    ob.save()


    return HttpResponse('''<script>alert("Add Successfull");window.location='/viewnotification'</script> ''')

@login_required(login_url='/')
def postcomplaint(request):
    return render(request,"Post Complaint.html")

@login_required(login_url='/')
def sendcomplaint(request):
    complaint = request.POST['complaint']

    ob = complaints()
    ob.complaint = complaint
    ob.date = datetime.today()
    ob.reply = "pending"
    ob.stud_id = student.objects.get(lid__id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/postcomplaint'</script> ''')


@login_required(login_url='/')
def viewcomplaint(request):
    ob = complaints.objects.all()
    return render(request,"viewcomplaints.html",{'val':ob})

@login_required(login_url='/')
def reply(request,id):
    request.session['cid'] = id
    return render(request,"Send Doubt Reply.html")

@login_required(login_url='/')
def compreply(request):
    replay = request.POST['textfield']

    ob = complaints.objects.get(id=request.session['cid'])
    ob.reply = replay
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/viewcomplaint'</script> ''')

# def compply(request,id):
#
#     return render(request, "Send doReply.html")

def attendexam(request):


    return render(request, "attend exam.html")


@login_required(login_url='/')
def postfeedback(request):
    return render(request,"postfeedback.html")

@login_required(login_url='/')
def sendfeedback(request):
    feedbacks = request.POST['feedback']

    ob = feedback()
    ob.feedback = feedbacks
    ob.date = datetime.today()
    ob.stud_id = student.objects.get(lid__id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/postfeedback'</script> ''')


@login_required(login_url='/')
def viewfeedback(request):
    ob = feedback.objects.all()
    return render(request,"viewfeedback.html",{'val':ob})


@login_required(login_url='/')
def addfeedback(request):
    feedbacks = request.POST['feedback']

    ob = feedback()
    ob.feedback = feedbacks
    ob.date = datetime.today()
    ob.stud_id = student.objects.get(lid__id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/postfeedback'</script> ''')

@login_required(login_url='/')
def postsubject(request):
    ob = department.objects.all()
    return render(request,"post subject.html",{'val':ob})


@login_required(login_url='/')
def examsubjectlist(request):
    ob = department.objects.all()
    # sob=student.objects.get(lid__id=request.session['lid'])
    # did=sob.dept_id.id
    # ob = exam.objects.filter(sub_id__d_id__id=did)
    # print(ob,"aaaaaaaaaaaaaaa")
    return render(request,"exam subjectlist.html",{'val':ob})


@login_required(login_url='/')
def examsubjectlistsearch(request):
    dept = request.POST['select']
    ob = department.objects.all()
    ob1 = subject.objects.filter(d_id__id=dept)
    return render(request, "exam subjectlist.html", {'val': ob,'val1':ob1})


@login_required(login_url='/')
def searchsubject(request):
    dept=request.POST['select']
    ob = department.objects.all()
    ob1=subject.objects.filter(d_id__id=dept)
    return render(request, "post subject.html", {'val1': ob1,'val':ob})


@login_required(login_url='/')
def insertsubject(request):
    ob = department.objects.all()
    return render(request, "addsubject.html",{'val':ob})


@login_required(login_url='/')
def addsubject(request):
    subjects = request.POST['subject']
    semester = request.POST['semester']
    departments = request.POST['department']

    ob = subject()
    ob.subject = subjects
    ob.semester = semester
    ob.d_id =department.objects.get(id=departments)
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/insertsubject'</script> ''')




@login_required(login_url='/')
def deletesubject(request,id):
    ob=subject.objects.get(id=id)
    ob.delete()

    return HttpResponse('''<script>alert("Delete Successfull");window.location='/addsubject'</script> ''')


@login_required(login_url='/')
def poststudymaterials(request):
    ob=subject.objects.all()
    return render(request,"add study materials.html",{'val':ob})


@login_required(login_url='/')
def viewstudymaterials(request):
    ob=study_material.objects.all()
    return render(request,"View list of Study material.html",{'val':ob})


@login_required(login_url='/')
def fileuploadmaterial(request):
    subjects = request.POST['select']
    materials = request.FILES['file']
    fs=FileSystemStorage()
    fp=fs.save(materials.name,materials)

    ob = study_material()
    ob.sub_id = subject.objects.get(id=subjects)
    ob.materials = fp
    ob.save()

    return HttpResponse('''<script>alert("Upload Successfull");window.location='/viewstudymaterials'</script> ''')

@login_required(login_url='/')
def viewstudymaterialsstud(request):
    ob = study_material.objects.all()
    return render(request,"View Study material stud.html",{'val':ob})

# def downloadstmaterial(request):
#
#
#
#     return HttpResponse('''<script>alert("Download Successfull");window.location='/viewstudymaterialsstud'</script> ''')

@login_required(login_url='/')
def allocatedsub(request):
    ob = subject.objects.all()
    ob1=staff.objects.all()
    return render(request,"allocated subject.html",{'val':ob ,'va':ob1})

@login_required(login_url='/')
def viewallocatedsub(request):
    ob=allocated_sub.objects.filter(staf_id__lid__id=request.session['lid'])

    return render(request,"view allocated subject.html",{'val':ob})


@login_required(login_url='/')
def allocatestaff(request):
    ob=staff.objects.all()
    return render(request,"Send doubt.html",{"val":ob})

@login_required(login_url='/')
def allocatingstaff(request):
    subjects = request.POST['subject']
    staf = request.POST['staff']

    ob = allocated_sub()
    ob.sub_id=subject.objects.get(id=subjects)
    ob.staf_id=staff.objects.get(id=staf)
    ob.save()

    return HttpResponse('''<script>alert("Allocate Successfull");window.location='/allocatedsub'</script> ''')


@login_required(login_url='/')
def senddoubt(request):
    ob=staff.objects.all()
    return render(request,"Send doubt.html",{"val":ob})

@login_required(login_url='/')
def adddoubt(request):
    Doubt = request.POST['doubt']
    sid=request.POST['s']

    ob = doubt()
    ob.doubt = Doubt
    ob.date = datetime.today()
    ob.reply = "pending"
    ob.staf_id = staff.objects.get(id=sid)
    ob.stud_id = student.objects.get(lid__id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/senddoubt'</script> ''')


@login_required(login_url='/')
def viewdoubt(request):
    ob = doubt.objects.filter(staf_id__lid__id=request.session['lid'],reply='pending')
    return render(request,"viewDoubt.html",{'val':ob})

@login_required(login_url='/')
def dreply(request,id):
    request.session['did']=id
    return render(request, "Send doReply.html")

@login_required(login_url='/')
def doubtreply(request):
    reply = request.POST['textfield']

    ob = doubt.objects.get(id=request.session['did'])
    ob.reply=reply
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/viewdoubt'</script> ''')

@login_required(login_url='/')
def addexam(request):
    ob=subject.objects.all()
    return render(request,"add exam.html",{'val':ob})


@login_required(login_url='/')
def conductexam(request):
    subjects = request.POST['subject']
    question = request.POST['question']
    option1 = request.POST['opt1']
    option2 = request.POST['opt2']
    option3= request.POST['opt3']
    option4= request.POST['opt4']
    answer = request.POST['answer']

    ob = exam()
    ob.sub_id = subject.objects.get(id=subjects)
    ob.question = question
    ob.option1=option1
    ob.option2=option2
    ob.option3=option3
    ob.option4=option4
    ob.answer=answer
    ob.save()

    return HttpResponse('''<script>alert("add Successfull");window.location='/addexam'</script> ''')


@login_required(login_url='/')
def addqpaper(request):
    return render(request,"Add Question papper.html")

@login_required(login_url='/')
def adminpage(request):
    return render(request,"adminindex.html")

@login_required(login_url='/')
def manageexam(request):
    return render(request,"Manage exam.html")


@login_required(login_url='/')
def staffs(request):
    return render(request,"staffindex.html")

@login_required(login_url='/')
def students(request):
    return render(request,"user.html")


@login_required(login_url='/')
def admin(request):
    return render(request,"admin page.html")
# def logout(request):
#     return render(request,"login.html")

@login_required(login_url='/')
def viewterms(request,id):

    request.session['eid']=id

    return render(request, "exam terms.html")


@login_required(login_url='/')
def start_test(request):
    id=request.session['eid']
    ob = exam.objects.filter(sub_id__id=id)
    request.session['qno']=0
    # return render(request, "view_exam.html",{'val':ob})
    return render(request, "attend exam.html",{'val':ob[0],"tmark":"0"})



@login_required(login_url='/')
def att_exam1(request):
    print(request.session['qno'],"=================================")
    print(request.session['qno'],"=================================")
    print(request.session['qno'],"=================================")
    print(request.session['qno'],"=================================")
    print(request.session['qno'],"=================================")
    id=request.session['eid']
    ob = exam.objects.filter(sub_id__id=id)

    ans = request.POST['ans']
    radiobutton=request.POST['radiobutton']
    mark = int(request.POST['mark'])
    qid=int(request.session['qno'])+1
    request.session['qno']=qid
    if ans==radiobutton:
        mark=mark+1
    if len(ob)>qid:
        return render(request, "attend exam.html",{'val':ob[qid],"tmark":str(mark)})
    else:
        ob = result()
        ob.sub_id = subject.objects.get(id=id)
        ob.stud_id = student.objects.get(lid__id=request.session['lid'])
        ob.mark = mark
        ob.date = datetime.today()
        ob.save()
        return HttpResponse('''<script>alert("Finish Successfull");window.location='/viewterms'</script> ''')



def attendtest1(request):
    return render(request, "exam.html")
def attendtest(request):
    # id=request.session['eid']
    # ob = exam.objects.filter(sub_id__id=id)
    # request.session['cq']=0

    # if len(ob)>0:
        return render(request,"exam.html")
        # return render(request, "attend exam.html",{'val':ob[0],"mark":"0"})
    # else:
    #     return "No questions"


def nextexam(request):
#     id = request.session['eid']
#     ob = exam.objects.filter(sub_id__id=id)
#     ans=request.POST['ans']
#     id=request.POST['id']
#     radiobutton=request.POST['radiobutton']
#     mark=int(request.POST['mark'])
#     cq=request.session['cq']+1
#
#     if radiobutton==ans:
#         mark=mark+1
#     if len(ob)<cq:
#         request.session['cq']=cq
#         return render(request, "attend exam.html",{'val':ob[cq],"mark":mark})
#     else:
#         return "finish exam"
    return "finish exam"



def logout(request):
    auth.logout(request)
    return  render(request,'index.html')












