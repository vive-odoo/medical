from odoo import fields,models

class DrugsPropertyTags(models.Model):
    _name="drugs.property.tags"
    _description="Drugs Tags"
    _order="name"


    name=fields.Char(string="Tags", required=True)
    _sql_constraints=[('unique_property_tag_name','unique(name)','The property tag name should be unique')]
