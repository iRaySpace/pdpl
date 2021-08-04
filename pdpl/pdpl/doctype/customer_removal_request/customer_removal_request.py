# -*- coding: utf-8 -*-
# Copyright (c) 2021, 9T9IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class CustomerRemovalRequest(Document):
	def validate(self):
		contact = _get_contact(self.customer)
		if not contact:
			frappe.msgprint("There is no Contact found on this customer. Contact fields will not be used.")

		for field in self.fields:
			if not field.is_contact_field:
				frappe.db.set_value("Customer", self.customer, field.fieldname, None)

	def on_submit(self):
		contact = _get_contact(self.customer)
		if contact:
			fields = list(map(lambda x: x.fieldname, self.fields))
			_set_contact_fields_to_empty(contact, fields)


def _set_contact_fields_to_empty(contact, fields):
	for field in fields:
		frappe.db.set_value("Contact", contact, field, None)


def _get_contact(customer):
	link = frappe.db.get_all(
		"Dynamic Link",
		filters={
			"link_doctype": "Customer",
			"link_name": customer,
		},
		fields=["parent"]
	)
	if not link:
		return None
	return link[0].get("parent")
