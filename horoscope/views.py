from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from collections import namedtuple
from datetime import datetime
from django.shortcuts import render



ZodiacAttribures = namedtuple('ZodiacAttributes', ['response', 'element', 'start_date', 'end_date'])

zodiac = {
    'aries': ZodiacAttribures("[ɛəri:z] Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
                              'Fire',  datetime(year=2024, month=3, day=21), datetime(year=2024, month=4, day=20)),
    'taurus': ZodiacAttribures("['tɔ:rəs] Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
                               'Earth', datetime(year=2024, month=4, day=21), datetime(year=2024, month=5, day=20)),
    'gemini': ZodiacAttribures("['dʒeminai] Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
                               'Air', datetime(year=2024, month=5, day=21), datetime(year=2024, month=6, day=20)),
    'cancer': ZodiacAttribures("['kænsə(r)] Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
                               'Water', datetime(year=2024, month=6, day=21), datetime(year=2024, month=7, day=20)),
    'leo': ZodiacAttribures('[li:əu] Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
                            'Fire',  datetime(year=2024, month=7, day=21), datetime(year=2024, month=8, day=20)),
    'virgo': ZodiacAttribures("['vз:gəu] Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
                              'Earth', datetime(year=2024, month=8, day=21), datetime(year=2024, month=9, day=20)),
    'libra': ZodiacAttribures("['li:brə] Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
                              'Air', datetime(year=2024, month=9, day=21), datetime(year=2024, month=10, day=20)),
    'scorpio': ZodiacAttribures("['skɔ:piəu] Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
                                'Water', datetime(year=2024, month=10, day=21), datetime(year=2024, month=11, day=20)),
    'sagittarius': ZodiacAttribures("[sædʒi'tɛəriəs] Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
                                    'Fire',  datetime(year=2024, month=11, day=21), datetime(year=2024, month=12, day=20)),
    'capricorn': ZodiacAttribures("['kæprikɔ:n] Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
                                  'Earth', datetime(year=2024, month=12, day=21), datetime(year=2024, month=1, day=20)),
    'aquarius': ZodiacAttribures("[ə'kwɛəriəs] Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
                                 'Air', datetime(year=2024, month=1, day=21), datetime(year=2024, month=2, day=20)),
    'pisces': ZodiacAttribures("['paisi:z] Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).",
                               'Water', datetime(year=2024, month=2, day=21), datetime(year=2024, month=3, day=20))
}


def horoscope(request, types=None):
    context = {'zodiacs': zodiac}
    return render(request, 'horoscope/list_of_signs.html', context=context)


def sort_by_type(types, elem):
    shown_list = ''
    for page in list(zodiac.keys()):
        if zodiac[page].element == elem:
            redir = reverse("what_zodiac", args=[page])
            shown_list += f'<li> <a href="{redir}">{page.title()} </a> </li>'
    result = f'''
            <ol>
                {shown_list}
            </ol>
            '''
    return HttpResponse(result)


def by_type(request):
    type_lst = ['Fire', 'Earth', 'Air', 'Water']
    shown_list = ''
    for el in type_lst:
        redir = reverse("sort_by_type", args=[el])
        shown_list += f'<li> <a href="{redir}">{el.title()} </a> </li>'
    result = f'''
            <ol>
                {shown_list}
            </ol>
            '''
    return HttpResponse(result)


def get_zodiac(request, sign: str):
    context = {'response': zodiac.get(sign), 'sign': sign}
    return render(request, 'horoscope/sign_zodiac.html', context=context)


def get_date(request, month, day):
     if month > 12 or day > 31:
         return HttpResponseNotFound("Вы ввели неправильную дату, пожалуйста, попробуйте еще раз.")
     for page in list(zodiac.keys()):
        if zodiac[page].start_date <= datetime(year=2024, month=month, day=day) <= zodiac[page].end_date:
            return HttpResponseRedirect(reverse('what_zodiac', args=[page]))


def enter_date(request):
    return HttpResponseRedirect(reverse('what_date', args=map(int,
    input('Пожалуйста, введите дату в формате: месяц, день через пробел').split())))

def get_by_num(request, num):
    return HttpResponseRedirect(reverse('what_zodiac', args=[list(zodiac.keys())[num - 1]]))