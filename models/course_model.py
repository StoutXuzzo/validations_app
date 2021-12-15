# -*- coding: utf-8 -*-

from odoo import models, fields, api

#refsh

class CourseModel(models.Model):
    _name = 'validations_app.course_model'
    _description = 'Course Model'

    name = fields.Char("Course Name", required = True)
    description = fields.Text("Course Description")