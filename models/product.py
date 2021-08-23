from odoo import api, fields, models

# Class for the product template where each product has its own score


class ProductScore(models.Model):

    _inherit = "product.template"

    product_score = fields.Integer(string="Product Score")

