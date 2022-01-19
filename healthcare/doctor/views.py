import datetime
from datetime import date
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Experience
from .serializers import ExperienceSerializer
# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def AddExperience(request):
    data = request.data
    current_user = request.user
    print("data: ", data)

    From = data["From"]
    To = data["To"]

    EmploymentPeriod = None

    if data["CurrentlyWorking"]:
        CurrentlyWorking = True
    else:
        CurrentlyWorking = False


    print("current",data["CurrentlyWorking"])

    if not data["CurrentlyWorking"]:
        FromDateSplit = From.split("-")
        ToDateSplit = To.split("-")

        FromYear = int(FromDateSplit[0])
        FromMonth = int(FromDateSplit[1])
        FromDay = int(FromDateSplit[2])

        ToYear = int(ToDateSplit[0])
        ToMonth = int(ToDateSplit[1])
        ToDay = int(ToDateSplit[2])

        FromDate = date(FromYear, FromMonth, FromDay)
        ToDate = date(ToYear, ToMonth, ToDay)

        NumberOfDays = ToDate - FromDate

        number_of_days = NumberOfDays.days

        years = number_of_days // 365

        months = (number_of_days - years *365) // 30

        if years == 0:
            EmploymentPeriod = str(months) + " Month "
        else:     
            EmploymentPeriod = str(years) + " Years " +  str(months) + " Month "
  
    experience = Experience.objects.create(
                 user = current_user,
                 HospitalName = data['HospitalName'],
                 Designation = data['Designation'],
                 Department = data['Department'],
                 EmploymentPeriod = EmploymentPeriod,
                 CurrentlyWorking = CurrentlyWorking,
                 From = data['From'],
                 To = data['To']
    )

    return Response({'success':'Successfully Added Experience'})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewExperience(request):
    exprience = Experience.objects.all()
    serializer = ExperienceSerializer(exprience, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    