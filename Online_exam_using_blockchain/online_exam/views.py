from datetime import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from online_exam.models import *
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def main(request):
    return render(request,"login.html")


def logincode(request):
    uname=request.POST['username']
    pw=request.POST['password']
    try:
        ob=login.objects.get(username=uname,password=pw)
        if ob.type == 'admin':
            return HttpResponse('''<script>alert("welcome  to adminhome ");window.location='/adminpage'</script>''')
        elif ob.type == 'staff':
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert("welcome staff ");window.location='/staffs'</script>''')
        elif ob.type == 'student':
            request.session['lid']=ob.id
            return HttpResponse('''<script>alert("welcome student ");window.location='/students'</script>''')
        else:
            return HttpResponse('''<script>alert("invalid ");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("invalid ");window.location='/'</script>''')

def staffp(request):
    return render(request,"staffpost.html")

def viewstaff(request):
    ob = staff.objects.all()
    return render(request,"viewstaff.html",{'val':ob})

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
    sob.finame = fname
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


def deletestaff(request,id):
    ob=staff.objects.get(lid__id=id)
    ob.delete()
    ob1=login.objects.get(id=id)
    ob1.delete()
    return HttpResponse('''<script>alert("Delete Successfull");window.location='/staffadd'</script> ''')


def postdepartment(request):
    return render(request,"post department.html")

def postdept(request):
    departments = request.POST['department']

    dob = department()
    dob.department = departments
    dob.save()


    return HttpResponse('''<script>alert("Add Successfull");window.location='/viewdept'</script> ''')

def viewdept(request):
    ob = department.objects.all()
    return render(request,"viewdepartment.html",{'val':ob})

def deletedepartment(request,id):
    ob=department.objects.get(id=id)
    ob.delete()

    return HttpResponse('''<script>alert("Delete Successfull");window.location='/viewdept'</script> ''')

def studentpost(request):
    return render(request,"studentpost.html")

def studadd(request):
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
    ob.type = 'student'
    ob.save()

    stob = student()
    stob.fname = fname
    stob.lname = lname
    stob.phone = phone
    stob.gender = gender
    stob.department = department
    stob.place = place
    stob.post = post
    stob.pin = pin

    stob.email = email
    stob.lid = ob
    stob.save()

    return HttpResponse('''<script>alert("Registration Successfull");window.location='/viewstud'</script> ''')


def deletestud(request,id):
    ob=student.objects.get(lid__id=id)
    ob.delete()
    ob1=login.objects.get(id=id)
    ob1.delete()
    return HttpResponse('''<script>alert("Delete Successfull");window.location='/viewstud'</script> ''')

def viewstud(request):
    ob=student.objects.all()
    return render(request,"viewstudent.html",{'val':ob})


def postnotification(request):
    return render(request,"post notification.html")

def viewnotification(request):
    ob = notifications.objects.all()
    return render(request,"viewnotification.html",{'val':ob})

def deletenotification(request,id):
    ob=notifications.objects.get(id=id)
    ob.delete()

    return HttpResponse('''<script>alert("Delete Successfull");window.location='/viewnotification'</script> ''')


def sendnotification(request):
    notification = request.POST['notification']


    ob = notifications()
    ob.notification = notification
    ob.date = datetime.today()
    ob.save()


    return HttpResponse('''<script>alert("Add Successfull");window.location='/viewnotification'</script> ''')


def postcomplaint(request):
    return render(request,"Post Complaint.html")

def sendcomplaint(request):
    complaint = request.POST['complaint']

    ob = complaints()
    ob.complaint = complaint
    ob.date = datetime.today()
    ob.reply = "pending"
    ob.stud_id = student.objects.get(lid__id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/postcomplaint'</script> ''')

def viewcomplaint(request):
    ob = complaints.objects.all()
    return render(request,"viewcomplaints.html",{'val':ob})

def reply(request):
    request.session['cid'] = id

    return render(request,"Send Doubt Reply.html")

def compreply(request):

    reply = request.POST['reply']

    ob = complaints.objects.get(id=request.session['cid'])
    ob.reply = reply
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/postcomplaint'</script> ''')

# def compply(request,id):
#
#     return render(request, "Send doReply.html")

def attendexam(request):


    return render(request, "attend exam.html")


def postfeedback(request):
    return render(request,"postfeedback.html")

def sendfeedback(request):
    feedbacks = request.POST['feedback']

    ob = feedback()
    ob.feedback = feedbacks
    ob.date = datetime.today()
    ob.stud_id = student.objects.get(lid__id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/postfeedback'</script> ''')

def viewfeedback(request):
    ob = feedback.objects.all()
    return render(request,"viewfeedback.html",{'val':ob})



def addfeedback(request):
    feedbacks = request.POST['feedback']

    ob = feedback()
    ob.feedback = feedbacks
    ob.date = datetime.today()
    ob.stud_id = student.objects.get(lid__id=request.session['lid'])
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/postfeedback'</script> ''')

def postsubject(request):
    ob = department.objects.all()
    return render(request,"post subject.html",{'val':ob})



def searchsubject(request):
    dept=request.POST['select']
    ob = department.objects.all()
    ob1=subject.objects.filter(d_id__id=dept)
    return render(request, "post subject.html", {'val1': ob1,'val':ob})


def insertsubject(request):
    ob = department.objects.all()
    return render(request, "addsubject.html",{'val':ob})

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





def deletesubject(request,id):
    ob=subject.objects.get(id=id)
    ob.delete()

    return HttpResponse('''<script>alert("Delete Successfull");window.location='/addsubject'</script> ''')



def poststudymaterials(request):
    ob=subject.objects.all()
    return render(request,"add study materials.html",{'val':ob})



def viewstudymaterials(request):
    ob=study_material.objects.all()
    return render(request,"View list of Study material.html",{'val':ob})


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


def viewstudymaterialsstud(request):
    ob = study_material.objects.all()
    return render(request,"View Study material stud.html",{'val':ob})


def allocatedsub(request):
    ob = subject.objects.all()
    ob1=staff.objects.all()
    return render(request,"allocated subject.html",{'val':ob ,'va':ob1})

def viewallocatedsub(request):

    return render(request,"view allocated subject.html")

def allocatestaff(request):
    ob=staff.objects.all()
    return render(request,"Send doubt.html",{"val":ob})

def allocatingstaff(request):
    subjects = request.POST['subject']
    staf = request.POST['staff']

    ob = allocated_sub()
    ob.sub_id=subject.objects.get(id=subjects)
    ob.staf_id=staff.objects.get(id=staf)
    ob.save()

    return HttpResponse('''<script>alert("Allocate Successfull");window.location='/allocatedsub'</script> ''')



def senddoubt(request):
    ob=staff.objects.all()
    return render(request,"Send doubt.html",{"val":ob})


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

def viewdoubt(request):
    ob = doubt.objects.filter(staf_id__lid__id=request.session['lid'],reply='pending')
    return render(request,"viewDoubt.html",{'val':ob})
def dreply(request,id):
    request.session['did']=id
    return render(request, "Send doReply.html")


def doubtreply(request):
    reply = request.POST['textfield']

    ob = doubt.objects.get(id=request.session['did'])
    ob.reply=reply
    ob.save()

    return HttpResponse('''<script>alert("send Successfull");window.location='/viewdoubt'</script> ''')


def addexam(request):
    ob=subject.objects.all()
    return render(request,"add exam.html",{'val':ob})

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

def addqpaper(request):
    return render(request,"Add Question papper.html")

def adminpage(request):
    return render(request,"admin page.html")

def manageexam(request):
    return render(request,"Manage exam.html")

def staffs(request):
    return render(request,"staffpage.html")

def students(request):
    return render(request,"studentpage.html")

def admin(request):
    return render(request,"admin page.html")









