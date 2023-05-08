from odoo import models,fields,api

class DrugsPropertyOrders(models.Model):
    _name="drugs.property.orders.lines"
    _description="Order Lines for the orders placed by customers"
    _rec_name = 'order_id'


    order_id=fields.Many2one("drugs.property.orders",required=True)
    drug_id=fields.Many2one("drugs.property",required=True)
    quantity=fields.Integer(required=True)
    price=fields.Float(related="drug_id.selling_price",readonly=True)
    subtotal=fields.Float(compute="_compute_subtotal",store=True)

    @api.depends('quantity','price')
    def _compute_subtotal(self):
        for record in self:
            record.subtotal=record.quantity*record.price

    _sql_constraints=[
        ('quantity_positive','CHECK(quantity>0)','Quantity must be positive.'),
        ('price_non_negative','CHECK(price>=0)','Price must be non negative.'),
    ]        