# -*- coding: utf-8 -*-

from odoo import models, fields, api
from secrets import choice
from string import ascii_letters, ascii_uppercase, digits


class StudentModel(models.Model):
    _name = 'validations_app.student_model'
    _description = 'Student Model'

    name = fields.Char("Student Name", required = True)
    password = fields.Char("Student Password", required = True)
    photo = fields.Binary("Student Photo")
    age = fields.Integer("Student Age")
    city = fields.Text("Student City")
    region = fields.Text("Student Region")
    email = fields.Char("Student Email")
    validations = fields.One2many("validations_app.validation_model", "student_id","Student Validations")

    def generatePassword(self):
        caracteres = ascii_letters + ascii_uppercase + digits
        longitud = 8
        self.password = ''.join(choice(caracteres) for caracter in range(longitud))
