# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AutoBackupConfigSettings(models.TransientModel):
    _name = 'autobackup.config.settings'
    _inherit = 'res.config.settings'

    autobackup_enabled = fields.Boolean(string="Auto Backup Enabled?")
    db_name = fields.Char(string="Database Name")
    master_pwd = fields.Char(string="Odoo Master Password")
    backup_dir = fields.Char(string="Backup Directory")
    backup_format = fields.Selection([('zip', 'ZIP (includes filestore)'), ('dump', 'Dump File')],
                                     string="Backup Format", default='zip')

    @api.multi
    def set_autobackup_enabled(self):
        return self.env['ir.values'].sudo().set_default('autobackup.config.settings', 'autobackup_enabled',
                                                        self.autobackup_enabled)

    @api.multi
    def set_db_name(self):
        return self.env['ir.values'].sudo().set_default('autobackup.config.settings', 'db_name', self.db_name)

    @api.multi
    def set_master_pwd(self):
        return self.env['ir.values'].sudo().set_default('autobackup.config.settings', 'master_pwd', self.master_pwd)

    @api.multi
    def set_backup_dir(self):
        return self.env['ir.values'].sudo().set_default('autobackup.config.settings', 'backup_dir', self.backup_dir)

    @api.multi
    def set_backup_format(self):
        return self.env['ir.values'].sudo().set_default('autobackup.config.settings', 'backup_format',
                                                        self.backup_format)
