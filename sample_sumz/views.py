from django.shortcuts import render
from django.views.generic import View
from sample_sumz.services import reading_questions

# Create your views here.


class AddQuestions(View):
    template_name = "sample_sumz.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            questions = reading_questions()
        return render(request,self.template_name)
