from ast import Str
from django.core.management.base import BaseCommand
from octopus.core.models import Data

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('first', type=str, help= 'complete Path for D0010 File in your local computer')
        parser.add_argument('--option1', type=int, help='number of records, minimum number of record is 20 by default')

    def handle(self, *args, **options):
        print('Command: mycommand')
        print(f'First: {options["first"]}')
        print(f'Option1: {options["option1"]}')

        file1 = open(options["first"], 'r')
        Lines = file1.readlines() 

        count = 0
        numOfRecords = options["option1"] if options["option1"] > 20 else 20 
        data = Data.objects.all()
        data.delete()
        
        for line in Lines:
            count += 1
            if count > numOfRecords :
                break
            else:
                print(f'Record{count} {line}')
                # data.delete()
                data = Data(
                    meterPoint=line,
                    meter =line,
                )

                data.save()

        self.stdout.write(self.style.SUCCESS(f'{numOfRecords if options["option1"] < 20 else count } Records saved in data base'))

        if options["option1"] < 20:
            self.stdout.write(self.style.WARNING('Showing 20 records. The number of records requested was less than 20'))