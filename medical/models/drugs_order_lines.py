from odoo import models,fields

class DrugsPropertyOrders(models.Model):
    _name="drugs.property.orders.lines"
    _description="Order Lines for the orders placed by customers"


    order_id=fields.Many2one("drugs.property.orders",required=True)
    drug_id=fields.Many2one("drugs.property",required=True)
    quantity=fields.Integer(required=True)
    price=fields.Float(related="drug_id.selling_price",readonly=True)
    subtotal=fields.Float()