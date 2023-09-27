from rest_framework import serializers
# from .models import Company,Employee
from .models import *
# from api.models import *
# Company serializer 
class ComapanySerializer(serializers.HyperlinkedModelSerializer):
    # company_id=serializers.ReadOnlyField()  #you can read only id 
    class Meta:
        model=Company
        fields='__all__'      


#Employee serializer
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField() #if you want to expose id 

    class Meta:
        model=Employee
        fields='__all__'