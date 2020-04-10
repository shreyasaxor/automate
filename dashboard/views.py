from django.shortcuts import render

# Create your views here.
from django.views import View


class Test(View):
    template_name='Flowchart_.html'

    def get(self,request,*args,**kwargs):

        return render(request,template_name =self.template_name)

test =Test.as_view()