from . import models
from openpyxl import Workbook

def createrecord(abcd):
    workbk=Workbook()
    excelsheet=workbk.active

    data=[('Username','First Name','Last Name','Email','Date of Birth')]

    for a in abcd:
        data+=[(a.username,a.first_name,a.last_name,a.email,a.profile.birth_date)]

    for dat in data:
        excelsheet.append(dat)

    workbk.save('userrecord.xlsx')
