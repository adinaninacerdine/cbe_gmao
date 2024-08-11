from odoo import models, fields, api
from datetime import datetime, timedelta

class MaintenanceRequest(models.Model):
    _inherit = 'maintenance.request'

    is_due_for_maintenance = fields.Boolean(compute='_compute_due_for_maintenance', store=True)

    @api.depends('x_studio_date_de_suivi_de_maintenance')
    def _compute_due_for_maintenance(self):
        for record in self:
            if record.x_studio_date_de_suivi_de_maintenance:
                delta = (fields.Datetime.now() - record.x_studio_date_de_suivi_de_maintenance).days
                record.is_due_for_maintenance = delta > 1
            else:
                record.is_due_for_maintenance = False

    @api.model
    def create_stock_move_for_maintenance(self):
        for record in self:
            if record.is_due_for_maintenance:
                for product in record.x_studio_many2many_field_5rd_1i4p634uk:
                    stock_move = self.env['stock.move'].create({
                        'name': 'Consommation pour Maintenance',
                        'product_id': product.id,
                        'product_uom_qty': 1,
                        'product_uom': product.uom_id.id,
                        'location_id': self.env.ref('stock.stock_location_stock').id,
                        'location_dest_id': self.env.ref('stock.stock_location_output').id,
                        'state': 'confirmed',
                    })
                    stock_move._action_confirm()
                    stock_move._action_assign()
                    stock_move._action_done()
