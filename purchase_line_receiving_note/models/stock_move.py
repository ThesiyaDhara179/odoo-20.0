from odoo import fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    receiving_note = fields.Text(
        string="Receiving Note",
        help="Instructions for warehouse receiving staff upon product receipt.",
    )

    def _prepare_move_copy_values(self, **kwargs):
        """Preserve receiving_note when copying/splitting stock moves (e.g. backorders)."""
        res = super()._prepare_move_copy_values(**kwargs)
        res['receiving_note'] = self.receiving_note
        return res
