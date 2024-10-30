from rest_framework import serializers

from .forms import ContactForm
from .models import ProjectsDone, Services


class ProjectsDoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsDone
        fields = '__all__'


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model: Services
        fields = '__all__'
