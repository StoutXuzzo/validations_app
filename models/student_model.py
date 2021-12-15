# -*- coding: utf-8 -*-

from odoo import models, fields, api


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