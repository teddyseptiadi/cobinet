from frappe import _

def get_data():
   return {
      'fieldname': 'anfrage',
      'non_standard_fieldnames': {
        'Opportunity': 'von_anfrage'
      },
      'transactions': [
         {
            'label': _('Sales'),
            'items': ['Opportunity']
         }
      ]
   }
