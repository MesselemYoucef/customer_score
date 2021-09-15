from odoo import api, fields, models
# This class represents the number customer template where the ttl score should be added


class CustomerScore(models.Model):
    _inherit = "res.partner"

    sales_score = fields.Integer(string="Sales Score", compute="_compute_total_scores")

    def _compute_total_scores(self):
        """Calculates the total score of a customer from his invoices"""
        for rec in self:
            customer_records = self.env['account.move'].search([('partner_id', '=', rec.id)])
            total_score = 0
            for record in customer_records:
                name = record['name'].split('/')[0]
                print(name)
                if name != '':
                    if name != "RINV":
                        total_score += record['customer_score']
                    else:
                        total_score -= record['customer_score']
            rec.sales_score = total_score
