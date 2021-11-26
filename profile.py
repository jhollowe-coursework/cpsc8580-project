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


nodes = {"r1": {"link_to": ["r2", "fw1"], "setup_commands": ['pwd | sudo tee /setup_test.txt']},
         "r2": {"link_to": ["r1", "fw1", "r3"]},
         "r3": {"link_to": ["r1", "r2", "fw2"]},
         "r4": {"link_to": ["fw2", "h1", "h2"]},
         "r5": {"link_to": ["fw2", "h3", "h4"]},
         "d1": {},
         "d2": {},
         "fw1": {"link_to": ["d1", "d2"]},
         "fw2": {},
         "h1": {},
         "h2": {},
         "h3": {},
         "h4": {},
         "a1": {"link_to": ["c1"]},
         "c1": {"link_to": ["a1"]}}


# create nodes
for node_name in nodes:
    node = request.XenVM(node_name)
    nodes[node_name]["_node_obj"] = node

    node.disk_image = os_urn

    # add setup commands that should be run on all nodes
    for cmd in global_setup_commands:
        node.addService(pg.Execute(base_shell, cmd))

    # add node-specific setup commands
    for cmd in (nodes[node_name].get("setup_commands") or []):
        node.addService(pg.Execute(base_shell, cmd))

# create links on instantiated nodes
for node_name in nodes:
    for link_dest in (nodes[node_name].get("link_to") or []):

        # create a place to store link objects
        if nodes[node_name].get("_link_objs") is None:
            nodes[node_name]["_link_objs"] = []

        # create the link
        node_self = nodes[node_name]["_node_obj"]
        node_other = nodes[link_dest]["_node_obj"]
        link = request.Link(members=[node_self, node_other])
        nodes[node_name]["_link_objs"].append(link)

        # ensure a duplicate reverse link will not be created
        if nodes[link_dest].get("link_to") is not None:
            if node_name in nodes[link_dest]["link_to"]:
                nodes[link_dest]["link_to"].remove(node_name)

# Print the generated rspec
pc.printRequestRSpec(request)
