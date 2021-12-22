# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ModuleModel(models.Model):
    _name = 'validations_app.module_model'
    _description = 'Module Model'

    name = fields.Char("Module Name", required = True, size = 50, index = True, help = "Name of the current module")
    course = fields.Many2one("validations_app.course_model", "Module Course", help = "Courses with this module")
    validations = fields.One2many("validations_app.validation_model", "module_id", "Module Validations", help = "Students who have validated this module.")
    description = fields.Text("Module Description", help = "I like racoons", size = 200, default = "I like racoons")
    hours = fields.Integer("Module Hours", required = True, help = "Total hours of the current course.")