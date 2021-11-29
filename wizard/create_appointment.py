from odoo import api, fields, models


class CreateAppointmentWizard(models.TransientModel):
    _name = 'create.appointment.wizard'
    _description = 'create appoinment'

    name = fields.Char(string='Name', required='True')
    patient_id = fields.Many2one(comodel_name='patient', string='Patient')

    def create_appointment_action(self):
        print("Button Is Clicked")
    
