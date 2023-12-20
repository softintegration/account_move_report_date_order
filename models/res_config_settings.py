# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    display_only_date_in_date_order = fields.Boolean(string="Display Order date in Date only format")

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        display_only_date_in_date_order = params.get_param('display_only_date_in_date_order',
                                                 default=False)
        res.update(display_only_date_in_date_order=display_only_date_in_date_order)
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param(
            "display_only_date_in_date_order", self.display_only_date_in_date_order)

