# -- coding: utf-8 --
from odoo import api, fields, models,_


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Appointment"

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True,
                       default=lambda self:_('New'))
    patient_id = fields.Many2one('patient', string="Patient", required=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft',
                             string="Status", tracking=True)
    note = fields.Text(string='Description')
    date_appointment = fields.Date(string='Date')
    date_checkup = fields.Datetime(string='Date Checkup')
    appointment_count = fields.Integer(string='Appointment Count', compute= "_compute_appointment_count")
    
    
    
    def _compute_appointment_count(self):
        appointment_count=self.env['appointment'
        ].search_count([('patient_id', '=', self.id)])
        self.appointment_count = appointment_count


    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self, vals):
        if vals.get('name', ('New')) == ('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or ('New')
        res = super(HospitalAppointment, self).create(vals)
        return res