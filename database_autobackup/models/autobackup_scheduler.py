# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import os
import logging

_logger = logging.getLogger(__name__)


class AutoBackupScheduler(models.Model):
    _name = 'autobackup.scheduler'
    _description = 'Auto Backup Scheduler'

    @api.model
    def cron_database_autobackup(self):
        _logger.info(":::: Autobackup Cron Started ::::")
        autobackup_enabled = self.env['ir.values'].get_default('autobackup.config.settings', 'autobackup_enabled')
        if autobackup_enabled:
            time_now = str(fields.Datetime.now(self)).replace(' ', '_')
            db_name = self.env['ir.values'].get_default('autobackup.config.settings', 'db_name')
            master_pwd = self.env['ir.values'].get_default('autobackup.config.settings', 'master_pwd')
            backup_dir = self.env['ir.values'].get_default('autobackup.config.settings', 'backup_dir')
            if backup_dir and backup_dir[-1] != '/':
                backup_dir += '/'
            backup_format = self.env['ir.values'].get_default('autobackup.config.settings', 'backup_format')
            server_url = self.env['ir.config_parameter'].get_param('web.base.url')
            command = 'curl --insecure -X POST -F "master_pwd=%s" -F "name=%s" -F "backup_format=%s" ' \
                      '-o %s%s_%s_db.%s %s/web/database/backup' % (master_pwd, db_name, backup_format,
                                                                   backup_dir, db_name, time_now,
                                                                   backup_format, server_url)
            unix_code = os.system(command)
            _logger.info(":::: Autobackup Cron Feedback Unix Code (Backup): %s ::::" % unix_code)
        _logger.info(":::: Autobackup Cron Finished ::::")
