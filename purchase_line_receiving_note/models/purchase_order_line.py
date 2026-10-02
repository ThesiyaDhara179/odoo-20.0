from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    receiving_note = fields.Text(
        string="Receiving Note",
        help="Instructions for warehouse receiving staff upon product receipt.",
    )

    def _prepare_stock_moves(self, picking):
        """Transfer receiving_note from Purchase Order Line to created stock.move records."""
        res = super()._prepare_stock_moves(picking)
        for move_vals in res:
            line_id = move_vals.get('purchase_line_id')
            if line_id:
                line = self.browse(line_id)
                move_vals['receiving_note'] = line.receiving_note
            elif self:
                move_vals['receiving_note'] = self[0].receiving_note
        return res
