from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

class FarmListView(ListAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    def get_queryset(self):
        customer_id = self.request.GET.get('customer')
        if customer_id:
            customer = get_object_or_404(Customer, external_id=customer_id)
            return customer.farms.all()
        return Farm.objects.all()


class CustomerListView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer