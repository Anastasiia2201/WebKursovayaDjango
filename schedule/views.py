import os
import datetime

import pdfplumber
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404


from subjects.models import Subject
from .models import Schedule, Group, Teacher
from basa_mtuci.constants import WEEK, TIME

file_path='pdf/BFI2202.pdf'

def create_schedule(group, order, week_type, week_day, subject, classroom, teacher, type, until_week, from_week):
    if subject:
        subject, _ = Subject.objects.get_or_create(name=subject)
        teacher, _ = Teacher.objects.get_or_create(last_name=teacher)
        schedule, _ = Schedule.objects.get_or_create(group=group, order=order, classroom=classroom,
                                                week_day=week_day, week_type=week_type, teacher=teacher,
                                                type=type, until_week=until_week, from_week=from_week)
        schedule.subject = subject
        schedule.save()
        return schedule
    return None

def parse_schedule():
    """Парсер"""
    with pdfplumber.open(file_path) as pdf:
        week_day = None
        text = pdf.pages[0].extract_text()
        group_index = text.find('Группа') + len('Группа') + 1
        group, _ = Group.objects.get_or_create(name=text[group_index:group_index+7])
        schedule_table = pdf.pages[0].extract_tables()
        for row in schedule_table[0][2:]:
            if row[0]:
                week_day = WEEK[row[0]]
            order = row[1]
            teacher_even = row[5]
            teacher_uneven = row[8]
            even_subject = row[6].replace('\n',' ')[:row[6].find('(')]
            uneven_subject = row[7].replace('\n',' ')[:row[7].find('(')]
            classroom_even = row[3]
            classroom_uneven = row[3]
            type_even = row[4]
            type_uneven = row[9]
            until_week = ['','']
            from_week = ['','']
            for i in [0,1]:
                text = row[i+6][row[i+6].find('(') + 1:row[i+6].find(')')]
                if text:
                    if text[0]=='с':
                        index = 1
                        while (text[index+1].isdigit()):
                            from_week[i] += text[index+1]
                            index += 1
                    index = text.find('о') + 2
                    while (text[index].isdigit()):
                        until_week[i] += text[index]
                        index += 1
                    if text[0]=='н':
                        index = 2
                        while (text[index+1].isdigit()):
                            from_week[i] += text[index+1]
                            index += 1
                        until_week[i] = from_week[i]
                if until_week[i] == '':
                    until_week[i] = '17'
                if  from_week[i] == '':
                    from_week[i] = '1'     
            create_schedule(group, order, 'even', week_day, even_subject, classroom_even, teacher_even, type_even, int(until_week[0]), int(from_week[0]))
            create_schedule(group, order, 'uneven', week_day, uneven_subject, classroom_uneven, teacher_uneven, type_uneven, int(until_week[1]), int(from_week[1]))
    return HttpResponse(schedule_table)


def get_schedule(week_day, week):
    week_type='even'
    if week % 2 == 0:
        week_type='uneven'
    day_schedule = Schedule.objects.filter(group__name='БФИ2202', week_type=week_type, week_day=week_day)
    lessons = []
    for i in range(1,6):
        lesson = day_schedule.filter(order=i, until_week__gte=week, from_week__lte=week).first()
        if lesson:
            lessons.append({
                'order': i,
                'time': TIME[i-1],
                'teacher': lesson.teacher.last_name,
                'classroom': lesson.classroom,
                'type': lesson.type,
                'subject': lesson.subject.name})
        else:
            lessons.append({
                'order': i,
                'time': TIME[i-1],
                'subject': ''})
    return lessons


def schedule(request, type):
    """Расписание"""
    # заполнить БД - parse_schedule()
    lessons = {}
    template = 'schedule/schedule.html'
    today = datetime.datetime.now()
    week = today.isocalendar()[1] - datetime.date(2024, 9, 1).isocalendar()[1]
    if type == 'today':
        lessons = get_schedule(today.weekday(), week)
    if type == 'tomorrow':
        lessons = get_schedule((today + datetime.timedelta(days=1)).weekday(), week)
    if type == 'week':
        for i in range(0,6):
            lessons[i] = (get_schedule(i, week))
    if type == 'next_week':
        for i in range(0,6):
            lessons[i] = (get_schedule(i, week + 1))
    context = {'lessons': lessons}

    return render(request, template, context)