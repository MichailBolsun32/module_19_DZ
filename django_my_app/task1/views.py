from django.shortcuts import render
from task1.forms import ContactForm
from task1.models import Buyer, Game
# Create your views here.

# вспомогательная ф-ция для создания списка меню
# используем список т.к. Django не поддерживает dict.items(), для итерации словаря
def get_menu():
    return [
        ['/platform/', 'Главная'],
        ['/platform/games/', 'Магазин'],
        ['/platform/cart/', 'Корзина'],
    ]

# Create your views here.

def func_start(request):
    return render(request, 'task1/start.html')


def func_platform(request):
    menu = get_menu()

    text_pagename = 'Главная страница'
    text_title = 'Главная страница'

    context = {
        'menu': menu,
        'text_pagename': text_pagename,
        'text_title': text_title,
    }
    return render(request,'task1/menu.html', context)

def func_games(request):
#    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2', ]
    games = Game.objects.all()
    #games_title = [game.title for game in games_]

    text_button_1 = 'Купить'
    text_button_2 = 'Вернуться обратно'
    text_pagename = 'Игры'
    text_title = 'Магазин'
    text_href = '/platform/'

    menu = get_menu()

    context = {
        'games': games,
        'text_button_1': text_button_1,
        'text_button_2': text_button_2,
        'text_pagename': text_pagename,
        'text_title': text_title,
        'text_href': text_href,
        'menu': menu,
    }
    return render(request, 'task1/games.html', context)

def func_cart(request):
    text_button_1 = 'Вернуться обратно'
    text_pagename = 'Корзина'
    text_title = 'Корзина'
    text_content = 'Извените, ваша корзина пуста'
    text_href = '/platform/'

    menu = get_menu()

    context = {
        'text_button_1': text_button_1,
        'text_pagename': text_pagename,
        'text_title': text_title,
        'text_content': text_content,
        'text_href': text_href,
        'menu': menu,
    }
    return render(request, 'task1/cart.html', context)

users_buyer = Buyer.objects.all()
users = [user.name for user in users_buyer]

def sign_up_by_django(request): # предситавление формы через файл - forms.py
    # users_buyer = Buyer.objects.all()
    # users = [user.name for user in users_buyer]

    if request.method == "POST":
       # Получаем данные
       form = ContactForm(request.POST)
       info = {'form': form}
       if form.is_valid():
           # Обработка данных формы
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           repeat_password = form.cleaned_data['repeat_password']
           age = form.cleaned_data['age']
           # дальнейшая логика, например отправка email

           if password != repeat_password:
               info['error'] = 'Пароли не совпадают'

           #убрали условие по условию задания
           # if int(age) < 18:
           #     info['error'] = 'Вы должны быть старше 18'

           if username in users:
               info['error'] = 'Пользователь уже существует'

           if len(info) == 1:
               info['username'] = f'Приветствуем, {username}!'
               users.append(username)
               Buyer.objects.create(name=username, age=age)
    else:
        form = ContactForm()
        info = {'form': form}

    return render(request, 'task1/registration_page_py.html', info)