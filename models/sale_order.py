from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    product_template_id = fields.Many2one("product.template", string="Product Name")
    product_score_template = fields.Integer(related="product_template_id.product_score", string="Score")

    sub_ttl_score = fields.Integer(string="Sub Score TTL",  compute="_calculate_sub_total")

    @api.depends('product_uom_qty')
    def _calculate_sub_total(self):
        """Calculate the subtotal of the score"""
        for record in self:
            subtotal = self.product_score_template * self.product_uom_qty
            record. sub_ttl_score = subtotal


class TotalScore(models.Model):
    _inherit = "sale.order"

    total_score = fields.Integer(string="Total Score", compute="_calculate_total_score")

    @api.depends('order_line.sub_ttl_score')
    def _calculate_total_score(self):
        ttl_score = 0
        print(self.order_line)
        for line in self.order_line.sub_ttl_score:
            ttl_score += line
        print(ttl_score)




