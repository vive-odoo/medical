from odoo import models,fields,api
from odoo.exceptions import UserError
class DrugsPropertyOrders(models.Model):
    _name="drugs.property.orders"
    _description="Order Placed by customer from the medical"
    _rec_name = 'cust_id'

    cust_id=fields.Many2one("drugs.property.customers",required=True)
    order_date=fields.Date(default=fields.Date.today())
    total_amount=fields.Float(compute="_compute_total_amount", store=True)
    order_lines=fields.One2many("drugs.property.orders.lines","order_id", string="Order Lines")
    state=fields.Selection(
        selection=[
            ("sold","Sold"),
            ("canceled","Canceled"),
        ],
        copy=False,
        default=None,
    )

    # _sql_constraints=[('date_customer_unique','UNIQUE(order_date , cust_id)','An order already exists for this customer on this date.')]            

    @api.depends('order_lines.subtotal')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount=sum(record.order_lines.mapped('subtotal')) 


    def action_sold_medicine(self):
        for record in self:
            if record.state=='canceled' :
                raise UserError("A sold medicine cannot be canceled")
            elif record.order_lines.quantity<0:
                raise UserError("Negative quantity not be sold")
                # record.total_amount=0    
            record.state="sold"      


    def action_canceled_medicine(self):
        for record in self:
            if record.state=='sold':
                raise UserError("A sold medicine cannot be canceled")
            record.state="canceled"      

    