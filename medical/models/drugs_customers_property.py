from odoo import models,fields

class DrugsPropertyCustomer(models.Model):
    _name="drugs.property.customers"
    _description="customer who purchase medicines from the medical shop"

    name=fields.Char(required=True)
    address=fields.Text()
    email=fields.Char()
    phone=fields.Char()
    cust_id=fields.Integer(required=True)
    _sql_constraints=[('phone_unique','UNIQUE(phone)','Phone number must be unique.')]