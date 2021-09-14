from odoo import api, fields, models
# This class represents the number customer template where the ttl score should be added


class CustomerScore(models.Model):
    _inherit = "res.partner"

    sales_score = fields.Integer(string="Sales Score", compute="_compute_total_scores")

    def _compute_total_scores(self):
        """Calculates the total score of a customer from his invoices"""
        for rec in self:
            score_count = self.env['account.move'].search([('partner_id', '=', rec.id)])
            total_score = 0
            for score in score_count:
                name = score['name'].split('/')[0]
                if name != "RINV":
                    print(name)
                total_score += score['customer_score']
            rec.sales_score = total_score
