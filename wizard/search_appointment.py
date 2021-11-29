from odoo import api, fields, models, _


class SearchAppointmentWizard(models.Model):
    _name = 'search.appointment.wizard'
    _description = 'Search Appointment Wizard'

    patient_id = fields.Many2one('patient', string='Patient', required=True)
    
    def action_search_appointment_m1(self):
        action = self.env.ref('ujiocba.search_appointment_action').read=()[0]
        action['domain'] = [('patient_id', '=' , self.patient_id.id)]
        return action

    def action_search_appointment_m2(self):
        action = self.env.ref('ir.action.action')._for_xml_id=("ujicoba.hospital_appointment_action")
        action['domain'] = [('patient_id', '=' , self.patient_id.id)]
        return action

    def action_search_appointment_m3(self):
        return {
            'type'      :   'ir.action.act_window',
            'name'      :   'Appointment',
            'res_model' :   'hospital_appointment',
            'view_type' :   'form',
            'domain'    :   [('patient_id', '=', self.patient_id.id)],
            'view_mode' :   'tree,form',
            'target'    :   'current'
        }
        return action