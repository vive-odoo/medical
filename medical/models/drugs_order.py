from odoo import models,fields,api

class DrugsPropertyOrders(models.Model):
    _name="drugs.property.orders"
    _description="Order Placed by customer from the medical"

    cust_id=fields.Many2one("drugs.property.customers",required=True)
    order_date=fields.Date(default=fields.Date.today())
    total_amount=fields.Float(compute="_compute_total_amount", store=True)
    order_lines=fields.One2many("drugs.property.orders.lines","order_id", string="Order Lines")



    @api.depends('order_lines.subtotal')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount=sum(record.order_lines.mapped('subtotal'))