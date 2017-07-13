import wmi
import os

class Networkerror(RuntimeError):
    def __init__(self, arg):
       self.args = arg

def GetCluster(computer="."):
    try:
        res = os.system('ping %s -n 1' % (computer,))
        if res == 0:
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
        else:
            raise Networkerror('Server not found or not reachable')
    except Networkerror, arg:
        print "Error: ", arg.args
    except wmi.x_wmi:
        print "The server isn't a cluster node"
