from django.urls import path
from .views import list_tarefas, detalhes_tarefas, add_tarefas, edit_tarefas, deletar_tarefa


app_name = "tarefas"

urlpatterns = [
    path('', list_tarefas, name="list"),
    path('<int:tarefa_id>/detalhes/', detalhes_tarefas, name='detalhes'),
    path('inserir/', add_tarefas, name='inserir'),
    path("<int:tarefa_pk>/editar/", edit_tarefas, name="editar"),
    path("<int:tarefa_pk>/deletar", deletar_tarefa, name="delete"),
]
