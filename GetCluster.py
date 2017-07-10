import wmi

def Get_Cluster(computer="."):
    c = wmi.WMI(computer=computer, namespace="MSCluster", authentication_level="pktPrivacy")
    clu = c.MSCluster_Cluster()
    nod = c.MSCluster_Node()
    rgr = c.MSCluster_ResourceGroupToResource()
    nar = c.MSCluster_NodeToActiveResource()

    p = set()
    s = set()

    print "\n"

    for cluster in clu:
        print "Cluster Name:", cluster.name


    print "\nCluster Nodes: \n"

    for clunodes in nod:
        print clunodes.name

    print "\n"

    for z in rgr:
        kv = str(z.GroupComponent).split("=")
        mn = str(z.PartComponent).split("=")
        for y in nar:
            na = str(y.GroupComponent).split("=")
            jy = str(y.PartComponent).split("=")
            if(mn==jy):
                print "Resource Name:", mn[1], "Resource Group: ", kv[1], "Node Name:", na[1]

