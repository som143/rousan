from rest_framework import serializers
from .models import Enquiry

class Enquiryserializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        # fields = ('write all the column name what ever required')
        fields = '__all__'
        