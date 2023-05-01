from odoo import models,fields

class DrugsPropertyOrders(models.Model):
    _name="drugs.property.orders"
    _description="Order Placed by customer from the medical"

    cust_id=fields.Many2one("drugs.property.customers",required=True)
    order_date=fields.Date(default=fields.Date.today())
    total_amount=fields.Float()