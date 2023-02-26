from django.contrib import admin
from django.http import HttpResponse
import datetime

@admin.action(description = 'В наличии')
def on_sale(self, request, queryset):
    queryset.update(status = 1)
    self.message_user(request, 'Действие выполнено')


@admin.action(description='Снять с продажи')
def status_not_available(self, request, queryset):
    queryset.update(status = 2)
    self.message_user(request, 'Действие выполнено')


@admin.action(description = 'Нету в наличии')
def not_available(self, request, queryset):
    queryset.update(status = 3)
    self.message_user(request, 'Действие выполнено')


@admin.action(description = 'выгрузка данных в формате .csv')
def export_as_csv(self, request, queryset):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv;'.format(datetime.datetime.now())
    response.write(u'\ufeff'.encode('utf8')) #обязательный элемент для корректной выгрузки в utf8
    writer = csv.writer(response)
    writer.writerow(['name', 'slug', 'pub_date', 'release_date', 'price', 'category', 'gameDev', 'status', 'description'])
    for i in queryset:
        writer.writerow([i.name, i.slug, i.pub_date, i.release_date, i.price, i.category, i.gameDev, i.status, i.description])
    return response