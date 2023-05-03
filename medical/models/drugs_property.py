from odoo import models,fields,api
from odoo.exceptions import UserError

class DrugsProperty(models.Model):
    _name="drugs.property"
    _description="Drugs info Property"
    _log_access = False

    drug_id=fields.Integer(required=True)
    name=fields.Char(required=True)
    description=fields.Text()
    quantity=fields.Integer()
    selling_price=fields.Float()
    manufacture=fields.Many2one("res.partner", string="Salesman",default=lambda self:self.env.user)
    expiry_date=fields.Date(required=True)

    state=fields.Selection(
        selection=[
            ("order","Order"),
            ("deliver","Deliver"),
            ("instock","In Stock"),
            ("store","store"),
            ("canceled","Canceled"),
        ],
        copy=False,
        default="order",
    )


    tag_ids=fields.Many2many("drugs.property.tags")

    # @api.onchange('quantity')
    # def _compute_quantity(self):
    #     if self.quantity<0:
    #         return {
    #             'warning':{
    #                 'title':'warning',
    #                 'message':'Quantity cannot be negative',
    #             },
    #         }
    #     else:
    #         return self.quantity    


    def action_store_medicine(self):
        for record in self:
            if record.state=='canceled' :
                raise UserError("A store medicine cannot be canceled")
            elif record.quantity<0:
                raise UserError("Negative quantity not be stored")    
            record.state="store"      


    def action_canceled_medicine(self):
        for record in self:
            if record.state=='store':
                raise UserError("A store medicine cannot be canceled")
            record.state="canceled"  