from odoo import models,fields

class DrugsProperty(models.Model):
    _name="drugs.property"
    _description="Drugs info Property"
    _log_access = False

    drug_id=fields.Integer(required=True)
    name=fields.Char(required=True)
    description=fields.Text()
    quantity=fields.Integer()
    selling_price=fields.Float()
    manufacture=fields.Many2one("res.users", string="Salesman",default=lambda self:self.env.user)
    expiry_date=fields.Date(required=True)

    state=fields.Selection(
        selection=[
            ("order","Order"),
            ("deliver","Deliver"),
            ("instock","In Stock"),
            ("sold","Sold"),
            ("canceled","Canceled"),
        ],
        copy=False,
        default="order",
    )


    tag_ids=fields.Many2many("drugs.property.tags")