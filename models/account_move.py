# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
from odoo.tools import float_is_zero, float_compare, float_round


class AccountMove(models.Model):
    _inherit = "account.move"

    sale_order_id = fields.Many2one('sale.order',compute='_compute_sale_order_id')
    date_order = fields.Datetime(string='Order Date',related='sale_order_id.date_order')

    @api.depends('invoice_line_ids.sale_line_ids')
    def _compute_sale_order_id(self):
        for each in self:
            each.sale_order_id = each.invoice_line_ids.mapped("sale_line_ids").mapped("order_id")

