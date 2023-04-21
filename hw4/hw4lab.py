import socket
import pandas as pd
import graphviz

# Read domains from TSV file
domains = pd.read_csv("domains.tsv", sep='\t')['domain']

# Initialize variables
main_dom = 1
dns = {}
last = {}
addr = {}
node = 300

# Initialize graph to be more efficient
dot = graphviz.Digraph(engine='fdp', comment='digraphtesting')

# Loop through domains until prompted to pass
for dom in domains:
    try:
        # Perform forward DNS lookup
        address = socket.getaddrinfo(dom, 443, type=socket.SOCK_STREAM)

        # Add node for domain across to graph
        main_dom += 1
        with dot.subgraph() as s:
            s.node(str(main_dom), dom)

        # Loop through IP addresses and perform reverse DNS lookup
        for j in range(len(address)-1):
            try:
                port = address[j][4]
                rev_dns = socket.gethostbyaddr(port[0])[0]
                node += 1
                dot.node(str(node), rev_dns)
                dot.edge(str(node), str(main_dom))
            except:
                pass
    except:
        pass
