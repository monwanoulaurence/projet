from django.shortcuts import render
from .models import Transaction

def my_view(request):
    # Obtenez l'utilisateur actuellement connecté
    user = request.user

    # Obtenez les transactions de l'utilisateur actuel
    transactions = Transaction.objects.filter(user=user)

    # Passer les transactions au modèle de template
    return render(request, 'user/userdash.html', {'transactions': transactions})
