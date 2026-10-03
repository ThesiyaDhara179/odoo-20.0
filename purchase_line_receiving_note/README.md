# Purchase Line Receiving Note

**Technical Name:** `purchase_line_receiving_note`  
**Odoo Version:** 20.0  
**License:** OPL-1  
**Category:** Inventory/Purchase  
**Author:** Dhara Thesiya  
**Price:** $2.00 USD

---

## Overview

The **Purchase Line Receiving Note** module allows purchasing users to specify line-by-line product receiving instructions directly on Purchase Order lines. When the Purchase Order is confirmed, these instructions automatically transfer to the corresponding incoming receipt stock moves (`stock.move`).

Warehouse receiving staff can view these instructions directly on the receipt screen, ensuring proper product handling, storage instructions, inspection guidelines, or special warehouse procedures are followed without manual communication.

---

## Key Features

1. **Purchase Order Line Receiving Note**:
   - Optional `receiving_note` text field added to Purchase Order lines.
   - Displayed in both line list view and form view.

2. **Automatic Transfer to Incoming Receipts**:
   - Automatically copies receiving notes from Purchase Order lines to `stock.move` records upon PO confirmation.

3. **Read-Only Receipt Visibility**:
   - Displays receiving instructions on incoming receipt stock move lines as read-only fields.

4. **Backorder & Partial Receipt Preservation**:
   - Automatically preserves receiving notes on backorders when partial receipts are validated.

5. **Historical Integrity**:
   - Preserves original receipt instructions if the Purchase Order line instruction is modified post-confirmation.

6. **Standard Stock Integrity**:
   - Does not alter standard Odoo stock quantities, reservation logic, or receipt validation flows.

---

## Configuration & Usage

### 1. Installation
1. Place the `purchase_line_receiving_note` directory in your custom addons path.
2. Update the apps list in Odoo (**Apps > Update Apps List**).
3. Search for `Purchase Line Receiving Note` and click **Install**.

### 2. Enter Receiving Notes on Purchase Orders
1. Go to **Purchase > Orders > Purchase Orders** and create a new Purchase Order.
2. On each Purchase Order line, enter specific instructions in the **Receiving Note** column (e.g., *"Store in Cold Storage - Rack B"*, *"Inspect seals before unloading"*).
3. Click **Confirm Order**.

### 3. View Notes on Incoming Receipt
1. Click the **Receipt** smart button on the confirmed Purchase Order.
2. In the incoming receipt form, each product move line displays the read-only **Receiving Note** column transferred from the Purchase Order.

---

## Technical Specifications

- **Dependencies:** `purchase_stock`
- **Models Extended:**
  - `purchase.order.line` (`receiving_note` text field, overrides `_prepare_stock_moves`)
  - `stock.move` (`receiving_note` text field, overrides `_prepare_move_copy_values`)
- **Views Overridden:**
  - `purchase.purchase_order_form`
  - `stock.view_picking_form`
  - `stock.view_move_form`
- **Automated Tests:**
  - Unit tests included in `tests/test_purchase_line_receiving_note.py`.

---

## Support & Contact

- **Author:** Dhara Thesiya
- **Website / Portfolio:** [https://dharaportfoliodoodeveloper.netlify.app/](https://dharaportfoliodoodeveloper.netlify.app/)
- **License:** Odoo Proprietary License v1.0 (OPL-1)
