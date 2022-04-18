from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=100)    # длина заголовка
    memo = models.TextField(blank=True)         # памятка- запись
    created = models.DateTimeField(auto_now_add=True)   # дата и время создания
    datecompleted = models.DateTimeField(null=True, blank=True) # когда выполнить,
    # blank=True, отображение не обязательно для нашего проекта (не для панели админа) 
    important = models.BooleanField(default=False)  # важность заметки
    user = models.ForeignKey(User, on_delete=models.CASCADE)    # создание пользователя
    
# чтобы вместо номера поста в панели админа было название (из title)
    def __str__(self):
        return self.title
