import cobra.mit.access
import cobra.mit.session
import cobra.mit.request
import cobra.model.fv
import cobra.model.pol

URL = 'https://sandboxapicdc.cisco.com'
LOGIN = 'admin'
PASSWORD = 'ciscopsdt'

auth = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
session = cobra.mit.access.MoDirectory(auth)
session.login()

tenant_name = "INITIALS_Cobra_Tenant"

root = cobra.model.pol.Uni('')
new_tenant = cobra.model.fv.Tenant(root, tenant_name)

config_request = cobra.mit.request.ConfigRequest()
config_request.addMo(new_tenant)
session.commit(config_request)