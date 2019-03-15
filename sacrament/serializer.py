from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  #text = serializers.SerializerMethodField('get_text')

  #def get_text(self):
  #    return self.first_name 

  class Meta:
    model = Profile
    exclude=[]