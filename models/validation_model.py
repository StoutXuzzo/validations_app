# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ValidationModel(models.Model):
    _name = 'validations_app.validation_model'
    _description = 'Validation Model'

    date = fields.Date("Validation Date")
    module_id = fields.Many2one("Validation Module")
    course_id = fields.Many2one("Validation course")