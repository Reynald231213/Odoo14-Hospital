from odoo import api, fields, models,_


class HospitalPatient(models.Model):
    _name = 'patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Patient'

    name = fields.Char(string='Name', Required = True)
    age = fields.Integer(string='Age')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),])
    note = fields.Text(string='Description')
    responsible_id = fields.Many2one(comodel_name='res.partner', string='Responsible')
    state = fields.Selection(string='Status', selection=[('confirm', 'Confirm'), ('done', 'Done'),('draft', 'Draft'),('cancel', 'Cancel')])
    appointment_count = fields.Integer(string='Appointment Count', compute='_compute_appointment_count')
    image = fields.Binary(string='Patient Image')
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    
    def action_confirm(self):
        self.state = 'confirm'
    def action_done(self):
        self.state = 'done'
    def action_draft(self):
        self.state = 'draft'
    def action_cancel(self):
        self.state = 'cancel'

class HospitalKids(models.Model):
    _name = 'kids'
    _description = 'Pasien Kids'

    name = fields.Char(string='Name')
    age = fields.Char(string='Age')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),])
    state = fields.Selection(string='State', selection=[('confirm', 'Confirm'), ('done', 'Done'),('draft', 'Draft'),('cancel', 'Cancel')])

