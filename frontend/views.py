from django.shortcuts import render
from django.views.generic import View
from .models import *
from django.conf import settings
from .forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

class IndexView(View):
    template_name = 'frontend/index.html'
    def get(self, request):
        return render(request, self.template_name)
class AdmissionView(View):
    template_name = 'frontend/admission.html'
    def get(self, request):

        return render(request, self.template_name)

class GalleryView(View):
    template_name = 'frontend/gallery.html'
    def get(self, request):
        gallery = GalleryModel.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(gallery, 6)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        return render(request, self.template_name,{'data':data})


class AchivementsView(View):
    template_name = 'frontend/achivements.html'
    def get(self, request):
        achievment = AchievmentModel.objects.all()
        return render(request, self.template_name,{'data':achievment})

class AboutView(View):
    template_name = 'frontend/about.html'
    def get(self, request):
        return render(request, self.template_name)

class HistoryView(View):
    template_name = 'frontend/history.html'
    def get(self, request):
        return render(request, self.template_name)

class CareerView(View):
    template_name = 'frontend/career.html'
    def get(self, request):
        return render(request, self.template_name)

class ContactView(View):
    template_name = 'frontend/contact.html'
    
    def get(self, request):
        form = ContactForm() 
        return render(request, self.template_name, {'form':form})
'''
    def post(self, request):
        form = ContactForm()
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            subject = 'mysite.com'
            message = '%s %s' %(comment, name)
            from_email = form.cleaned_data['email']
            emailTo = [settings.EMAIL_HOST_USER]
            try:
                send_mail(subject, message, from_email, emailTo, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
        return render(request, self.template_name, {'form': form})
'''
class ContactView(View):
    template_name = 'frontend/contact.html'
    
    def get(self, request):
        form = ContactForm() 
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
        return render(request, self.template_name, {'form': form})
class SuccessView(View):
    def get(self, request):
        return HttpResponse('Success! Thank you for your message.')
