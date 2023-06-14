from odoo import models,fields,Command

class MedicalAccount(models.Model):
    _inherit =  "drugs.property.orders"
    def action_sold_medicine(self):
        print(self)
        self.env["account.move"].create(
        {
            "cust_id": self.cust_id.id,
            "move_type":'out_invoice',
            "line_ids": [
                Command.create({
                    'order_date': self.order_date,
                    'drug_id': self.order_lines.drug_id,
                    'price': self.order_lines.price,
                    'quantity':self.order_lines.quantity,
                    'total_amount':self.total_amount
                }),
            ],
        }
    )
        return super().action_sold_medicine()