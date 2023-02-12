from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleScope, Tag





class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        activated_checkboxes = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                activated_checkboxes += 1
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        if activated_checkboxes == 0:
            raise ValidationError('Укажите основной раздел')
        if activated_checkboxes > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода



class RelationshipInline(admin.TabularInline):
    model = ArticleScope
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass





