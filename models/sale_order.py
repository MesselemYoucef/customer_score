from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    product_template_id = fields.Many2one("product.template", string="Product Name")

    product_score_template = fields.Integer(related="product_template_id.product_score", string="Score")
