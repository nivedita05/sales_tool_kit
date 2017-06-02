
# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import datetime,timedelta
from frappe.utils import getdate, add_days, add_years, cstr,formatdate, strip
from erpnext.stock.stock_ledger import get_previous_sle, NegativeStockError
from frappe.model.naming import make_autoname
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe import utils
class SampleForm(Document):
	def autoname(self):
		#estateabr = frappe.db.get_value("Estate",{"estate_name": self.estatename}, "abbreviation")
		self.name = make_autoname("SAM" + "/.####")

	def validate(self):
		self.get_courier_link()
		self.set_address()
		
	def get_courier_link(self):
		if self.courier_name=="DTDC":
			self.courier_website = "www.dtdc.in"
		if self.courier_name=="BLUE DART":
			self.courier_website = "www.bluedart.com"
		if self.courier_name=="TIRUPATI":
			self.courier_website = "www.shreetirupaticourier.net"
		if self.courier_name=="INLAND":
			self.courier_website = "http://www.courier-services.in/inland-couriers-private-limited-burrabazar-kolkata_contact-number-address"
		if self.courier_name=="JAYSHREE":
			self.courier_website = "http://www.trackcourier.net/jayshree-courier-service-tracking/"


	def set_address(self):
		line1 = frappe.db.sql("""select address_line1 from `tabAddress` where address_title=%s """,(self.customer_name))
		#line2 = frappe.db.sql("""select address_line2 from `tabAddress` where address_title=%s """,(self.customer_name))
		city = frappe.db.sql("""select city from `tabAddress` where address_title=%s """,(self.customer_name))
		country = frappe.db.sql("""select country from `tabAddress` where address_title=%s """,(self.customer_name))
		state = frappe.db.sql("""select state from `tabAddress` where address_title=%s """,(self.customer_name))
		
		self.address = line1[0][0] 
		self.shipping_address = line1[0][0] 