from django.core.management.base import BaseCommand
import requests
from farmers.models import Customer, Farm, CustomerFarmLinks


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('start parsing agvend api')
        response = requests.get(
            'http://agvend-static.s3.amazonaws.com/test-data/farms-43fk34-fj50lLq123dkAAoq194mfiqf.json'
        )
        farmers_data = response.json()
        i = 0
        farms_count = len(farmers_data['Farms'])
        for farm in farmers_data['Farms']:
            i += 1
            print(i, 'of', farms_count, end='\r')
            farm_instance, _ = Farm.objects.get_or_create(
                external_id=farm['FarmGUID'],
                name=farm['FarmID'],
                description=farm['Description']
            )
            for customer in farm['FarmSplits']:
                customer_instance, _ = Customer.objects.get_or_create(
                    external_id=customer['GrowerID'],
                    first_name=customer['SplitFirstName'],
                    last_name=customer['SplitLastName']
                )
                CustomerFarmLinks.objects.get_or_create(
                    customer=customer_instance,
                    farm=farm_instance
                )
