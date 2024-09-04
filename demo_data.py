from enum import Enum
from datetime import time

from .domain import *


class DemoData(Enum):
    SMALL = 'SMALL'
    LARGE = 'LARGE'
    BWI = 'BWI3'


def id_generator():
    current = 0
    while True:
        yield str(current)
        current += 1


def generate_demo_data(demo_data: DemoData) -> Timetable:
    ids = id_generator()
    days = (('MONDAY', 'TUESDAY') if demo_data == DemoData.SMALL
            else ('MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY'))
    if demo_data == DemoData.BWI:
        timeslots = []
        timeslots.append(Timeslot(next(ids), 'MONDAY', time(8, 15), time(9, 45)))
        timeslots.append(Timeslot(next(ids), 'MONDAY', time(10, 0), time(11, 30)))
        timeslots.append(Timeslot(next(ids), 'MONDAY', time(11, 45), time(13, 15)))
        timeslots.append(Timeslot(next(ids), 'MONDAY', time(15, 15), time(16, 45)))
        timeslots.append(Timeslot(next(ids), 'MONDAY', time(17, 0), time(18, 30)))
        timeslots.append(Timeslot(next(ids), 'TUESDAY', time(13, 30),time(16, 45)))
        timeslots.append(Timeslot(next(ids), 'WEDNESDAY', time(8, 15), time(9, 45)))
        timeslots.append(Timeslot(next(ids), 'WEDNESDAY', time(10, 0), time(11, 30)))
        timeslots.append(Timeslot(next(ids), 'WEDNESDAY', time(13, 30), time(16, 45)))
        timeslots.append(Timeslot(next(ids), 'WEDNESDAY', time(17, 0), time(20, 15)))
        timeslots.append(Timeslot(next(ids), 'FRIDAY', time(9, 0), time(13,15)))
    else:
        timeslots = [
            Timeslot(id=next(ids),
                     day_of_week=day,
                     start_time=start,
                     end_time=start.replace(hour=start.hour + 1))
            for day in days
            for start in (time(8, 30), time(9, 30), time(10, 30), time(13, 30), time(14, 30))
        ]

    if demo_data == DemoData.SMALL:
        room_ids = ('A', 'B', 'C')
    elif demo_data == DemoData.BWI:
        room_ids = ('H.1.2', "Online-Veranstaltung", "H.1.6", "I.2.15", "H.1.3", "H.1.7")
    else:
        room_ids = ('A', 'B', 'C', 'D', 'E', 'F')
    rooms = [Room(id=next(ids), name=f'Room {name}') for name in room_ids]

    lessons = []
    if demo_data == DemoData.SMALL:
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physics", teacher="M. Curie", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Chemistry", teacher="M. Curie", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Biology", teacher="C. Darwin", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="History", teacher="I. Jones", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="I. Jones", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="I. Jones", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Spanish", teacher="P. Cruz", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Spanish", teacher="P. Cruz", student_group="9th grade"))
    if demo_data == DemoData.LARGE:
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="ICT", teacher="A. Turing", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physics", teacher="M. Curie", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Geography", teacher="C. Darwin", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Geology", teacher="C. Darwin", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="History", teacher="I. Jones", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="I. Jones", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Drama", teacher="I. Jones", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Art", teacher="S. Dali", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Art", teacher="S. Dali", student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="9th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="10th grade"))
    lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="10th grade"))
    lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="10th grade"))
    lessons.append(Lesson(id=next(ids), subject="Physics", teacher="M. Curie", student_group="10th grade"))
    lessons.append(Lesson(id=next(ids), subject="Chemistry", teacher="M. Curie", student_group="10th grade"))
    lessons.append(Lesson(id=next(ids), subject="French", teacher="M. Curie", student_group="10th grade"))
    lessons.append(Lesson(id=next(ids), subject="Geography", teacher="C. Darwin", student_group="10th grade"))
    lessons.append(Lesson(id=next(ids), subject="History", teacher="I. Jones", student_group="10th grade"))
    lessons.append(Lesson(id=next(ids), subject="English", teacher="P. Cruz", student_group="10th grade"))
    lessons.append(Lesson(id=next(ids), subject="Spanish", teacher="P. Cruz", student_group="10th grade"))
    if demo_data == DemoData.LARGE:
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="ICT", teacher="A. Turing", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physics", teacher="M. Curie", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Biology", teacher="C. Darwin", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Geology", teacher="C. Darwin", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="History", teacher="I. Jones", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="P. Cruz", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="P. Cruz", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Drama", teacher="I. Jones", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Art", teacher="S. Dali", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Art", teacher="S. Dali", student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="10th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="10th grade"))

        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="ICT", teacher="A. Turing", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physics", teacher="M. Curie", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Chemistry", teacher="M. Curie", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="French", teacher="M. Curie", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physics", teacher="M. Curie", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Geography", teacher="C. Darwin", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Biology", teacher="C. Darwin", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Geology", teacher="C. Darwin", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="History", teacher="I. Jones", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="History", teacher="I. Jones", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="P. Cruz", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="P. Cruz", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="P. Cruz", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Spanish", teacher="P. Cruz", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Drama", teacher="P. Cruz", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Art", teacher="S. Dali", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Art", teacher="S. Dali", student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="11th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="11th grade"))

        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Math", teacher="A. Turing", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="ICT", teacher="A. Turing", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physics", teacher="M. Curie", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Chemistry", teacher="M. Curie", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="French", teacher="M. Curie", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physics", teacher="M. Curie", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Geography", teacher="C. Darwin", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Biology", teacher="C. Darwin", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Geology", teacher="C. Darwin", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="History", teacher="I. Jones", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="History", teacher="I. Jones", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="P. Cruz", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="P. Cruz", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="English", teacher="P. Cruz", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Spanish", teacher="P. Cruz", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Drama", teacher="P. Cruz", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Art", teacher="S. Dali", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Art", teacher="S. Dali", student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="12th grade"))
        lessons.append(Lesson(id=next(ids), subject="Physical education", teacher="C. Lewis",
                              student_group="12th grade"))
    if demo_data == DemoData.BWI:
        lessons.append(Lesson(id=next(ids), subject="Softwareentwicklung", teacher="Prof. Dr. Ing. Heß", student_group="BWI 3"))
        lessons.append(Lesson(id=next(ids), subject="Logistik", teacher="Prof. Dr. Liebstückel", student_group="BWI 3"))
        lessons.append(Lesson(id=next(ids), subject="Projektmanagement", teacher="Prof. Dr. Wedlich", student_group="BWI 3"))
        lessons.append(Lesson(id=next(ids), subject="Logistik", teacher="Prof. Dr. Liebstückel", student_group="BWI 3"))
        lessons.append(Lesson(id=next(ids), subject="Übung Programmieren 2", teacher="Zilker", student_group="BWI 3"))
        lessons.append(Lesson(id=next(ids), subject="Datenkommunikation", teacher="Prof. Dr. Bachmeir", student_group="BWI 3"))
        lessons.append(Lesson(id=next(ids), subject="IT-Projektmanagement", teacher="Prof. Dr.-Ing. Heß", student_group="BWI 3"))
        lessons.append(Lesson(id=next(ids), subject="Softwareentwicklung", teacher="Prof. Dr.-Ing. Fertig", student_group="BWI 3"))
        lessons.append(Lesson(id=next(ids), subject="IT-Organisation und IT-Controlling", teacher="Prof. Dr. Saueressig", student_group="BWI 3"))
        lessons.append(Lesson(id=next(ids), subject="Software Industry Education and Economy in India", teacher="Prof. Dr. Mueßig, Prof. Dr. Saueressig"))
        lessons.append(Lesson(id=next(ids), subject="Innovationsmanagement und Unternehmensgründung", teacher="Prof. Dr. Mueßig"))


    return Timetable(id=demo_data.name, timeslots=timeslots, rooms=rooms, lessons=lessons)
