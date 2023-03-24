"""MyPage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse
from django.http import HttpResponse

pages_list = {
    'admin': 'http://127.0.0.1:8000/admin/',
    'Главная': 'http://127.0.0.1:8000/',
    'Гороскоп':'http://127.0.0.1:8000/horoscope',
    'Дни недели':'http://127.0.0.1:8000/week',
    'Люди': 'http://127.0.0.1:8000/week/people',
    'Табличка': 'http://127.0.0.1:8000/table'
}

def main(request):
    shown_list = ''
    for page in pages_list:
        shown_list += f'<li> <a href="{pages_list[page]}">{page.title()} </a> </li>'
    result = f'''
        <ol>
            {shown_list}
        </ol>
        '''
    return HttpResponse(result)
    # return HttpResponse('Main page')

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('horoscope/', include('horoscope.urls')),
    path('week/', include('week_days.urls')),
    path('table/', include('table.urls'))
]
