from rest_framework import serializers
from .models import Handover2pm

class Handover2pmSerializer(serializers.ModelSerializer):
	class Meta:
		model = Handover2pm
		fields = '__all__'