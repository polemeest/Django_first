from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .lists_of_data import people_data, people_dict

days_dict = {
    'monday': HttpResponse("На понедельник запланирован поход"),
    'tuesday': HttpResponse("На вторник ничего не запланировано"),
    'wednesday': HttpResponse("На среду ничего не запланировано"),
    'thirsday': HttpResponse("На четверг ничего не запланировано"),
    'friday': HttpResponse("На пятницу ничего не запланировано"),
    'saturday': HttpResponse("На субботу ничего не запланировано"),
    'sunday': HttpResponse("На воскресенье ничего не запланировано")
}


def main(request):
    shown_list = ''
    for page in days_dict:
        redir = reverse("what_day", args=[page])
        shown_list += f'<li> <a href="{redir}">{page.title()} </a> </li>'
    context = {"result" : shown_list}
    return render(request, 'week_days/greetings_page.html', context=context)



def week_day(request, day: str):
    return days_dict.get(str(day).lower(), HttpResponseNotFound(f'Дня "{day}" не существует'))


def week_day_by_number(request, day: int):
    try:
        return HttpResponseRedirect(reverse("what_day", args=[list(days_dict)[day - 1]]))
    except IndexError:
        return HttpResponseNotFound(f'Дня под номером {day} не существует. В неделе только 7 дней')

# return (HttpResponse(f"Сегодня {day} день недели"), HttpResponse(f'Неверный номер дня - {day}'))[day > 7]


def people(request):
    list_for_render = {'lst': people_dict}
    return render(request, 'week_days/list_of_people.html', context=list_for_render)
