{
    "name": "Purchase Line Receiving Note",
    "version": "20.0.1.0.0",
    "category": "Inventory/Purchase",
    "summary": "Transfer product-wise receiving notes from Purchase Order lines to incoming receipt stock moves",
    "description": """
Purchase Line Receiving Note
============================
Allow purchase users to enter product-wise receiving instructions on Purchase Order lines.
Automatically transfer these instructions to corresponding incoming receipt stock moves
and preserve them across partial receipts and backorders.

Key Features:
-------------
- Optional Receiving Note text field on Purchase Order lines.
- Automatic transfer of receiving notes to incoming receipt stock moves upon PO confirmation.
- Read-only Receiving Note field on incoming receipt stock move lines.
- Preserves receiving instructions when partial receipts generate backorders.
- Keeps original receipt instructions intact even if PO line instructions are modified post-confirmation.
- Pure Odoo 20 Community & Enterprise compatible with zero extra external dependencies.

Developed by Dhara Thesiya
    """,
    "author": "Dhara Thesiya",
    "website": "https://dharaportfoliodoodeveloper.netlify.app/",
    "license": "LGPL-3",
    "price": 0.00,
    "currency": "EUR",
    "depends": ["purchase_stock"],
    "data": [
        "views/purchase_order_views.xml",
        "views/stock_picking_views.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
}
