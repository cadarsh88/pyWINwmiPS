import wmi

def Get_OS(computer="."):
	c = wmi.WMI(computer=computer, namespace="CIMv2", authentication_level="pktPrivacy")

	os = c.Win32_OperatingSystem()
	cs = c.Win32_ComputerSystem()

	for j in os:
		print "\nHostname = ", str(j.CSName), "\nOS = ", str(j.Caption) + str(j.Version), "\nServicePack = ", str(j.CSDVersion)

	for i in cs:
		print "\nNumberOfProcessors = ", int(i.NumberOfProcessors), "\nNumbereOfLogicalProcecssors = ", int(i.NumberOfLogicalProcessors), "\nTotalPhysicalMemory(GB) = ", int(i.TotalPhysicalMemory)/1073741824
	