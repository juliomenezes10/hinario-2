from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as loginUser

from django.http import HttpResponse
from .forms import HinarioForm
from .models import Ponto, CreateHinario


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, "home.html")
    
    else:
        return redirect("pontos:login")

def createuser(request):
    if request.method == "POST":
        email = request.POST.get("emailCreate")
        senha = request.POST.get("senhaCreate")
        name = request.POST.get("nameCreate")
        userEmail = User.objects.filter(email=email)
        userName = User.objects.filter(username=name)

        if userEmail or userName:
            return HttpResponse("<h1>Já existe um usuario com esse email ou username</h1>")

        else:
            user = User.objects.create_user(name, email, senha)
            user.save()
            return redirect("pontos:login")
    else:
        return render(request, "createuser.html")

def login(request):
    if request.method == "POST": 
        email = request.POST.get("emailLogin")
        senha = request.POST.get("senhaLogin")
        username = User.objects.get(email=email)
        user = authenticate(username=username, password=senha)

        if user is not None:
            loginUser(request, user)
            return redirect("pontos:home")
        
        else:
            return HttpResponse("Conta Invalida")
        
    return render(request, "login.html")

def signout(request):
    logout(request)
    return redirect("pontos:login")

def addpontos(request):
    if request.method == "POST":
        form = HinarioForm(request.POST)
        
        if form.is_valid():
            form.save()

            return redirect("pontos:home")

        else:
            return HttpResponse("Deu error")

    else:
        form = HinarioForm()
        return render(request, "addpontos.html", {"form": form})

def hinarioView(request):
    categorys =  CreateHinario.objects.all()
    

    return render(request, "hinario.html", { "categorys": categorys})
    
    
def pontosView(request, slug_id):
    match slug_id:
        case "hino-da-umbanda":
            pontos = Ponto.objects.filter(category_id=4)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Hino da Umbanda"})
        case "hinos-da-ayahuasca":
            pontos = Ponto.objects.filter(category_id=5)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Hinos da Ayahuasca"})
        case "hinario-do-mestre-irineu":
            pontos = Ponto.objects.filter(category_id=6)


            return render(request, "pontos.html", {"ponto": pontos, "title": "O Cruzeirinho"})
        case "abertura":
            pontos = Ponto.objects.filter(category_id=7)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Abertura"})
        case "saldacao-da-porteira":
            pontos = Ponto.objects.filter(category_id=8)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Saldação da Porteira"})
        case "defumacao":
            pontos = Ponto.objects.filter(category_id=9)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Defumação"})
        case "descarrego":
            pontos = Ponto.objects.filter(category_id=10)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Descarrego"})
        case "encerramento":
            pontos = Ponto.objects.filter(category_id=11)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Encerramento"})
        case "oxala":
            pontos = Ponto.objects.filter(category_id=12)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Oxalá"})
        case "ogum":
            pontos = Ponto.objects.filter(category_id=13)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Ogum"})
        case "omulu-obaluae":
            pontos = Ponto.objects.filter(category_id=14)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Omulu/Obaluaê"})
        case "iemanja":
            pontos = Ponto.objects.filter(category_id=15)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Iemanjá"})
        case "xango":
            pontos = Ponto.objects.filter(category_id=16)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Xangô"})
        case "oxossi":
            pontos = Ponto.objects.filter(category_id=17)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Oxossi"})
        case "oxum":
            pontos = Ponto.objects.filter(category_id=18)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Oxum"})
        case "iansa":
            pontos = Ponto.objects.filter(category_id=19)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Iansã"})
        case "nana-buruque":
            pontos = Ponto.objects.filter(category_id=20)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Nanã Buruque"})
        case "marinheiros-marujos":
            pontos = Ponto.objects.filter(category_id=21)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Marinheiros e Marujos"})
        case "boiaderos":
            pontos = Ponto.objects.filter(category_id=22)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Boiaderos"})

        case "baianos":
            pontos = Ponto.objects.filter(category_id=23)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Bainos"})
        case "pretos-velhos":
            pontos = Ponto.objects.filter(category_id=24)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Pretos Velhos"})
        case "caboclos":
            pontos = Ponto.objects.filter(category_id=25)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Caboclos"})
        case "exus-pomba-giras":
            pontos = Ponto.objects.filter(category_id=26)
            
            return render(request, "pontos.html", {"ponto": pontos, "title": "Exus e Pomba Giras"})
        case "criancas":
            pontos = Ponto.objects.filter(category_id=27)

            return render(request, "pontos.html", {"ponto": pontos, "title": "Crianças"})

    return HttpResponse(f"{slug_id}")