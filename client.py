from ssdpy import SSDPClient

client = SSDPClient()
devices = client.m_search()
for device in devices:
    print(device)

