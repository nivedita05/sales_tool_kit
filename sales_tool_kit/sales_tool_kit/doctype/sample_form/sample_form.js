// Copyright (c) 2017, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Sample Form', {
	refresh: function(frm) {

	}
});

cur_frm.fields_dict['customer_address'].get_query = function(doc) {
return{
filters:[
['address_title', '=', doc.customer_name]

]
}}
cur_frm.fields_dict['shipping_detail'].get_query = function(doc) {
return{
filters:[
['address_title', '=', doc.customer_name]

]
}}