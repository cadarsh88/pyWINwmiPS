import wmi
c = wmi.WMI(namespace="MSCluster")

clu = c.MSCluster_Cluster()
nod = c.MSCluster_Node()
rgr = c.MSCluster_ResourceGroupToResource()

p = set()
s = set()

for cluster in clu:
    print "Cluster Name:", cluster.name

for clunodes in nod:
    print"Cluster Nodes: \n", clunodes.name

for i in rgr:
    p.add(str(i.GroupComponent))
    s.add(str(i.PartComponent))

print "Resource Groups: \n"
for j in p:
    print j

print "Clustered Resources: \n"
for k in s:
    print k



