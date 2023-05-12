from odoo import models,fields,api
from odoo.exceptions import UserError
class DrugsPropertyOrders(models.Model):
    _name="drugs.property.orders"
    _description="Order Placed by customer from the medical"
    _rec_name = 'cust_id'
    _order="order_date desc"

    cust_id=fields.Many2one("drugs.property.customers",required=True, string="Customer")
    order_date=fields.Date(default=fields.Date.today())
    total_amount=fields.Float(compute="_compute_total_amount", store=True)
    order_lines=fields.One2many("drugs.property.orders.lines","order_id", string="Order Lines")
    # quantity=fields.Integer(related="order_lines.quantity")
    # drug_id=fields.Many2one(related="order_lines.drug_id")
    # price=fields.Float(related="order_lines.price")
    state=fields.Selection(
        selection=[
            ("new","New"),
            ("sold","Sold"),
            ("canceled","Canceled"),
        ],
        copy=False,
        default="new",
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
                # record.total_amount=0    
            record.state="sold"      


    def action_canceled_medicine(self):
        for record in self:
            if record.state=='sold':
                raise UserError("A sold medicine cannot be canceled")
            record.state="canceled"      

    