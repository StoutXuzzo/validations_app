# -*- coding: utf-8 -*-

from odoo import models, fields, api
from secrets import choice
from string import ascii_letters, ascii_uppercase, digits


class TeacherModel(models.Model):
    _name = 'validations_app.teacher_model'
    _description = 'Teacher Model'

    name = fields.Char("Teacher Name", required = True)
    surname = fields.Char("Teacher Surname", required = True)
    photo = fields.Binary("Teacher Photo")
    dni = fields.Char("Teacher DNI", required = True)
    
    students = fields.Many2many("validations_app.student_model", String = "Students")
