import logging
import xlwt

_logger = logging.getLogger(__name__)

from odoo import models, fields, api


class MyModel(models.Model):
    _name = 'my.model'
    # add fields here

    def export_data_to_excel(self):
        # create an xlwt workbook and sheet
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('My Model Data')

        # create the header row
        sheet.write(0, 0, 'ID')
        sheet.write(0, 1, 'Field 1')
        sheet.write(0, 2, 'Field 2')
        # add more header cells as needed

        # retrieve all records from the model
        records = self.env['my.model'].search([])

        # iterate through the records and write them to the sheet
        row = 1
        for record in records:
            sheet.write(row, 0, record.id)
            sheet.write(row, 1, record.field_1)
            sheet.write(row, 2, record.field_2)
            # add more cells as needed
            row += 1

        # save the workbook to a file
        workbook.save('my_model_data.xls')