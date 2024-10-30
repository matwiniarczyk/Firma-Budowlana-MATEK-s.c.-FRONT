from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .forms import ContactForm
from .models import ProjectsDone, Services
from .serializers import ProjectsDoneSerializer, ContactFormSerializer, ServiceSerializer

from django.core.mail import send_mail


class HomePageAPIView(APIView):
    def get(self, request):
        data = {"message": "Strona główna z API"}
        return Response(data)


class AboutUsAPIView(APIView):
    def get(self, request):
        data = {"message": "Lorem ipsum"}
        return Response(data)


class ServicesAPIView(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer


class ProjectsDoneListAPIView(generics.ListAPIView):
    queryset = ProjectsDone.objects.all()
    serializer_class = ProjectsDoneSerializer


class ContactFormAPIView(APIView):
    def post(self, request):
        form = ContactForm(request.data)
        if form.is_valid():
            send_mail(
                subject=form.cleaned_data['topic'],
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=[form.cleaned_data['matiwiniar@gmail.com']],
            )
            return Response({"message": "Formularz został wysłany"})
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
