from odoo import api, fields, models


class CustomerInvoice(models.Model):
    _inherit = "account.move"

    customer_score = fields.Integer(string="Customer Score")