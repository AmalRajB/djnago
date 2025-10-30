from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template,render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from .forms import cirtificateform
from django.utils.html import strip_tags
from django.core.mail import send_mail
from.models import cirtificate


def formdatafn(request):
    if request.method =='POST':
        form = cirtificateform(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['studentname']
            course = form.cleaned_data['course']
            date = form.cleaned_data['date']
            form.save()
            temp = get_template('stdpdf.html')
            html = temp.render({
                'name':student_name,
                'course':course,
                'date':date
            })
            buffer = BytesIO()
            pisa_status = pisa.CreatePDF(html,dest=buffer)
            if pisa_status.err:
                return HttpResponse('something went wrong try again..')
            else:
                subject = f'Congratulations {student_name}'
                form_email = 'abcinstitute@gmail.com'
                recipient_list = [f'{student_name}@gmail.com']
                html_message = render_to_string('mail.html',{'name':student_name,
                'course':course,
                'date':date})
                plain_message = strip_tags(html_message)
                send_mail(subject,plain_message,form_email,recipient_list,html_message=html_message)
                responce = HttpResponse(buffer.getvalue(),content_type='application/pdf')
                responce['content-Disposition'] = f'attachment; filename = {student_name}.pdf'
                return responce
   
    else:
        form = cirtificateform()
    return render(request,'cirtificateform.html',{'form':form})
        
