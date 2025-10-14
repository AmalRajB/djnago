from django.shortcuts import render
def employeefn(request):
    empdir = [
        {'name':'john','jobtitle':'senior','salary':70000,'jobtype':1},
        {'name':'bob','jobtitle':'trainee','salary':25000,'jobtype':1},
        {'name':'max','jobtitle':'senior','salary':60000,'jobtype':1},
        {'name':'eva','jobtitle':'junior','salary':40000,'jobtype':0},
        {'name':'nami','jobtitle':'senior','salary':50000,'jobtype':0},
        {'name':'robin','jobtitle':'trainee','salary':30000,'jobtype':0},
        {'name':'juan','jobtitle':'junior','salary':45000,'jobtype':1},
        {'name':'steve','jobtitle':'senior','salary':80000,'jobtype':1},
        {'name':'sam','jobtitle':'trainee','salary':20000,'jobtype':0},
        {'name':'boby','jobtitle':'senior','salary':50000,'jobtype':1}
    ]
    jobtype = 'FullTime'
    jobtype1 = 'PartTime'
    context = {
        'empdir':empdir,
        'jobtype':jobtype,
        'jobtype1':jobtype1,
    }
    return render(request,'employee.html',context)

def studentfn(request):

    stddir = [
        {'name': 'Amal', 'grade': 'A', 'passed': True},
        {'name': 'Ajay', 'grade': 'E', 'passed': False},
        {'name': 'Manu', 'grade': 'B', 'passed': True},
        {'name': 'Anu', 'grade': 'C', 'passed': True},
        {'name': 'Jithu', 'grade': 'E', 'passed': False},
        {'name': 'Gokul', 'grade': 'A', 'passed': True},
        {'name': 'Arya', 'grade': 'D', 'passed': False},
        {'name': 'Athul', 'grade': 'B', 'passed': True},
    ]
    return render(request,'student.html',{'stddir':stddir})
