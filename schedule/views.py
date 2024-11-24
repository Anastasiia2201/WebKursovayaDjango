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

def create_schedule(group, order, week_type, week_day, subject, classroom, teacher, type):
    if subject:
        subject, _ = Subject.objects.get_or_create(name=subject)
        teacher, _ = Teacher.objects.get_or_create(last_name=teacher)
        schedule, _ = Schedule.objects.get_or_create(group=group, order=order, classroom=classroom,
                                                week_day=week_day, week_type=week_type, teacher=teacher,
                                                type=type)
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
            create_schedule(group, order, 'even', week_day, even_subject, classroom_even, teacher_even, type_even)
            create_schedule(group, order, 'uneven', week_day, uneven_subject, classroom_uneven, teacher_uneven, type_uneven)
    return HttpResponse(schedule_table)



def schedule(request):
    """Расписание"""
    template = 'schedule/schedule.html'
    today = datetime.datetime.now()
    lessons = []
    day = 3
    day_schedule = Schedule.objects.filter(group__name='БФИ2202', week_type='even', week_day=day)
    for i in range(1,6):
        try:
            lesson = day_schedule.filter(order=i).first()
            lessons.append({
                'order': i,
                'time': TIME[i-1],
                'teacher': lesson.teacher.last_name,
                'classroom': lesson.classroom,
                'type': lesson.type,
                'subject': lesson.subject.name})
        except:
            lessons.append({
                'order': i,
                'time': TIME[i-1],
                'subject': ''})
    context = {'lessons': lessons}
    return render(request, template, context)