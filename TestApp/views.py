from django.shortcuts import render
from . import forms
# Create your views here.
def thankyouview(request):
    return render(request,'testApp/thankyou.html')

def feedbackview(request):
    form=forms.FeedbackForm()
    if request.method=='POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            print('Form Validation Success and Printing Information')
            print('Name:',form.cleaned_data['name'])
            print('Roll No:',form.cleaned_data['rollno'])
            print('EMail:',form.cleaned_data['email'])
            print('Feedback:',form.cleaned_data['feedback'])
            return thankyouview(request)
    return render(request,'testApp/feedback.html',{'form':form})
