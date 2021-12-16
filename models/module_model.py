# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ModuleModel(models.Model):
    _name = 'validations_app.module_model'
    _description = 'Module Model'

    name = fields.Char("Module Name", required = True)
    course = fields.Many2one("validations_app.course_model", "Module Course")
    validations = fields.One2many("validations_app.validation_model", "module_id", "Module Validations")
    description = fields.Text("Module Description")
    hours = fields.Integer("Module Hours", required = True)