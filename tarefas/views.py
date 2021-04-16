from django.shortcuts import render, reverse, redirect, get_object_or_404

from .models import Tarefa
from .forms import TarefaForm


def list_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/list.html', {'tarefas': tarefas})


def detalhes_tarefas(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    return render(request, 'tarefas/detalhes.html', {'tarefa': tarefa})


def add_tarefas(request):
    form = TarefaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(reverse("tarefas:list"))

    return render(request, "tarefas/add.html", context={"form": form})


def edit_tarefas(request, tarefa_pk):
    tarefa = get_object_or_404(Tarefa.objects, pk=tarefa_pk)
    form = TarefaForm(request.POST or None, instance=tarefa)

    if form.is_valid():
        form.save()
        return redirect(reverse("tarefas:list"))

    return render(request, "tarefas/edit.html", context={"tarefa": tarefa, "form": form})


def deletar_tarefa(request, tarefa_pk):
    tarefa = get_object_or_404(Tarefa.objects, pk=tarefa_pk)

    tarefa.delete()

    return redirect(reverse("tarefas:list"))
