# Company Contacts Portal

## Overview
The **Company Contacts Portal** is an Odoo module that enhances the portal functionality by allowing users to view and send a message to company contacts through the portal view. This module improves accessibility and usability for external users.

## Features
- Display company contacts in the portal.
- Send a message to the contact.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/marijastosic/company_contacts_portal.git
   ```
2. Move the module to your Odoo addons directory:
   ```bash
   mv company_contacts_portal /your/odoo/addons/
   ```
3. Restart the Odoo server:
   ```bash
   sudo systemctl restart odoo
   ```
4. Activate the developer mode in Odoo.
5. Install the module from **Apps** in Odoo.

## Usage
- Navigate to **Portal > Company Contacts**.
- View contacts based on your access level.
- Send a message to contacts by clicking on the "Send Message" button.
- Selected contact can view this messsage in its chatter (both message body and recipient info).
## Configuration
- Go to **Settings > Users & Companies > Users**.
- Assign the necessary access rights for portal users.

