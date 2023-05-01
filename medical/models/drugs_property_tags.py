from odoo import fields,models

class DrugsPropertyTags(models.Model):
    _name="drugs.property.tags"
    _description="Drugs Tags"
    _order="name"


    name=fields.Char(string="Tags", required=True)
