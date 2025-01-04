from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)  # Имя покупателя (username аккаунта)
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.IntegerField()  # Возраст

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов игры
    description = models.TextField()  # Описание
    age_limited = models.BooleanField(default=False)  # Ограничение по возрасту 18+
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели, обладающие этой игрой

    def __str__(self):
        return self.title