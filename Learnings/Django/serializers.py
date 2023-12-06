import json
python_dict = {'age':23, 'add':'abcd gaon'}
python_data = {'name':'Dipti', 'rollno':100}
# todo To Convert Python to JSON use dump method
json_data = json.dumps(python_data)
js = json.dumps(python_dict)
print(python_dict)
# todo To Convert JSON to Python Object use loads method
parsed_data = json.loads(json_data)

# ! Serializer
# Serializers are used for converting complex data such as querysets and model instances to native python datatypes 
# ?called (Serialization)
# That can be easily rendered into json, XML or other content types which is understood by FrontEnd
# ? deserailization is also done by serializer which means it allows parsed data to be converted back into complex types.

from rest_framework import serializers

#  StudentSerializer Sub Class h 
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

# models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 100)
    roll = models.IntegerField()
    city = models.CharField(max_length = 100)

# is data ko jo frontend m store h ise json m convert krna h or client ko send krna h
# or agar client se data aa rha h jo k json h use db m store krna h
# Jitni bhi database table m rows ban rhi h wo sab objects hoge
# Complex Data Type --> Python Native Data Type --> Json Data (i.e called serialization)

# Creating Query Set
stu = Student.objects.all()

# Converting Query Set from stu to List of Python Dict/Serializing Query Set
serializer = StudentSerializer(stu, many=True)
print(serializer.data)

# render serialized data into JSON which is understood by frontend (i.e using JSONRender)
# import JSONRenderer
from rest_framework.renderers import JSONRenderer

# Render the data into JSON
json_data = JSONRenderer().render(serializer.data)


# views.py
from django.http import HttpResponse

def student_detail(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu, many=True)
    json_data =  JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')



    

