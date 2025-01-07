from django.contrib import admin
from task1.models import Buyer, Game, News

# Register your models here.
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    list_filter = ('size', 'cost',)
    search_fields = ('title',)
    list_per_page = 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age',)
    list_display = ('name','balance','age',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ('title',)
    search_fields = ('title', 'data')
    list_display = ('title', 'content', 'data')
    list_per_page = 10