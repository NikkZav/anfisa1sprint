def menu_items(request):
    return {
        'menu_items': [
            {'name': 'Главная',
             'url': 'homepage:index',
             'view_name': 'homepage:index'},
            {'name': 'Каталог мороженого',
             'url': 'ice_cream:ice_cream_list',
             'view_name': 'ice_cream:ice_cream_list'},
            {'name': 'О проекте',
             'url': 'about:description',
             'view_name': 'about:description'},
            {'name': 'Классический пломбир',
             'url': 'ice_cream:ice_cream_detail',
             'view_name': 'ice_cream:ice_cream_detail',
             'pk': 1}
        ]
    }
