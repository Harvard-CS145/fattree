#!/usr/bin/python3

# ./topology/generate_fattree_topo.py [K]
#   Generate the FatTree topology config file `topology/p4app_fattree.json`
#   with [K] value

import sys


# Usage function
def usage():
    print(
        "Usage: ./topology/generate_fattree_topo.py [K]\n\t"
        "Generate the FatTree topology config file `topology/p4app_fattree.json` "
        "with [K] value"
    )


template = """{
    "p4_src": "p4src/l2fwd.p4",
    "cli": true,
    "pcap_dump": true,
    "enable_log": true,
    "topology": {
        "assignment_strategy": "l2",
        "links": [%s],
        "hosts": {
            %s
        },
        "switches": {
            %s
        }
    }
}
"""

# Get the K value from command line argument (choose from 4, 6, 8)
k = 4  # by default we K=4
try:
    k = int(sys.argv[1])
except Exception as e:
    print(f"Failed to parse the argument [K]! Cause: {e}")
    usage()
    exit(1)

if k != 4 and k != 6 and k != 8:
    print("K should be 4, 6, or 8!")
    usage()
    exit(1)

print(f"We have K={k} in the FatTree topology")

# Generate the topology details, number of hosts, tor switches, agg switches, and core switches
half_k = k // 2
host_num = k * k * k // 4
tor_num = k * k // 2
agg_num = k * k // 2
core_num = k * k // 4

# Generate our own JSON string
hosts = ""
# TODO: generate the hosts JSON string

print(f"Host list: {hosts}")

switches = ""
# TODO: generate the switches JSON string

print(f"Switch list: {switches}")

links = ""
# TODO: generate the links JSON string

print(f"Link list: {links}")

# Write the generated config JSON to file
f = None
try:
    f = open("topology/p4app_fattree.json", "w")
except Exception as e:
    print(
        "Failed to open file topology/p4app_fattree.json to write the JSON config! "
        f"Cause: {e}"
    )
try:
    f.write(template % (links, hosts, switches))
except Exception as e:
    print(f"Failed to write to file topology/p4app_fattree.json! Cause: {e}")

print("Successfully generate FatTree topology config file topology/p4app_fattree.json")
