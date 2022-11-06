from django.shortcuts import render, redirect
from funcionario.forms import ColaboradorForm
from funcionario.models import Colaborador

def emp(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = ColaboradorForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    data = {}
    data['colaboradores'] = Colaborador.objects.all()
    return render(request, 'show.html', data)



def edit(request, id):
    data = {}
    data['db'] = Colaborador.objects.get(id=id)
    data['form'] = ColaboradorForm(instance=data['db'])
    return render(request, 'index.html', data)



def update(request, id):
   data = {}
   data['db'] = Colaborador.objects.get(id=id)
   form = ColaboradorForm(request.POST or None, instance=data['db'])
   if form.is_valid():
       form.save()
       return redirect('/')



def delete(request, id):
    colaborador = Colaborador.objects.get(id=id)
    colaborador.delete()
    return redirect('/')


