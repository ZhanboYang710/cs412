from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

import random, time

# Create your views here.

menu = [
    "Tomato soup and ketchup",
    "Spicy shawarma with pineapple",
    "Bread with mysterious sauce"
]

length = len(menu)

def main(request):
    template_name = "restaurant/main.html"

    return render(request, template_name)


def order(request):
    template_name = "restaurant/order.html"

    random_num = random.randint(0,length-1)

    context = {
        "todayspecial" : menu[random_num]    
    }
    
    return render(request, template_name, context)


def confirmation(request):
    template_name = "restaurant/confirmation.html"

    print(request)

    total = 0

    ingredients = []

    if (request.POST):
        print(request.POST)

        name = request.POST.get("your_name", None)
        orderSpecial = request.POST.get("order_special", None)
        shawarma_choice = request.POST.get("shawarma", None)
        meat = ""
        pickle = request.POST.get("add_pickle", None)
        onion = request.POST.get("add_onion", None)
        lettuce = request.POST.get("add_lettuce", None)
        flavor = request.POST.get("flavor", None)
        instruction = request.POST.get("spec_intru", None)

        delivery_time = random.randint(30, 60)
        current_time = time.ctime()

        if orderSpecial == "yes":
            special = True
            total += 12
        else:
            special = False

        if shawarma_choice == "chicken shawarma":
            total += 5
            meat = "chicken"
        elif shawarma_choice == "beef shawarma":
            total += 6
            meat = "beef"
        elif shawarma_choice == "fish shawarma":
            total += 7
            meat = "fish"
        else:
            meat = None

        if pickle:
            ingredients.append(pickle)
            total += 1
        if onion:
            ingredients.append(onion)
            total += 1
        if lettuce:
            ingredients.append(lettuce)
            total += 1

        context = {
            'name' : name,
            'order_today_special' : special,
            'meat_choice': meat,
            'ingredients': ingredients,
            'flavor': flavor,
            'intruction': instruction,
            'price': total,
            'time': current_time,
            'delivery_time': delivery_time,
        }


        return render(request, template_name, context)

    return redirect("main")