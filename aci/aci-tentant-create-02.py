from acitoolkit.acitoolkit import *

URL = 'https://sandboxapicdc.cisco.com'
LOGIN = 'admin'
PASSWORD = 'ciscopsdt'

session = Session(URL, LOGIN, PASSWORD)
session.login()

tenant_name = "INITIALS_Example_Tenant"
new_tenant = Tenant(tenant_name)
vrf = Context("Example_VRF", new_tenant)

bridge_domain = BridgeDomain("Example_BD", new_tenant)
bridge_domain.add_context(vrf)

subnet = Subnet("Example_Subnet", bridge_domain)
subnet.set_scope('public')
subnet.set_addr('10.10.10.1/24')

filter_http = Filter("http", new_tenant)
filter_entry_tcp80 = FilterEntry("tcp-80", filter_http, etherT="ip", prot="tcp", dFromPort='http', dToPort='http')

filter_sql = Filter("sql", new_tenant)
filter_entry_tcp1433 = FilterEntry("tcp-1433", filter_http, etherT="ip", prot="tcp", dFromPort='1433', dToPort='1433')

contract_web = Contract('web', new_tenant)

contract_subject_http = ContractSubject("http", contract_web)
contract_subject_http.add_filter(filter_http)

contract_database = Contract("database", new_tenant)

contract_subject_sql = ContractSubject("sql", contract_database)
contract_subject_sql.add_filter(filter_sql)

app_profile = AppProfile("Example_App", new_tenant)

epg_web = EPG("Web", app_profile)
epg_web.add_bd(bridge_domain)
epg_web.provide(contract_web)
epg_web.consume(contract_database)

epg_database = EPG("Database", app_profile)
epg_database.add_bd(bridge_domain)
epg_database.provide(contract_database)

resp = session.push_to_apic(new_tenant.get_url(), new_tenant.get_json())
if resp.ok:
    print("\n{}: {}\n\n{} is ready for use".format(resp.status_code, resp.reason, new_tenant.name))
else:
    print("\n{}: {}\n\n{} was not created!\n\n Error: {}".format(resp.status_code, resp.reason, subnet.name, resp.content))