# Inventory Plugin - itential.plugins.solarwinds

The `itential.plugins.solarwinds` plugin provides an Ansible inventory plugin
that, once installed, can be used to pull inventory from Solarwinds NCM.  The
plugin is forked from
[here](https://github.com/dalrrard/ansible-solarwinds-inventory-plugin) and
updated to work in the `itential.plugins` collection.

```bash
curl  https://172.20.101.102:17774/SolarWinds/InformationService/v3/Json/Query -k -u Admin:Admin@Admin -H "content-type: application/json" -X POST -d '{"query": "SELECT CN.SysName, CN.OSImage, CN.AgentIP, CN.ConnectionProfile, CN.OSVersion, CN.MachineType FROM Cirrus.Nodes CN}"'

curl https://172.20.101.102:17774/SolarWinds/InformationService/v3/Json/Invoke/Cirrus.Nodes/GetConnectionProfile -X POST -H "Content-Type: application/json" -k  -u Admin:Admin@Admin -d '{"id": 1}'
```
