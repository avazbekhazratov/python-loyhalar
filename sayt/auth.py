from django.shortcuts import render, redirect
from sayt.auth_models import User
from django.contrib.auth import login, logout, authenticate


def sing_in(requests):
    if not requests.user.is_anonymous:
        return redirect('home')

    if requests.POST:
        username = requests.POST.get('username', '')
        pas = requests.POST.get('pass', '')

        user = User.objects.filter(username=username).first()
        if not user:
            return render(requests, 'auth/sign-in.html', {'error': "Bunaqa User yo'q"})

        if not user.check_password(pas):
            return render(requests, 'auth/sign-in.html', {'error': "Parol Xato"})

        login(requests, user)

        return redirect('home')

    return render(requests, 'auth/sign-in.html', {})


def sing_out(requests, conf=None):
    if requests.user.is_anonymous:
        return redirect('login')

    if conf:
        logout(requests)
        return redirect('login')

    return render(requests, 'auth/sign-out.html')


def sing_up(requests):
    if not requests.user.is_anonymous:
        return redirect('home')

    if requests.POST:
        data = requests.POST

        username = data.get('username', '')
        name = data.get('name', '')
        phone = data.get('phone', '')
        pas = data.get('pass', '')
        pas_conf = data.get('pass_conf', '')

        if 'oferta' not in data:
            return render(requests, 'auth/sign-up.html', {'error': "oferta qabul qilinmagan!"})

        if pas != pas_conf:
            return render(requests, 'auth/sign-up.html', {'error': "parollar mos emas"})

        user = User.objects.filter(username=username).first()
        if user:
            return render(requests, 'auth/sign-up.html', {'error': "Bunaqa user bor"})

        user = User.objects.create_user(username=username, password=pas, name=name, phone=phone, oferta=True)

        login(requests, user)
        authenticate(requests)

        return redirect('home')

    return render(requests, 'auth/sign-up.html', {})







