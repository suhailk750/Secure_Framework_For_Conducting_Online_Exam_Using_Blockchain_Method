from django.db import models

# Create your models here.

class login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class student(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    gender = models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.IntegerField()
    email=models.CharField(max_length=100)

class staff(models.Model):
    lid=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    gender=models.CharField(max_length=100)
    department=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.BigIntegerField()
    email=models.CharField(max_length=100)

class department(models.Model):
    department=models.CharField(max_length=100)


class complaints(models.Model):
    stud_id=models.ForeignKey(student,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)


class notifications(models.Model):
    notification=models.CharField(max_length=100)
    date=models.DateField()

class feedback(models.Model):
    stud_id = models.ForeignKey(student, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)
    date=models.DateField()

class subject(models.Model):
    d_id=models.ForeignKey(department,on_delete=models.CASCADE)
    subject=models.CharField(max_length=100)
    semester=models.CharField(max_length=100)

class study_material(models.Model):
    sub_id=models.ForeignKey(subject,on_delete=models.CASCADE)
    materials=models.CharField(max_length=100)

class result(models.Model):
    stud_id=models.ForeignKey(student,on_delete=models.CASCADE)
    sub_id=models.ForeignKey(subject,on_delete=models.CASCADE)
    mark=models.FloatField()
    date=models.DateField()

class allocated_sub(models.Model):
    staf_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    sub_id=models.ForeignKey(subject,on_delete=models.CASCADE)

class doubt(models.Model):
    staf_id=models.ForeignKey(staff,on_delete=models.CASCADE)
    stud_id=models.ForeignKey(student,on_delete=models.CASCADE)
    doubt=models.CharField(max_length=100)
    date=models.DateField()
    reply=models.CharField(max_length=100)


class exam(models.Model):
    sub_id=models.ForeignKey(subject,on_delete=models.CASCADE)
    question=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)














