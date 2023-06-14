from odoo import models,fields

class DrugsPropertyCustomer(models.Model):
    _name="drugs.property.customers"
    _description="customer who purchase medicines from the medical shop"

    name=fields.Char(required=True)
    address=fields.Text()
    email=fields.Char()
    phone=fields.Char()
    cust_id=fields.Integer(required=True)
    # cust_id=fields.Many2one(
    #     "res.users", default=lambda self: self.env.user)
    # order_lines=fields.One2many("drugs.property.orders.lines","order_id",string="Order Lines",readonly=True)
    order_ids=fields.One2many("drugs.property.orders","cust_id",string='Orders',readonly=True)
    _sql_constraints=[('phone_unique','UNIQUE(phone)','Phone number must be unique.')]