import frappe
from frappe.utils import cint

@frappe.whitelist()
def update_warranty_parts(doc,method):

          
            material = frappe.db.get_value('Warranty Request',{'name':doc.warranty_request_name},['name'])
            if material:
                mr = frappe.get_doc('Warranty Request',material)

                if doc.items:  
                    for i in doc.items:           
                        mr.append("material_request_part",{
                            'item_code':i.item_code,
                            'item_name':i.item_name,
                            'qty':i.qty,
                            'uom':i.uom,
                            'schedule_date':i.schedule_date
                            })
                            
                        mr.flags.ignore_permissions  = True
                        mr.save()
                        frappe.msgprint(msg = 'Warranty Request Updated Successfully',
				            	title = 'Message',
					            indicator = 'green')
			                        
                        return   


                        