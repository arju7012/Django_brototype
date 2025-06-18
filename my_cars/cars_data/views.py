from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_cars(request):

    cars = {
        "car_data": [
        {
            "brand": "Toyota",
            "model": "Camry",
            "year": 2023
        },
        {
            "brand": "Honda",
            "model": "Civic",
            "year": 2024
        },
        {
            "brand": "Ford",
            "model": "F-150",
            "year": 2023
        },
        {
            "brand": "BMW",
            "model": "X5",
            "year": 2024
        },
        {
            "brand": "Mercedes-Benz",
            "model": "C-Class",
            "year": 2023
        },
        {
            "brand": "Tesla",
            "model": "Model 3",
            "year": 2024
        },
        {
            "brand": "Audi",
            "model": "A4",
            "year": 2023
        },
        {
            "brand": "Nissan",
            "model": "Rogue",
            "year": 2024
        },
        {
            "brand": "Hyundai",
            "model": "Elantra",
            "year": 2023
        },
        {
            "brand": "Kia",
            "model": "Sportage",
            "year": 2024
        },
        {
            "brand": "Chevrolet",
            "model": "Silverado",
            "year": 2023
        },
        {
            "brand": "Volkswagen",
            "model": "Jetta",
            "year": 2024
        },
        {
            "brand": "Subaru",
            "model": "Outback",
            "year": 2023
        },
        {
            "brand": "Mazda",
            "model": "CX-5",
            "year": 2024
        },
        {
            "brand": "Lexus",
            "model": "RX",
            "year": 2023
        },
        {
            "brand": "Volvo",
            "model": "XC60",
            "year": 2024
        },
        {
            "brand": "Jeep",
            "model": "Wrangler",
            "year": 2023
        },
        {
            "brand": "Porsche",
            "model": "911",
            "year": 2024
        },
        {
            "brand": "Ferrari",
            "model": "Roma",
            "year": 2023
        },
        {
            "brand": "Lamborghini",
            "model": "Huracan",
            "year": 2024
        },
        {
            "brand": "Genesis",
            "model": "GV70",
            "year": 2023
        },
        {
            "brand": "Acura",
            "model": "MDX",
            "year": 2024
        },
        {
            "brand": "Infiniti",
            "model": "QX60",
            "year": 2023
        },
        {
            "brand": "Chrysler",
            "model": "Pacifica",
            "year": 2024
        },
        {
            "brand": "Dodge",
            "model": "Charger",
            "year": 2023
        }
        ]
    }


    return render(request,'index.html', cars)


