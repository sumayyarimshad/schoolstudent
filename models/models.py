# -*- coding: utf-8 -*-
from odoo import models, fields, api


class schoolform(models.Model):
    _name = 'schoolform.schoolform'
    _description = 'schoolform.schoolform'

    name = fields.Char('Name')
    id= fields.Char('ID')
    address=fields.Text('Address')
    catogories=fields.Selection([('private','Private'),('public','Public')],'catogory')