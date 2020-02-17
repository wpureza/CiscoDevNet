from acitoolkit.acitoolkit import *

def TentantList(session):
    return Tenant.get(session)

URL = 'https://sandboxapicdc.cisco.com'
LOGIN = 'admin'
PASSWORD = 'ciscopsdt'

session = Session(URL, LOGIN,   PASSWORD)
session.login()

epg_list = EPG.get(session)
for epg in epg_list:
    print(EPG.get_attributes(epg))