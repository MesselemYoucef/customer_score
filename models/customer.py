from odoo import api, fields, models
# This class represents the number customer template where the ttl score should be added


class CustomerScore(models.Model):
    _inherit = "res.partner"

    sales_score = fields.Integer(string="Sales Score")
