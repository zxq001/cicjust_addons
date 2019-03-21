# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BillCount(models.Model):
    _name = 'bill.count'
    _description = "出账单"

    name = fields.Char(string="Title",required=True)
    is_done = fields.Boolean('啥情况？')
# value = fields.Integer()
# value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100