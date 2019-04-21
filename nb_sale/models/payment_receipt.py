from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PaymentReceiptNB(models.Model):
    _name = 'payment.receipt.nb'

    no_kwitansi = fields.Char(string='Nomor Kwitansi')