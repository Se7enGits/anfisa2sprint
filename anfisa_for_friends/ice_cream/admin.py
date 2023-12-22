from django.contrib import admin

from .models import Category, Topping, Wrapper, IceCream


# Этот вариант сработает для всех моделей приложения.
# Вместо пустого значения в админке будет отображена строка "Не задано".
admin.site.empty_value_display = 'Не задано'


# Так вставка будет столбцами
# class IceCreamInline(admin.StackedInline):
# А так — в строку:
class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 0  # количество отображаемых пустых форм
    # max_num = 5  # максимальное кол-во встроенных форм


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',
    )


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    # Это свойство сработает для всех полей этой модели.
    # Вместо пустого значения будет выводиться строка "Не задано".
    # empty_value_display = 'Не задано'

    # Указываем, для каких связанных моделей нужно включить такой интерфейс:
    filter_horizontal = ('toppings',)


# Регистрируем класс с настройками админки для моделей IceCream и Category:
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
# Регистрируем модели Topping и Wrapper, 
# чтобы ими можно было управлять через админку
# (интерфейс админки для этих моделей останется стандартным):
admin.site.register(Topping)
admin.site.register(Wrapper)
