
from django.shortcuts import render

from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
from crm.models import Month,Sales,Enquiry

def index(request):
     return render(request,"index.html")





def population_chart(request):
     labels = []
     data = []

     queryset = Month.objects.values('country__name').annotate(country_population=Sum('population')).order_by(
          '-country_population')
     for entry in queryset:
          labels.append(entry['country__name'])
          data.append(entry['country_population'])

     return JsonResponse(data={
          'labels': labels,
          'data': data,
     })