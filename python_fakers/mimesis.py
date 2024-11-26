from python_fakers.mimesis import Generic
from mimesis.locales import Locale
g = Generic(locale=Locale.EN)

# Create ERP-like data
erp_data = {
    'company': g.company.company(),
    'invoice_number': g.business.invoice_number(),
    'price': g.business.price(),
    'vendor_code': g.business.vendor_code()
}