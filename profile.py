"""Base topology for ZTA & BYOD work"""

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

os_urn = "urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD"
base_shell = "/bin/sh"

global_setup_commands = ["sudo apt update",
                         "sudo apt install -y openvswitch-switch"]


nodes = {"r1": {"setup_commands": ['pwd | sudo tee /setup_test.txt']},
         "r2": {},
         "r3": {},
         "r4": {},
         "r5": {},
         "d1": {},
         "d2": {},
         "fw1": {},
         "fw2": {},
         "h1": {},
         "h2": {},
         "h3": {},
         "h4": {},
         "a1": {},
         "c1": {}}


# create nodes
for node_name in nodes:
    node = request.XenVM(node_name)
    nodes[node_name]["node_obj"] = node

    node.disk_image = os_urn

    # add setup commands that should be run on all nodes
    for cmd in global_setup_commands:
        node.addService(pg.Execute(base_shell, cmd))

    # add node-specific setup commands
    for cmd in (nodes[node_name].get("setup_commands") or []):
        node.addService(pg.Execute(base_shell, cmd))


# Print the generated rspec
pc.printRequestRSpec(request)
