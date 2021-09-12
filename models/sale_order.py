from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    product_template_id = fields.Many2one("product.template", string="Product Name")
    product_score_template = fields.Integer(related="product_template_id.product_score", string="Score")

    sub_ttl_score = fields.Integer(string="Sub Score TTL",  compute="_calculate_sub_total")

    @api.depends('product_uom_qty', 'product_score_template')
    def _calculate_sub_total(self):
        """Calculate the subtotal of the score"""
        for record in self:
            subtotal = record.product_score_template * record.product_uom_qty
            record. sub_ttl_score = subtotal


class TotalScore(models.Model):
    _inherit = "sale.order"

    total_score = fields.Integer(string="Total Score", compute="_calculate_total_score")

    @api.depends('order_line.sub_ttl_score')
    def _calculate_total_score(self):
        """Calculates the total of all product scores mentioned in the sales form"""
        for record in self:
            ttl_score = 0
            for line in record.order_line:
                ttl_score += line.sub_ttl_score
            record.total_score = ttl_score



