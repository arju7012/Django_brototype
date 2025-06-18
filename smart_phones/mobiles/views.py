from django.shortcuts import render


# Create your views here.

def show_mobile(request):
    mobiles = {
    "mobile_data": [
        {
            "brand": "Apple",
            "model": "iPhone 15 Pro Max",
            "year": 2023
        },
        {
            "brand": "Samsung",
            "model": "Galaxy S24 Ultra",
            "year": 2024
        },
        {
            "brand": "Google",
            "model": "Pixel 8 Pro",
            "year": 2023
        },
        {
            "brand": "OnePlus",
            "model": "12",
            "year": 2024
        },
        {
            "brand": "Xiaomi",
            "model": "14 Ultra",
            "year": 2024
        },
        {
            "brand": "Oppo",
            "model": "Find X7 Ultra",
            "year": 2024
        },
        {
            "brand": "Vivo",
            "model": "X100 Pro",
            "year": 2023
        },
        {
            "brand": "Realme",
            "model": "GT 5 Pro",
            "year": 2023
        },
        {
            "brand": "Honor",
            "model": "Magic6 Pro",
            "year": 2024
        },
        {
            "brand": "Sony",
            "model": "Xperia 1 VI",
            "year": 2024
        },
        {
            "brand": "Motorola",
            "model": "Edge 50 Ultra",
            "year": 2024
        },
        {
            "brand": "Asus",
            "model": "ROG Phone 8 Pro",
            "year": 2024
        },
        {
            "brand": "Nokia",
            "model": "X21 5G",
            "year": 2022
        },
        {
            "brand": "Lenovo",
            "model": "Legion Y70",
            "year": 2022
        },
        {
            "brand": "Huawei",
            "model": "P60 Pro",
            "year": 2023
        },
        {
            "brand": "Infinix",
            "model": "Note 40 Pro+",
            "year": 2024
        },
        {
            "brand": "Tecno",
            "model": "Camon 30 Pro",
            "year": 2024
        },
        {
            "brand": "Nothing",
            "model": "Phone (2)",
            "year": 2023
        },
        {
            "brand": "Fairphone",
            "model": "5",
            "year": 2023
        },
        {
            "brand": "ZTE",
            "model": "Axon 60 Ultra",
            "year": 2024
        },
        {
            "brand": "Redmi",
            "model": "Note 13 Pro+",
            "year": 2024
        },
        {
            "brand": "POCO",
            "model": "X6 Pro",
            "year": 2024
        },
        {
            "brand": "iQOO",
            "model": "12 Pro",
            "year": 2023
        },
        {
            "brand": "BlackBerry",
            "model": "Key2 LE",
            "year": 2018
        },
        {
            "brand": "LG",
            "model": "Velvet",
            "year": 2020
        }
    ]
}


    return render(request, 'index.html', mobiles)