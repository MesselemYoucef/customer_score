from odoo import api, fields, models


class CustomerInvoice(models.Model):
    _inherit = "account.move"

    customer_score = fields.Integer(related="invoice_line_ids.sale_line_ids.order_id.total_score", string="Customer Score")