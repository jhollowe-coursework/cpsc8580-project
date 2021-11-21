"""Base topology for ZTA & BYOD work"""

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node r1
node_r1 = request.XenVM('r1')
node_r1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_r1.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_r1.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface0 = node_r1.addInterface('interface-3')
iface1 = node_r1.addInterface('interface-15')
iface2 = node_r1.addInterface('interface-19')

# Node r2
node_r2 = request.XenVM('r2')
node_r2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_r2.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_r2.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface3 = node_r2.addInterface('interface-5')
iface4 = node_r2.addInterface('interface-17')
iface5 = node_r2.addInterface('interface-18')

# Node fw1
node_fw1 = request.XenVM('fw1')
node_fw1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_fw1.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_fw1.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface6 = node_fw1.addInterface('interface-2')
iface7 = node_fw1.addInterface('interface-4')
iface8 = node_fw1.addInterface('interface-25')
iface9 = node_fw1.addInterface('interface-27')

# Node fw2
node_fw2 = request.XenVM('fw2')
node_fw2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_fw2.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_fw2.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface10 = node_fw2.addInterface('interface-11')
iface11 = node_fw2.addInterface('interface-13')
iface12 = node_fw2.addInterface('interface-21')

# Node r5
node_r5 = request.XenVM('r5')
node_r5.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_r5.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_r5.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface13 = node_r5.addInterface('interface-10')
iface14 = node_r5.addInterface('interface-9')
iface15 = node_r5.addInterface('interface-23')

# Node r4
node_r4 = request.XenVM('r4')
node_r4.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_r4.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_r4.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface16 = node_r4.addInterface('interface-12')
iface17 = node_r4.addInterface('interface-1')
iface18 = node_r4.addInterface('interface-7')

# Node r3
node_r3 = request.XenVM('r3')
node_r3.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_r3.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_r3.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface19 = node_r3.addInterface('interface-14')
iface20 = node_r3.addInterface('interface-16')
iface21 = node_r3.addInterface('interface-20')

# Node h1
node_h1 = request.XenVM('h1')
node_h1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_h1.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_h1.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface22 = node_h1.addInterface('interface-0')

# Node h2
node_h2 = request.XenVM('h2')
node_h2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_h2.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_h2.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface23 = node_h2.addInterface('interface-6')

# Node h3
node_h3 = request.XenVM('h3')
node_h3.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_h3.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_h3.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface24 = node_h3.addInterface('interface-8')

# Node h4
node_h4 = request.XenVM('h4')
node_h4.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_h4.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_h4.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface25 = node_h4.addInterface('interface-22')

# Node d1
node_d1 = request.XenVM('d1')
node_d1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_d1.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_d1.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface26 = node_d1.addInterface('interface-24')

# Node d2
node_d2 = request.XenVM('d2')
node_d2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_d2.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_d2.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface27 = node_d2.addInterface('interface-26')

# Node c1
node_c1 = request.XenVM('c1')
node_c1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_c1.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_c1.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface28 = node_c1.addInterface('interface-29')

# Node a1
node_a1 = request.XenVM('a1')
node_a1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_a1.addService(pg.Execute('/bin/sh', 'sudo apt update'))
node_a1.addService(pg.Execute(
    '/bin/sh', 'sudo apt install -y openvswitch-switch'))
iface29 = node_a1.addInterface('interface-28')

# Link link-1
link_1 = request.Link('link-1')
link_1.Site('undefined')
link_1.addInterface(iface6)
link_1.addInterface(iface0)

# Link link-2
link_2 = request.Link('link-2')
link_2.Site('undefined')
link_2.addInterface(iface7)
link_2.addInterface(iface3)

# Link link-5
link_5 = request.Link('link-5')
link_5.Site('undefined')
link_5.addInterface(iface13)
link_5.addInterface(iface10)

# Link link-6
link_6 = request.Link('link-6')
link_6.Site('undefined')
link_6.addInterface(iface16)
link_6.addInterface(iface11)

# Link link-7
link_7 = request.Link('link-7')
link_7.Site('undefined')
link_7.addInterface(iface19)
link_7.addInterface(iface1)

# Link link-8
link_8 = request.Link('link-8')
link_8.Site('undefined')
link_8.addInterface(iface20)
link_8.addInterface(iface4)

# Link link-9
link_9 = request.Link('link-9')
link_9.Site('undefined')
link_9.addInterface(iface5)
link_9.addInterface(iface2)

# Link link-10
link_10 = request.Link('link-10')
link_10.Site('undefined')
link_10.addInterface(iface21)
link_10.addInterface(iface12)

# Link link-0
link_0 = request.Link('link-0')
link_0.Site('undefined')
link_0.addInterface(iface22)
link_0.addInterface(iface17)

# Link link-3
link_3 = request.Link('link-3')
link_3.Site('undefined')
link_3.addInterface(iface23)
link_3.addInterface(iface18)

# Link link-4
link_4 = request.Link('link-4')
link_4.Site('undefined')
link_4.addInterface(iface24)
link_4.addInterface(iface14)

# Link link-11
link_11 = request.Link('link-11')
link_11.Site('undefined')
link_11.addInterface(iface25)
link_11.addInterface(iface15)

# Link link-12
link_12 = request.Link('link-12')
link_12.Site('undefined')
link_12.addInterface(iface26)
link_12.addInterface(iface8)

# Link link-13
link_13 = request.Link('link-13')
link_13.Site('undefined')
link_13.addInterface(iface27)
link_13.addInterface(iface9)

# Link link-14
link_14 = request.Link('link-14')
link_14.Site('undefined')
link_14.addInterface(iface29)
link_14.addInterface(iface28)


# Print the generated rspec
pc.printRequestRSpec(request)
