


from django.urls import path
from online_exam import views


urlpatterns=[
    path('',views.main,name="main"),
    path('logincode',views.logincode,name="logincode"),
    path('studentpost',views.studentpost,name="studentpost"),
    path('viewstud',views.viewstud,name="viewstud"),
    path('staffp',views.staffp,name="staffp"),
    path('viewstaff',views.viewstaff,name="viewstaff"),
    path('postcomplaint',views.postcomplaint,name="postcomplaint"),
    path('viewcomplaint',views.viewcomplaint,name="viewcomplaint"),
    path('postdepartment',views.postdepartment,name="postdepartment"),
    path('postdept', views.postdept, name="postdept"),
    path('viewdept',views.viewdept,name="viewdept"),
    path('postnotification',views.postnotification,name="postnotification"),
    path('viewnotification',views.viewnotification,name="viewnotification"),
    path('postfeedback',views.postfeedback,name="postfeedback"),
    path('viewfeedback',views.viewfeedback,name="viewfeedback"),
    # path('viewsubject',views.viewsubject,name="viewsubject"),
    path('postsubject',views.postsubject,name="postsubject"),
    path('poststudymaterials',views.poststudymaterials,name="poststudymaterials"),
    path('viewstudymaterials',views.viewstudymaterials,name="viewstudymaterials"),
    path('allocatedsub',views.allocatedsub,name="allocatedsub"),
    path('senddoubt',views.senddoubt,name="senddoubt"),
    path('viewdoubt',views.viewdoubt,name="viewdoubt"),
    path('addexam',views.addexam,name="addexam"),
    path('addqpaper',views.addqpaper,name="addqpaper"),
    path('adminpage',views.adminpage,name="adminpage"),
    path('manageexam',views.manageexam,name="manageexam"),
    path('staffs',views.staffs,name="staffs"),
    path('studentpost',views.studentpost,name="studentpost"),
    path('admin',views.admin,name="admin"),
    path('students',views.students,name='students'),
    path('viewstudymaterialsstud',views.viewstudymaterialsstud,name="viewstudymaterialsstud"),
    path('viewallocatedsub',views.viewallocatedsub,name="viewallocatedsub"),
    path('studadd',views.studadd,name="studadd"),
    path('fileuploadmaterial', views.fileuploadmaterial, name="fileuploadmaterial"),
    path('sendnotification',views.sendnotification,name = 'sendnotification'),
    path('reply/<int:id>',views.reply,name = 'reply'),
    # path('replay',views.replay,name = 'replay'),
    path('compreply',views.compreply,name = 'compreply'),
    path('sendcomplaint', views.sendcomplaint, name='sendcomplaint'),
    path('sendfeedback', views.sendfeedback, name='sendfeedback'),
    path('adddoubt', views.adddoubt, name='adddoubt'),
    path('dreply/<int:id>', views.dreply, name='dreply'),
    path('doubtreply', views.doubtreply, name='doubtreply'),
    path('addsubject', views.addsubject, name='addsubject'),
    path('insertsubject', views.insertsubject, name='insertsubject'),
    path('allocatingstaff', views.allocatingstaff, name='allocatingstaff'),
    path('conductexam', views.conductexam, name='conductexam'),
    path('attendexam', views.attendexam, name='attendexam'),
    path('viewstudadmin', views.viewstudadmin, name='viewstudadmin'),
    # path('examterms', views.examterms, name='examterms'),
    path('studentviewnotifi', views.studentviewnotifi, name='studentviewnotifi'),
    path('examsubjectlist', views.examsubjectlist, name='examsubjectlist'),
    path('examsubjectlistsearch', views.examsubjectlistsearch, name='examsubjectlistsearch'),
    path('viewterms/<int:id>', views.viewterms, name='viewterms'),

    path('searchsubject', views.searchsubject, name='searchsubject'),
    path('attendtest', views.attendtest, name='attendtest'),


    path('deletestud/<int:id>',views.deletestud,name = 'deletestud'),
    path('deletestaff/<int:id>',views.deletestaff,name = 'deletestaff'),
    path('deletedepartment/<int:id>',views.deletedepartment,name = 'deletedepartment'),
    path('deletenotification/<int:id>',views.deletenotification,name = 'deletenotification'),
    path('deletesubject/<int:id>',views.deletesubject,name = 'deletesubject'),


    # path('postpqpaper',views.postpqpaper,name="postpqpaper"),
    # path('ViewPQpaper',views.ViewPQpaper,name="ViewPQpaper"),

    path('staffadd',views.staffadd,name="staffadd"),


]