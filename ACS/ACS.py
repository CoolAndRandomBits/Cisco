import requests

BaseURL = "https://<ACShostname>/Rest/NetworkDevice/Device"


print("\n")
print("Please enter your ACS credentials.\n")
print("WARNING: Password will be echoed to screen.  Make sure no one is looking.\n")
Username = input("Username: ")
Password = input("Password: ")
  

objSession = requests.Session()
objSession.auth = (Username, Password)
objSession.verify = False


hostname = "device-hostname"
ipaddr = "3.3.3.3"
deviceType = "All Device Types:UPS"
deviceLoc = "All Locations:UPS_Devices"
authSecret = "_____________"



payloadACS = """
<ns2:device xmlns:ns2="networkdevice.rest.mgmt.acs.nm.cisco.com">
    <name>""" + hostname + """</name>
    <groupInfo>
        <groupName>""" + deviceType + """</groupName>
        <groupType>Device Type</groupType>
    </groupInfo>
    <groupInfo>
        <groupName>""" + deviceLoc + """</groupName>
        <groupType>Location</groupType>
    </groupInfo>
    <radiusConnection>
        <sharedSecret>""" + authSecret + """</sharedSecret>
    </radiusConnection>
    <subnets>
        <ipAddress>""" + ipaddr + """</ipAddress>
        <netMask>32</netMask>
    </subnets>
</ns2:device>
"""

print(payloadACS)
headerXML = {'Content-Type': 'application/xml'}
r = objSession.post(BaseURL, headers=headerXML, data=payloadACS)

