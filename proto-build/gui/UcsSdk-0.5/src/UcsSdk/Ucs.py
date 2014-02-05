from xml.dom.minidom import *
from UcsBase import *

def BaseObject(name):
	if (name == "Method"):
		return Method()
	elif (name == "MethodSet"):
		return MethodSet()
	elif (name == "AllbitsFilter"):
		return AllbitsFilter()
	elif (name == "AndFilter"):
		return AndFilter()
	elif (name == "AnybitFilter"):
		return AnybitFilter()
	elif (name == "BwFilter"):
		return BwFilter()
	elif (name == "ClassId"):
		return ClassId()
	elif (name == "ClassIdSet"):
		return ClassIdSet()
	elif (name == "ConfigConfig"):
		return ConfigConfig()
	elif (name == "ConfigMap"):
		return ConfigMap()
	elif (name == "ConfigSet"):
		return ConfigSet()
	elif (name == "Dn"):
		return Dn()
	elif (name == "DnSet"):
		return DnSet()
	elif (name == "EqFilter"):
		return EqFilter()
	elif (name == "FilterFilter"):
		return FilterFilter()
	elif (name == "GeFilter"):
		return GeFilter()
	elif (name == "GtFilter"):
		return GtFilter()
	elif (name == "Id"):
		return Id()
	elif (name == "IdSet"):
		return IdSet()
	elif (name == "LeFilter"):
		return LeFilter()
	elif (name == "LtFilter"):
		return LtFilter()
	elif (name == "NeFilter"):
		return NeFilter()
	elif (name == "NotFilter"):
		return NotFilter()
	elif (name == "OrFilter"):
		return OrFilter()
	elif (name == "Pair"):
		return Pair()
	elif (name == "WcardFilter"):
		return WcardFilter()
	else:
		return ManagedObject(UcsUtils.WordL(name))

def ClassFactory(name):
	from UcsBase import UcsUtils
	from MoMeta import _VersionMeta,_ManagedObjectMeta
	from MethodMeta import _MethodFactoryMeta
	if name in _ManagedObjectMeta.keys():
		return ManagedObject(name)
	elif name in _MethodFactoryMeta.keys():
		return ExternalMethod(name)
	else:
		return BaseObject(UcsUtils.WordU(name))

class Method(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "Method")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("method")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"aaaChangeSelfPassword",
					"aaaCheckComputeAuthToken",
					"aaaCheckComputeExtAccess",
					"aaaGetAuthTokenClient",
					"aaaGetNComputeAuthTokenByDn",
					"aaaKeepAlive",
					"aaaLogin",
					"aaaLogout",
					"aaaRefresh",
					"aaaTokenLogin",
					"aaaTokenRefresh",
					"apeBootPnuOs",
					"apeConfigureCMCLIF",
					"apeCreateHVVnic",
					"apeCreateSfish",
					"apeCreateVMVnic",
					"apeDeleteHVVnic",
					"apeDeleteSfish",
					"apeDeleteVMVnic",
					"apeGetAdaptorConnectivity",
					"apeGetPnuOSInventory",
					"apeGetSwitchApeFru",
					"apeInjectStimuli",
					"apeInsertNewChassis",
					"apeInsertNewFex",
					"apeInsertNewRack",
					"apeIssueChassisId",
					"apeIssueFexId",
					"apeIssueRackId",
					"apeMcGet",
					"apeMcGetBiosTokens",
					"apeMcGetSmbios",
					"apeMcSet",
					"apeMuxOffline",
					"apeSetServerLifeCycle",
					"apeSetSwitchInventory",
					"computeGetInventory",
					"configCheckCompatibility",
					"configCheckConformance",
					"configCheckFirmwareUpdatable",
					"configConfFiltered",
					"configConfMo",
					"configConfMoGroup",
					"configConfMos",
					"configConfRename",
					"configEstimateImpact",
					"configFindDependencies",
					"configFindDnsByClassId",
					"configFindHostPackDependencies",
					"configFindPermitted",
					"configGetXmlFile",
					"configGetXmlFileStr",
					"configInstallAllImpact",
					"configMoChangeEvent",
					"configRefreshIdentity",
					"configReleaseResolveContext",
					"configRenewResolveContext",
					"configResolveChildren",
					"configResolveChildrenSorted",
					"configResolveClass",
					"configResolveClassSorted",
					"configResolveClasses",
					"configResolveClassesSorted",
					"configResolveContext",
					"configResolveDn",
					"configResolveDns",
					"configResolveParent",
					"configScope",
					"eventRegisterEventChannel",
					"eventRegisterEventChannelResp",
					"eventSendEvent",
					"eventSendHeartbeat",
					"eventSubscribe",
					"eventUnRegisterEventChannel",
					"eventUnsubscribe",
					"externalMethod",
					"faultAckFault",
					"faultAckFaults",
					"faultResolveFault",
					"fsmDebugAction",
					"loggingSyncOcns",
					"lsClone",
					"lsInstantiateNNamedTemplate",
					"lsInstantiateNTemplate",
					"lsInstantiateTemplate",
					"lsResolveTemplates",
					"lsTemplatise",
					"methodVessel",
					"mgmtResolveBackupFilenames",
					"orgResolveElements",
					"orgResolveLogicalParents",
					"policyResolveNames",
					"poolResolveInScope",
					"statsClearInterval",
					"statsResolveThresholdPolicy",
					"swatExample",
					"swatGetstats",
					"swatInject",
					"syntheticFSObjInventory",
					"syntheticFSObjInventoryB",
					"syntheticTestTx",
					"trigPerformTokenAction",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class MethodSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "MethodSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("methodSet")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"aaaChangeSelfPassword",
					"aaaCheckComputeAuthToken",
					"aaaCheckComputeExtAccess",
					"aaaGetAuthTokenClient",
					"aaaGetNComputeAuthTokenByDn",
					"aaaKeepAlive",
					"aaaLogin",
					"aaaLogout",
					"aaaRefresh",
					"aaaTokenLogin",
					"aaaTokenRefresh",
					"apeBootPnuOs",
					"apeConfigureCMCLIF",
					"apeCreateHVVnic",
					"apeCreateSfish",
					"apeCreateVMVnic",
					"apeDeleteHVVnic",
					"apeDeleteSfish",
					"apeDeleteVMVnic",
					"apeGetAdaptorConnectivity",
					"apeGetPnuOSInventory",
					"apeGetSwitchApeFru",
					"apeInjectStimuli",
					"apeInsertNewChassis",
					"apeInsertNewFex",
					"apeInsertNewRack",
					"apeIssueChassisId",
					"apeIssueFexId",
					"apeIssueRackId",
					"apeMcGet",
					"apeMcGetBiosTokens",
					"apeMcGetSmbios",
					"apeMcSet",
					"apeMuxOffline",
					"apeSetServerLifeCycle",
					"apeSetSwitchInventory",
					"computeGetInventory",
					"configCheckCompatibility",
					"configCheckConformance",
					"configCheckFirmwareUpdatable",
					"configConfFiltered",
					"configConfMo",
					"configConfMoGroup",
					"configConfMos",
					"configConfRename",
					"configEstimateImpact",
					"configFindDependencies",
					"configFindDnsByClassId",
					"configFindHostPackDependencies",
					"configFindPermitted",
					"configGetXmlFile",
					"configGetXmlFileStr",
					"configInstallAllImpact",
					"configMoChangeEvent",
					"configRefreshIdentity",
					"configReleaseResolveContext",
					"configRenewResolveContext",
					"configResolveChildren",
					"configResolveChildrenSorted",
					"configResolveClass",
					"configResolveClassSorted",
					"configResolveClasses",
					"configResolveClassesSorted",
					"configResolveContext",
					"configResolveDn",
					"configResolveDns",
					"configResolveParent",
					"configScope",
					"eventRegisterEventChannel",
					"eventRegisterEventChannelResp",
					"eventSendEvent",
					"eventSendHeartbeat",
					"eventSubscribe",
					"eventUnRegisterEventChannel",
					"eventUnsubscribe",
					"externalMethod",
					"faultAckFault",
					"faultAckFaults",
					"faultResolveFault",
					"fsmDebugAction",
					"loggingSyncOcns",
					"lsClone",
					"lsInstantiateNNamedTemplate",
					"lsInstantiateNTemplate",
					"lsInstantiateTemplate",
					"lsResolveTemplates",
					"lsTemplatise",
					"methodVessel",
					"mgmtResolveBackupFilenames",
					"orgResolveElements",
					"orgResolveLogicalParents",
					"policyResolveNames",
					"poolResolveInScope",
					"statsClearInterval",
					"statsResolveThresholdPolicy",
					"swatExample",
					"swatGetstats",
					"swatInject",
					"syntheticFSObjInventory",
					"syntheticFSObjInventoryB",
					"syntheticTestTx",
					"trigPerformTokenAction",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class AllbitsFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "AllbitsFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("allbits")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class AndFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "AndFilter")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("and")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"abstractFilter",
					"allbits",
					"and",
					"anybit",
					"bw",
					"eq",
					"ge",
					"gt",
					"le",
					"lt",
					"ne",
					"not",
					"or",
					"wcard",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class AnybitFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "AnybitFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("anybit")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class BwFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "BwFilter")
		self.Class = None
		self.FirstValue = None
		self.Property = None
		self.SecondValue = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("bw")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("firstValue", getattr(self,"FirstValue"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("secondValue", getattr(self,"SecondValue"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class ClassId(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ClassId")
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("classId")
		else:
			x = w.createElement(elementName)
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class ClassIdSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ClassIdSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("classIdSet")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"classId",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class ConfigConfig(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ConfigConfig")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("configConfig")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"aaaAuthRealm",
					"aaaAuthRealmFsm",
					"aaaAuthRealmFsmStage",
					"aaaConsoleAuth",
					"aaaDefaultAuth",
					"aaaDomain",
					"aaaDomainAuth",
					"aaaEpAuthProfile",
					"aaaEpFsm",
					"aaaEpFsmStage",
					"aaaEpFsmTask",
					"aaaEpLogin",
					"aaaEpUser",
					"aaaExtMgmtCutThruTkn",
					"aaaLdapEp",
					"aaaLdapEpFsm",
					"aaaLdapEpFsmStage",
					"aaaLdapGroup",
					"aaaLdapGroupRule",
					"aaaLdapProvider",
					"aaaLocale",
					"aaaLog",
					"aaaModLR",
					"aaaOrg",
					"aaaPreLoginBanner",
					"aaaProviderGroup",
					"aaaProviderRef",
					"aaaPwdProfile",
					"aaaRadiusEp",
					"aaaRadiusEpFsm",
					"aaaRadiusEpFsmStage",
					"aaaRadiusProvider",
					"aaaRealmFsm",
					"aaaRealmFsmStage",
					"aaaRealmFsmTask",
					"aaaRemoteUser",
					"aaaRole",
					"aaaSession",
					"aaaSessionLR",
					"aaaShellLogin",
					"aaaSshAuth",
					"aaaTacacsPlusEp",
					"aaaTacacsPlusEpFsm",
					"aaaTacacsPlusEpFsmStage",
					"aaaTacacsPlusProvider",
					"aaaUser",
					"aaaUserData",
					"aaaUserEp",
					"aaaUserEpFsm",
					"aaaUserEpFsmStage",
					"aaaUserEpFsmTask",
					"aaaUserLocale",
					"aaaUserRole",
					"aaaWebLogin",
					"adaptorCapQual",
					"adaptorCapSpec",
					"adaptorDiagCap",
					"adaptorEthCompQueueProfile",
					"adaptorEthFailoverProfile",
					"adaptorEthInterruptProfile",
					"adaptorEthOffloadProfile",
					"adaptorEthPortBySizeLargeStats",
					"adaptorEthPortBySizeLargeStatsHist",
					"adaptorEthPortBySizeSmallStats",
					"adaptorEthPortBySizeSmallStatsHist",
					"adaptorEthPortErrStats",
					"adaptorEthPortErrStatsHist",
					"adaptorEthPortMcastStats",
					"adaptorEthPortMcastStatsHist",
					"adaptorEthPortOutsizedStats",
					"adaptorEthPortOutsizedStatsHist",
					"adaptorEthPortStats",
					"adaptorEthPortStatsHist",
					"adaptorEthRecvQueueProfile",
					"adaptorEthWorkQueueProfile",
					"adaptorEtherIfStats",
					"adaptorEtherIfStatsHist",
					"adaptorExtEthIf",
					"adaptorExtEthIfFsm",
					"adaptorExtEthIfFsmStage",
					"adaptorExtEthIfFsmTask",
					"adaptorExtEthIfPc",
					"adaptorExtEthIfPcEp",
					"adaptorExtIpV6RssHashProfile",
					"adaptorFamilyTypeDef",
					"adaptorFcCdbWorkQueueProfile",
					"adaptorFcErrorRecoveryProfile",
					"adaptorFcIfEventStats",
					"adaptorFcIfEventStatsHist",
					"adaptorFcIfFC4Stats",
					"adaptorFcIfFC4StatsHist",
					"adaptorFcIfFrameStats",
					"adaptorFcIfFrameStatsHist",
					"adaptorFcInterruptProfile",
					"adaptorFcOEIf",
					"adaptorFcPortFLogiProfile",
					"adaptorFcPortPLogiProfile",
					"adaptorFcPortProfile",
					"adaptorFcPortStats",
					"adaptorFcPortStatsHist",
					"adaptorFcRecvQueueProfile",
					"adaptorFcWorkQueueProfile",
					"adaptorFruCapProvider",
					"adaptorFruCapRef",
					"adaptorFwCapProvider",
					"adaptorHostEthIf",
					"adaptorHostEthIfFsm",
					"adaptorHostEthIfFsmStage",
					"adaptorHostEthIfFsmTask",
					"adaptorHostEthIfProfile",
					"adaptorHostFcIf",
					"adaptorHostFcIfFsm",
					"adaptorHostFcIfFsmStage",
					"adaptorHostFcIfFsmTask",
					"adaptorHostFcIfProfile",
					"adaptorHostIscsiIf",
					"adaptorHostIscsiIfProfile",
					"adaptorHostMgmtCap",
					"adaptorHostethHwAddrCap",
					"adaptorHostfcHwAddrCap",
					"adaptorIScsiCap",
					"adaptorIpV4RssHashProfile",
					"adaptorIpV6RssHashProfile",
					"adaptorIscsiAuth",
					"adaptorIscsiProt",
					"adaptorIscsiTargetIf",
					"adaptorLanCap",
					"adaptorLldpCap",
					"adaptorMenloBaseErrorStats",
					"adaptorMenloBaseErrorStatsHist",
					"adaptorMenloDcePortStats",
					"adaptorMenloDcePortStatsHist",
					"adaptorMenloEthErrorStats",
					"adaptorMenloEthErrorStatsHist",
					"adaptorMenloEthStats",
					"adaptorMenloEthStatsHist",
					"adaptorMenloFcErrorStats",
					"adaptorMenloFcErrorStatsHist",
					"adaptorMenloFcStats",
					"adaptorMenloFcStatsHist",
					"adaptorMenloHostPortStats",
					"adaptorMenloHostPortStatsHist",
					"adaptorMenloMcpuErrorStats",
					"adaptorMenloMcpuErrorStatsHist",
					"adaptorMenloMcpuStats",
					"adaptorMenloMcpuStatsHist",
					"adaptorMenloNetEgStats",
					"adaptorMenloNetEgStatsHist",
					"adaptorMenloNetInStats",
					"adaptorMenloNetInStatsHist",
					"adaptorMenloQErrorStats",
					"adaptorMenloQErrorStatsHist",
					"adaptorMenloQStats",
					"adaptorMenloQStatsHist",
					"adaptorNwMgmtCap",
					"adaptorProtocolProfile",
					"adaptorQual",
					"adaptorRssProfile",
					"adaptorSanCap",
					"adaptorUnit",
					"adaptorUnitAssocCtx",
					"adaptorUnitExtn",
					"adaptorUplinkHwAddrCap",
					"adaptorVlan",
					"adaptorVnicStats",
					"adaptorVnicStatsHist",
					"adaptorVsan",
					"apeControllerChassis",
					"apeControllerEeprom",
					"apeControllerManager",
					"apeDcosAgManager",
					"apeFru",
					"apeHostAgent",
					"apeLANBoot",
					"apeLocalDiskBoot",
					"apeManager",
					"apeMc",
					"apeMcTable",
					"apeMenlo",
					"apeMenloVnic",
					"apeMenloVnicStats",
					"apeNicAgManager",
					"apePalo",
					"apePaloVnic",
					"apePaloVnicStats",
					"apeParam",
					"apeReading",
					"apeSANBoot",
					"apeSdr",
					"apeSwitchFirmwareInv",
					"apeVirtualMediaBoot",
					"biosBOT",
					"biosBootDev",
					"biosBootDevGrp",
					"biosFeatureRef",
					"biosParameterRef",
					"biosRef",
					"biosSettingRef",
					"biosSettings",
					"biosUnit",
					"biosVIdentityParams",
					"biosVProfile",
					"biosVfACPI10Support",
					"biosVfAssertNMIOnPERR",
					"biosVfAssertNMIOnSERR",
					"biosVfBootOptionRetry",
					"biosVfCPUPerformance",
					"biosVfConsoleRedirection",
					"biosVfCoreMultiProcessing",
					"biosVfDirectCacheAccess",
					"biosVfEnhancedIntelSpeedStepTech",
					"biosVfExecuteDisableBit",
					"biosVfFrontPanelLockout",
					"biosVfIntelEntrySASRAIDModule",
					"biosVfIntelHyperThreadingTech",
					"biosVfIntelTurboBoostTech",
					"biosVfIntelVTForDirectedIO",
					"biosVfIntelVirtualizationTechnology",
					"biosVfLvDIMMSupport",
					"biosVfMaxVariableMTRRSetting",
					"biosVfMaximumMemoryBelow4GB",
					"biosVfMemoryMappedIOAbove4GB",
					"biosVfMirroringMode",
					"biosVfNUMAOptimized",
					"biosVfOSBootWatchdogTimer",
					"biosVfOSBootWatchdogTimerPolicy",
					"biosVfOSBootWatchdogTimerTimeout",
					"biosVfOnboardSATAController",
					"biosVfOnboardStorage",
					"biosVfOptionROMEnable",
					"biosVfOptionROMLoad",
					"biosVfPCISlotOptionROMEnable",
					"biosVfPOSTErrorPause",
					"biosVfPackageCStateLimit",
					"biosVfProcessorC1E",
					"biosVfProcessorC3Report",
					"biosVfProcessorC6Report",
					"biosVfProcessorC7Report",
					"biosVfProcessorCState",
					"biosVfQuietBoot",
					"biosVfResumeOnACPowerLoss",
					"biosVfSelectMemoryRASConfiguration",
					"biosVfSerialPortAEnable",
					"biosVfSparingMode",
					"biosVfSriovConfig",
					"biosVfUCSMBootOrderRuleControl",
					"biosVfUEFIOSUseLegacyVideo",
					"biosVfUSBBootConfig",
					"biosVfUSBFrontPanelAccessLock",
					"biosVfUSBSystemIdlePowerOptimizingSetting",
					"bmcSELCounter",
					"callhomeDest",
					"callhomeEp",
					"callhomeEpFsm",
					"callhomeEpFsmStage",
					"callhomeEpFsmTask",
					"callhomePeriodicSystemInventory",
					"callhomePolicy",
					"callhomeProfile",
					"callhomeSmtp",
					"callhomeSource",
					"callhomeTestAlert",
					"capabilityCatalogue",
					"capabilityCatalogueFsm",
					"capabilityCatalogueFsmStage",
					"capabilityCatalogueFsmTask",
					"capabilityEp",
					"capabilityFeatureLimits",
					"capabilityMgmtExtension",
					"capabilityMgmtExtensionFsm",
					"capabilityMgmtExtensionFsmStage",
					"capabilityMgmtExtensionFsmTask",
					"capabilityNetworkLimits",
					"capabilityStorageLimits",
					"capabilitySystemLimits",
					"capabilityUpdate",
					"capabilityUpdater",
					"capabilityUpdaterFsm",
					"capabilityUpdaterFsmStage",
					"capabilityUpdaterFsmTask",
					"clitestTypeTest",
					"clitestTypeTest2",
					"clitestTypeTestChild",
					"commCimxml",
					"commDateTime",
					"commDns",
					"commDnsProvider",
					"commEvtChannel",
					"commHttp",
					"commHttps",
					"commNtpProvider",
					"commShellSvcLimits",
					"commSmashCLP",
					"commSnmp",
					"commSnmpTrap",
					"commSnmpUser",
					"commSsh",
					"commSvcEp",
					"commSvcEpFsm",
					"commSvcEpFsmStage",
					"commSvcEpFsmTask",
					"commSyslog",
					"commSyslogClient",
					"commSyslogConsole",
					"commSyslogFile",
					"commSyslogMonitor",
					"commSyslogSource",
					"commTelnet",
					"commWebChannel",
					"commWebSvcLimits",
					"commWsman",
					"commXmlClConnPolicy",
					"computeAutoconfigPolicy",
					"computeBlade",
					"computeBladeDiscPolicy",
					"computeBladeFsm",
					"computeBladeFsmStage",
					"computeBladeFsmTask",
					"computeBladeInheritPolicy",
					"computeBoard",
					"computeBoardController",
					"computeChassisConnPolicy",
					"computeChassisDiscPolicy",
					"computeChassisQual",
					"computeDefaults",
					"computeIOHub",
					"computeIOHubEnvStats",
					"computeIOHubEnvStatsHist",
					"computeMbPowerStats",
					"computeMbPowerStatsHist",
					"computeMbTempStats",
					"computeMbTempStatsHist",
					"computeMemoryUnitConstraintDef",
					"computePCIeFatalCompletionStats",
					"computePCIeFatalProtocolStats",
					"computePCIeFatalReceiveStats",
					"computePCIeFatalStats",
					"computePciCap",
					"computePciSlotScanDef",
					"computePhysicalAssocCtx",
					"computePhysicalFsm",
					"computePhysicalFsmStage",
					"computePhysicalFsmTask",
					"computePhysicalQual",
					"computePlatform",
					"computePnuOSImage",
					"computePool",
					"computePoolPolicyRef",
					"computePoolable",
					"computePooledRackUnit",
					"computePooledSlot",
					"computePoolingPolicy",
					"computePsuControl",
					"computePsuPolicy",
					"computeQual",
					"computeRackQual",
					"computeRackUnit",
					"computeRackUnitFsm",
					"computeRackUnitFsmStage",
					"computeRackUnitFsmTask",
					"computeRackUnitMbTempStats",
					"computeRackUnitMbTempStatsHist",
					"computeRtcBattery",
					"computeScrubPolicy",
					"computeServerDiscPolicy",
					"computeServerDiscPolicyFsm",
					"computeServerDiscPolicyFsmStage",
					"computeServerDiscPolicyFsmTask",
					"computeServerMgmtPolicy",
					"computeSlotQual",
					"configSorter",
					"dcxNs",
					"dcxUniverse",
					"dcxVIf",
					"dcxVc",
					"dcxVifEp",
					"dhcpAcquired",
					"dhcpInst",
					"dhcpLease",
					"diagBladeTest",
					"diagNetworkTest",
					"diagRslt",
					"diagRunPolicy",
					"diagSrvCapProvider",
					"diagSrvCtrl",
					"dpsecMac",
					"epqosDefinition",
					"epqosDefinitionDelTask",
					"epqosDefinitionDelTaskFsm",
					"epqosDefinitionDelTaskFsmStage",
					"epqosDefinitionDelTaskFsmTask",
					"epqosDefinitionFsm",
					"epqosDefinitionFsmStage",
					"epqosDefinitionFsmTask",
					"epqosEgress",
					"equipmentAdaptorConnDef",
					"equipmentAdaptorDef",
					"equipmentBaseBoardCapProvider",
					"equipmentBeaconCapProvider",
					"equipmentBeaconLed",
					"equipmentBeaconLedFsm",
					"equipmentBeaconLedFsmStage",
					"equipmentBeaconLedFsmTask",
					"equipmentBiosDef",
					"equipmentBladeAGLibrary",
					"equipmentBladeBiosCapProvider",
					"equipmentBladeCapProvider",
					"equipmentBladeConnDef",
					"equipmentBladeIOMConnDef",
					"equipmentBoardControllerDef",
					"equipmentCatalogCapProvider",
					"equipmentChassis",
					"equipmentChassisCapProvider",
					"equipmentChassisFsm",
					"equipmentChassisFsmStage",
					"equipmentChassisFsmTask",
					"equipmentChassisStats",
					"equipmentChassisStatsHist",
					"equipmentDbgPluginCapProvider",
					"equipmentDimmEntry",
					"equipmentDimmMapping",
					"equipmentDiscoveryCap",
					"equipmentFan",
					"equipmentFanModule",
					"equipmentFanModuleCapProvider",
					"equipmentFanModuleDef",
					"equipmentFanModuleStats",
					"equipmentFanModuleStatsHist",
					"equipmentFanStats",
					"equipmentFanStatsHist",
					"equipmentFex",
					"equipmentFexCapProvider",
					"equipmentFexEnvStats",
					"equipmentFexEnvStatsHist",
					"equipmentFexFsm",
					"equipmentFexFsmStage",
					"equipmentFexFsmTask",
					"equipmentFexPowerSummary",
					"equipmentFexPowerSummaryHist",
					"equipmentFexPsuInputStats",
					"equipmentFexPsuInputStatsHist",
					"equipmentGemCapProvider",
					"equipmentGemPortCap",
					"equipmentHDDFaultMonDef",
					"equipmentHostIfCapProvider",
					"equipmentIOCard",
					"equipmentIOCardCapProvider",
					"equipmentIOCardFsm",
					"equipmentIOCardFsmStage",
					"equipmentIOCardFsmTask",
					"equipmentIOCardStats",
					"equipmentIOCardStatsHist",
					"equipmentIOCardTypeDef",
					"equipmentIndicatorLed",
					"equipmentLocalDiskCapProvider",
					"equipmentLocalDiskControllerCapProvider",
					"equipmentLocalDiskControllerCapRef",
					"equipmentLocalDiskControllerDef",
					"equipmentLocalDiskDef",
					"equipmentLocatorLed",
					"equipmentLocatorLedFsm",
					"equipmentLocatorLedFsmStage",
					"equipmentLocatorLedFsmTask",
					"equipmentManufacturingDef",
					"equipmentMemoryUnitCapProvider",
					"equipmentMemoryUnitDiscoveryModifierDef",
					"equipmentMgmtCapProvider",
					"equipmentMgmtExtCapProvider",
					"equipmentNetworkElementFanStats",
					"equipmentNetworkElementFanStatsHist",
					"equipmentPOST",
					"equipmentPOSTCode",
					"equipmentPOSTCodeReporter",
					"equipmentPOSTCodeTemplate",
					"equipmentPciDef",
					"equipmentPhysicalDef",
					"equipmentPicture",
					"equipmentPortGroupAggregationDef",
					"equipmentPortGroupDef",
					"equipmentPortGroupSwComplexDef",
					"equipmentPortSwComplexRef",
					"equipmentProcessorUnitCapProvider",
					"equipmentProcessorUnitDef",
					"equipmentPsu",
					"equipmentPsuCapProvider",
					"equipmentPsuDef",
					"equipmentPsuInputStats",
					"equipmentPsuInputStatsHist",
					"equipmentPsuOutputStats",
					"equipmentPsuOutputStatsHist",
					"equipmentPsuStats",
					"equipmentPsuStatsHist",
					"equipmentRackUnitCapProvider",
					"equipmentRackUnitFanStats",
					"equipmentRackUnitFanStatsHist",
					"equipmentRackUnitPsuStats",
					"equipmentRackUnitPsuStatsHist",
					"equipmentRaidDef",
					"equipmentServerFeatureCap",
					"equipmentServiceDef",
					"equipmentSlotArray",
					"equipmentSlotArrayRef",
					"equipmentSwitchCap",
					"equipmentSwitchCapProvider",
					"equipmentSwitchCard",
					"equipmentUnifiedPortCapProvider",
					"equipmentXcvr",
					"etherErrStats",
					"etherErrStatsHist",
					"etherFcoeInterfaceStats",
					"etherFcoeInterfaceStatsHist",
					"etherLossStats",
					"etherLossStatsHist",
					"etherNicIfConfig",
					"etherPIo",
					"etherPIoEndPoint",
					"etherPIoFsm",
					"etherPIoFsmStage",
					"etherPauseStats",
					"etherPauseStatsHist",
					"etherPortChanIdElem",
					"etherPortChanIdUniverse",
					"etherRxStats",
					"etherRxStatsHist",
					"etherServerIntFIo",
					"etherServerIntFIoFsm",
					"etherServerIntFIoFsmStage",
					"etherServerIntFIoFsmTask",
					"etherServerIntFIoPc",
					"etherServerIntFIoPcEp",
					"etherSwIfConfig",
					"etherSwitchIntFIo",
					"etherSwitchIntFIoPc",
					"etherSwitchIntFIoPcEp",
					"etherTxStats",
					"etherTxStatsHist",
					"eventEpCtrl",
					"eventHolder",
					"eventInst",
					"eventLog",
					"eventPolicy",
					"eventRecord",
					"extmgmtArpTargets",
					"extmgmtGatewayPing",
					"extmgmtIf",
					"extmgmtIfMonPolicy",
					"extmgmtMiiStatus",
					"extpolClient",
					"extpolClientCont",
					"extpolController",
					"extpolControllerCont",
					"extpolEp",
					"extpolEpFsm",
					"extpolEpFsmStage",
					"extpolEpFsmTask",
					"extpolProvider",
					"extpolProviderCont",
					"extpolProviderFsm",
					"extpolProviderFsmStage",
					"extpolProviderFsmTask",
					"extpolRegistry",
					"extpolRegistryFsm",
					"extpolRegistryFsmStage",
					"extpolRegistryFsmTask",
					"extpolSystemContext",
					"extvmmEp",
					"extvmmEpFsm",
					"extvmmEpFsmStage",
					"extvmmEpFsmTask",
					"extvmmKeyInst",
					"extvmmKeyRing",
					"extvmmKeyStore",
					"extvmmKeyStoreFsm",
					"extvmmKeyStoreFsmStage",
					"extvmmKeyStoreFsmTask",
					"extvmmMasterExtKey",
					"extvmmMasterExtKeyFsm",
					"extvmmMasterExtKeyFsmStage",
					"extvmmMasterExtKeyFsmTask",
					"extvmmProvider",
					"extvmmProviderFsm",
					"extvmmProviderFsmStage",
					"extvmmProviderFsmTask",
					"extvmmSwitchDelTask",
					"extvmmSwitchDelTaskFsm",
					"extvmmSwitchDelTaskFsmStage",
					"extvmmSwitchDelTaskFsmTask",
					"extvmmSwitchSet",
					"fabricBHVlan",
					"fabricChassisEp",
					"fabricComputePhEp",
					"fabricComputeSlotEp",
					"fabricComputeSlotEpFsm",
					"fabricComputeSlotEpFsmStage",
					"fabricComputeSlotEpFsmTask",
					"fabricDceSrv",
					"fabricDceSwSrv",
					"fabricDceSwSrvEp",
					"fabricDceSwSrvPc",
					"fabricDceSwSrvPcEp",
					"fabricEp",
					"fabricEpMgr",
					"fabricEpMgrFsm",
					"fabricEpMgrFsmStage",
					"fabricEpMgrFsmTask",
					"fabricEthEstc",
					"fabricEthEstcCloud",
					"fabricEthEstcEp",
					"fabricEthEstcPc",
					"fabricEthEstcPcEp",
					"fabricEthLan",
					"fabricEthLanEp",
					"fabricEthLanPc",
					"fabricEthLanPcEp",
					"fabricEthMon",
					"fabricEthMonDestEp",
					"fabricEthMonFiltEp",
					"fabricEthMonFiltRef",
					"fabricEthMonLan",
					"fabricEthMonSrcEp",
					"fabricEthMonSrcRef",
					"fabricEthTargetEp",
					"fabricEthVlanPc",
					"fabricEthVlanPortEp",
					"fabricFcEstc",
					"fabricFcEstcCloud",
					"fabricFcEstcEp",
					"fabricFcMon",
					"fabricFcMonDestEp",
					"fabricFcMonFiltEp",
					"fabricFcMonFiltRef",
					"fabricFcMonSan",
					"fabricFcMonSrcEp",
					"fabricFcMonSrcRef",
					"fabricFcSan",
					"fabricFcSanEp",
					"fabricFcSanPc",
					"fabricFcSanPcEp",
					"fabricFcVsanPc",
					"fabricFcVsanPortEp",
					"fabricFcoeEstcEp",
					"fabricFcoeSanEp",
					"fabricFcoeSanPc",
					"fabricFcoeSanPcEp",
					"fabricFcoeVsanPc",
					"fabricFcoeVsanPortEp",
					"fabricIf",
					"fabricLanAccessMgr",
					"fabricLanCloud",
					"fabricLanCloudFsm",
					"fabricLanCloudFsmStage",
					"fabricLanCloudFsmTask",
					"fabricLanMonCloud",
					"fabricLanPinGroup",
					"fabricLanPinTarget",
					"fabricLastAckedSlot",
					"fabricLocale",
					"fabricMulticastPolicy",
					"fabricNetGroup",
					"fabricOrgVlanPolicy",
					"fabricPath",
					"fabricPathConn",
					"fabricPathEp",
					"fabricPoolableVlan",
					"fabricPooledVlan",
					"fabricSanCloud",
					"fabricSanCloudFsm",
					"fabricSanCloudFsmStage",
					"fabricSanCloudFsmTask",
					"fabricSanMonCloud",
					"fabricSanPinGroup",
					"fabricSanPinTarget",
					"fabricSwChPhEp",
					"fabricVCon",
					"fabricVConProfile",
					"fabricVlan",
					"fabricVlanEp",
					"fabricVlanGroupReq",
					"fabricVlanPermit",
					"fabricVlanReq",
					"fabricVsan",
					"fabricVsanEp",
					"fabricVsanMembership",
					"fabricZoneIdUniverse",
					"faultAffectedClass",
					"faultHolder",
					"faultInst",
					"faultLocalTypedHolder",
					"faultPolicy",
					"faultSuppressPolicy",
					"faultSuppressPolicyItem",
					"faultSuppressTask",
					"fcErrStats",
					"fcErrStatsHist",
					"fcNicIfConfig",
					"fcPIo",
					"fcPIoFsm",
					"fcPIoFsmStage",
					"fcStats",
					"fcStatsHist",
					"fcSwIfConfig",
					"fcpoolAddr",
					"fcpoolBlock",
					"fcpoolBootTarget",
					"fcpoolFormat",
					"fcpoolInitiator",
					"fcpoolInitiatorEp",
					"fcpoolInitiators",
					"fcpoolPoolable",
					"fcpoolUniverse",
					"firmwareAck",
					"firmwareBlade",
					"firmwareBootDefinition",
					"firmwareBootUnit",
					"firmwareBundleInfo",
					"firmwareBundleInfoDigest",
					"firmwareBundleType",
					"firmwareBundleTypeCapProvider",
					"firmwareCatalogPack",
					"firmwareCatalogue",
					"firmwareCompSource",
					"firmwareCompTarget",
					"firmwareComputeHostPack",
					"firmwareComputeMgmtPack",
					"firmwareDependency",
					"firmwareDistImage",
					"firmwareDistributable",
					"firmwareDistributableFsm",
					"firmwareDistributableFsmStage",
					"firmwareDistributableFsmTask",
					"firmwareDownloader",
					"firmwareDownloaderFsm",
					"firmwareDownloaderFsmStage",
					"firmwareDownloaderFsmTask",
					"firmwareHost",
					"firmwareHostPackModImpact",
					"firmwareImage",
					"firmwareImageFsm",
					"firmwareImageFsmStage",
					"firmwareImageFsmTask",
					"firmwareInfra",
					"firmwareInfraPack",
					"firmwareInstallImpact",
					"firmwareInstallable",
					"firmwarePackItem",
					"firmwareRack",
					"firmwareRunning",
					"firmwareSpec",
					"firmwareStatus",
					"firmwareSystem",
					"firmwareSystemCompCheckResult",
					"firmwareSystemFsm",
					"firmwareSystemFsmStage",
					"firmwareSystemFsmTask",
					"firmwareType",
					"firmwareUpdatable",
					"firmwareUpgradeConstraint",
					"firmwareUpgradeDetail",
					"firmwareUpgradeInfo",
					"flowctrlDefinition",
					"flowctrlItem",
					"fsmStatus",
					"hostimgPolicy",
					"hostimgTarget",
					"identIdentCtx",
					"identIdentRequest",
					"identIdentRequestFsm",
					"identIdentRequestFsmStage",
					"identIdentRequestFsmTask",
					"identMetaSystem",
					"identMetaSystemFsm",
					"identMetaSystemFsmStage",
					"identMetaSystemFsmTask",
					"identMetaVerse",
					"identRequestEp",
					"identSysInfo",
					"imgprovPolicy",
					"imgprovTarget",
					"imgsecKey",
					"imgsecPolicy",
					"initiatorFcInitiatorEp",
					"initiatorGroupEp",
					"initiatorIScsiInitiatorEp",
					"initiatorLunEp",
					"initiatorMemberEp",
					"initiatorRequestorEp",
					"initiatorRequestorGrpEp",
					"initiatorStoreEp",
					"initiatorUnitEp",
					"ipIPv4Dns",
					"ipIpV4StaticAddr",
					"ipServiceIf",
					"ippoolAddr",
					"ippoolBlock",
					"ippoolPool",
					"ippoolPoolable",
					"ippoolPooled",
					"ippoolUniverse",
					"iqnpoolAddr",
					"iqnpoolBlock",
					"iqnpoolFormat",
					"iqnpoolPool",
					"iqnpoolPoolable",
					"iqnpoolPooled",
					"iqnpoolUniverse",
					"iscsiAuthProfile",
					"iscsiProtocolProfile",
					"licenseContents",
					"licenseDownloader",
					"licenseDownloaderFsm",
					"licenseDownloaderFsmStage",
					"licenseDownloaderFsmTask",
					"licenseEp",
					"licenseFeature",
					"licenseFeatureCapProvider",
					"licenseFeatureLine",
					"licenseFile",
					"licenseFileFsm",
					"licenseFileFsmStage",
					"licenseFileFsmTask",
					"licenseInstance",
					"licenseInstanceFsm",
					"licenseInstanceFsmStage",
					"licenseInstanceFsmTask",
					"licenseProp",
					"licenseServerHostId",
					"licenseSource",
					"licenseSourceFile",
					"lldpAcquired",
					"lsAgentPolicy",
					"lsBinding",
					"lsFcLocale",
					"lsFcZone",
					"lsFcZoneGroup",
					"lsPower",
					"lsRequirement",
					"lsServer",
					"lsServerAssocCtx",
					"lsServerFsm",
					"lsServerFsmStage",
					"lsServerFsmTask",
					"lsTier",
					"lsVConAssign",
					"lsVersionBeh",
					"lsZoneInitiatorMember",
					"lsZoneTargetMember",
					"lsbootDef",
					"lsbootIScsi",
					"lsbootIScsiImagePath",
					"lsbootLan",
					"lsbootLanImagePath",
					"lsbootLocalStorage",
					"lsbootPolicy",
					"lsbootSanImage",
					"lsbootSanImagePath",
					"lsbootStorage",
					"lsbootVirtualMedia",
					"lsmaintAck",
					"lsmaintMaintPolicy",
					"macpoolAddr",
					"macpoolBlock",
					"macpoolFormat",
					"macpoolPool",
					"macpoolPoolable",
					"macpoolPooled",
					"macpoolUniverse",
					"managedObject",
					"memoryArray",
					"memoryArrayEnvStats",
					"memoryArrayEnvStatsHist",
					"memoryBufferUnit",
					"memoryBufferUnitEnvStats",
					"memoryBufferUnitEnvStatsHist",
					"memoryErrorStats",
					"memoryQual",
					"memoryRuntime",
					"memoryRuntimeHist",
					"memoryUnit",
					"memoryUnitEnvStats",
					"memoryUnitEnvStatsHist",
					"mgmtAccessPolicy",
					"mgmtAccessPolicyItem",
					"mgmtAccessPort",
					"mgmtBackup",
					"mgmtBackupFsm",
					"mgmtBackupFsmStage",
					"mgmtBackupFsmTask",
					"mgmtBackupPolicy",
					"mgmtBackupPolicyFsm",
					"mgmtBackupPolicyFsmStage",
					"mgmtCfgExportPolicy",
					"mgmtCfgExportPolicyFsm",
					"mgmtCfgExportPolicyFsmStage",
					"mgmtConnection",
					"mgmtController",
					"mgmtControllerFsm",
					"mgmtControllerFsmStage",
					"mgmtControllerFsmTask",
					"mgmtEntity",
					"mgmtExportPolicyFsm",
					"mgmtExportPolicyFsmStage",
					"mgmtExportPolicyFsmTask",
					"mgmtIf",
					"mgmtIfFsm",
					"mgmtIfFsmStage",
					"mgmtIfFsmTask",
					"mgmtImporter",
					"mgmtImporterFsm",
					"mgmtImporterFsmStage",
					"mgmtImporterFsmTask",
					"mgmtIntAuthPolicy",
					"mgmtPmonEntry",
					"networkElement",
					"networkIfStats",
					"nfsEp",
					"nfsMountDef",
					"nfsMountDefFsm",
					"nfsMountDefFsmStage",
					"nfsMountDefFsmTask",
					"nfsMountInst",
					"nfsMountInstFsm",
					"nfsMountInstFsmStage",
					"nfsMountInstFsmTask",
					"nwctrlDefinition",
					"observe",
					"observeObserved",
					"observeObservedCont",
					"observeObservedFsm",
					"observeObservedFsmStage",
					"observeObservedFsmTask",
					"orgOrg",
					"osAgent",
					"osInstance",
					"pciEquipSlot",
					"pciUnit",
					"pkiCertReq",
					"pkiEp",
					"pkiEpFsm",
					"pkiEpFsmStage",
					"pkiEpFsmTask",
					"pkiKeyRing",
					"pkiTP",
					"policyCommunication",
					"policyConfigBackup",
					"policyControlEp",
					"policyControlEpFsm",
					"policyControlEpFsmStage",
					"policyControlEpFsmTask",
					"policyControlledInstance",
					"policyControlledType",
					"policyDateTime",
					"policyDigest",
					"policyDiscovery",
					"policyDns",
					"policyFault",
					"policyInfraFirmware",
					"policyMEp",
					"policyMonitoring",
					"policyPolicyEp",
					"policyPolicyRequestor",
					"policyPolicyScope",
					"policyPolicyScopeCont",
					"policyPolicyScopeContext",
					"policyPolicyScopeFsm",
					"policyPolicyScopeFsmStage",
					"policyPolicyScopeFsmTask",
					"policyPowerMgmt",
					"policyPsu",
					"policySecurity",
					"portDomainEp",
					"portGroup",
					"portPIoFsm",
					"portPIoFsmStage",
					"portPIoFsmTask",
					"portTrustMode",
					"powerBudget",
					"powerChassisMember",
					"powerEp",
					"powerGroup",
					"powerGroupAdditionPolicy",
					"powerGroupQual",
					"powerGroupStats",
					"powerGroupStatsHist",
					"powerMgmtPolicy",
					"powerPlacement",
					"powerPolicy",
					"powerPrioWght",
					"powerRackUnitMember",
					"procDoer",
					"procManager",
					"procPrt",
					"procPrtCounts",
					"procStimulusCounts",
					"procSvc",
					"procTxCounts",
					"processorCore",
					"processorEnvStats",
					"processorEnvStatsHist",
					"processorErrorStats",
					"processorQual",
					"processorRuntime",
					"processorRuntimeHist",
					"processorThread",
					"processorUnit",
					"processorUnitAssocCtx",
					"qosclassDefinition",
					"qosclassDefinitionFsm",
					"qosclassDefinitionFsmStage",
					"qosclassDefinitionFsmTask",
					"qosclassEthBE",
					"qosclassEthClassified",
					"qosclassFc",
					"solConfig",
					"solIf",
					"solPolicy",
					"statsCollectionPolicy",
					"statsCollectionPolicyFsm",
					"statsCollectionPolicyFsmStage",
					"statsCollectionPolicyFsmTask",
					"statsHolder",
					"statsThr32Definition",
					"statsThr32Value",
					"statsThr64Definition",
					"statsThr64Value",
					"statsThrFloatDefinition",
					"statsThrFloatValue",
					"statsThresholdClass",
					"statsThresholdPolicy",
					"storageAuthKey",
					"storageConnectionDef",
					"storageConnectionPolicy",
					"storageController",
					"storageDomainEp",
					"storageDrive",
					"storageEnclosure",
					"storageEpUser",
					"storageEtherIf",
					"storageFcIf",
					"storageFcTargetEp",
					"storageFcTargetIf",
					"storageIScsiTargetIf",
					"storageIniGroup",
					"storageInitiator",
					"storageItem",
					"storageLocalDisk",
					"storageLocalDiskConfigDef",
					"storageLocalDiskConfigPolicy",
					"storageLocalDiskPartition",
					"storageLocalDiskSlotEp",
					"storageLocalLun",
					"storageLunDisk",
					"storageNodeEp",
					"storageQual",
					"storageRaidBattery",
					"storageSystem",
					"storageSystemFsm",
					"storageSystemFsmStage",
					"storageSystemFsmTask",
					"storageVirtualDrive",
					"storageVsanRef",
					"swAccessDomain",
					"swAccessDomainFsm",
					"swAccessDomainFsmStage",
					"swAccessDomainFsmTask",
					"swAccessEp",
					"swCardEnvStats",
					"swCardEnvStatsHist",
					"swEnvStats",
					"swEnvStatsHist",
					"swEthEstcEp",
					"swEthEstcPc",
					"swEthLanBorder",
					"swEthLanBorderFsm",
					"swEthLanBorderFsmStage",
					"swEthLanBorderFsmTask",
					"swEthLanEp",
					"swEthLanMon",
					"swEthLanPc",
					"swEthMon",
					"swEthMonDestEp",
					"swEthMonFsm",
					"swEthMonFsmStage",
					"swEthMonFsmTask",
					"swEthMonSrcEp",
					"swEthTargetEp",
					"swFabricZoneNs",
					"swFabricZoneNsOverride",
					"swFcEstcEp",
					"swFcMon",
					"swFcMonDestEp",
					"swFcMonFsm",
					"swFcMonFsmStage",
					"swFcMonFsmTask",
					"swFcMonSrcEp",
					"swFcSanBorder",
					"swFcSanBorderFsm",
					"swFcSanBorderFsmStage",
					"swFcSanBorderFsmTask",
					"swFcSanEp",
					"swFcSanMon",
					"swFcSanPc",
					"swFcServerZoneGroup",
					"swFcZone",
					"swFcZoneSet",
					"swFcoeEstcEp",
					"swFcoeSanEp",
					"swFcoeSanPc",
					"swPhys",
					"swPhysEtherEp",
					"swPhysFcEp",
					"swPhysFsm",
					"swPhysFsmStage",
					"swPhysFsmTask",
					"swSystemStats",
					"swSystemStatsHist",
					"swUlan",
					"swUtilityDomain",
					"swUtilityDomainFsm",
					"swUtilityDomainFsmStage",
					"swUtilityDomainFsmTask",
					"swVlan",
					"swVlanGroup",
					"swVlanPortNs",
					"swVlanPortNsOverride",
					"swVlanRef",
					"swVsan",
					"swZoneInitiatorMember",
					"swZoneTargetMember",
					"swatAction",
					"swatCondition",
					"swatInjection",
					"swatResultstats",
					"swatTarget",
					"swatTrigger",
					"syntheticDirectory",
					"syntheticFile",
					"syntheticFileSystem",
					"syntheticFsObj",
					"syntheticFsObjFsm",
					"syntheticFsObjFsmStage",
					"syntheticFsObjFsmTask",
					"syntheticTime",
					"sysdebugAutoCoreFileExportTarget",
					"sysdebugAutoCoreFileExportTargetFsm",
					"sysdebugAutoCoreFileExportTargetFsmStage",
					"sysdebugAutoCoreFileExportTargetFsmTask",
					"sysdebugBackupBehavior",
					"sysdebugCore",
					"sysdebugCoreFileRepository",
					"sysdebugCoreFsm",
					"sysdebugCoreFsmStage",
					"sysdebugCoreFsmTask",
					"sysdebugEp",
					"sysdebugLogControlDestinationFile",
					"sysdebugLogControlDestinationSyslog",
					"sysdebugLogControlDomain",
					"sysdebugLogControlEp",
					"sysdebugLogControlEpFsm",
					"sysdebugLogControlEpFsmStage",
					"sysdebugLogControlEpFsmTask",
					"sysdebugLogControlModule",
					"sysdebugMEpLog",
					"sysdebugMEpLogPolicy",
					"sysdebugManualCoreFileExportTarget",
					"sysdebugManualCoreFileExportTargetFsm",
					"sysdebugManualCoreFileExportTargetFsmStage",
					"sysdebugManualCoreFileExportTargetFsmTask",
					"sysdebugTechSupFileRepository",
					"sysdebugTechSupport",
					"sysdebugTechSupportCmdOpt",
					"sysdebugTechSupportFsm",
					"sysdebugTechSupportFsmStage",
					"sysdebugTechSupportFsmTask",
					"sysfileDigest",
					"sysfileMutation",
					"sysfileMutationFsm",
					"sysfileMutationFsmStage",
					"sysfileMutationFsmTask",
					"topMetaInf",
					"topRoot",
					"topSysDefaults",
					"topSystem",
					"trigAbsWindow",
					"trigClientToken",
					"trigLocalAbsWindow",
					"trigLocalSched",
					"trigMeta",
					"trigRecurrWindow",
					"trigSched",
					"trigTest",
					"trigTriggered",
					"uuidpoolAddr",
					"uuidpoolBlock",
					"uuidpoolFormat",
					"uuidpoolPool",
					"uuidpoolPoolable",
					"uuidpoolPooled",
					"uuidpoolUniverse",
					"versionApplication",
					"versionEp",
					"vmComputeEp",
					"vmDC",
					"vmDCOrg",
					"vmEp",
					"vmHba",
					"vmHv",
					"vmInstance",
					"vmLifeCyclePolicy",
					"vmLifeCyclePolicyFsm",
					"vmLifeCyclePolicyFsmStage",
					"vmLifeCyclePolicyFsmTask",
					"vmNic",
					"vmOrg",
					"vmSwitch",
					"vmVif",
					"vmVlan",
					"vmVnicProfCl",
					"vmVnicProfInst",
					"vmVsan",
					"vnicBootIpPolicy",
					"vnicBootTarget",
					"vnicConnDef",
					"vnicDefBeh",
					"vnicDynamicCon",
					"vnicDynamicConPolicy",
					"vnicDynamicConPolicyRef",
					"vnicDynamicIdUniverse",
					"vnicDynamicProvider",
					"vnicDynamicProviderEp",
					"vnicEthLif",
					"vnicEther",
					"vnicEtherIf",
					"vnicFc",
					"vnicFcGroupDef",
					"vnicFcGroupTempl",
					"vnicFcIf",
					"vnicFcLif",
					"vnicFcNode",
					"vnicFcOEIf",
					"vnicIPv4Dhcp",
					"vnicIPv4Dns",
					"vnicIPv4If",
					"vnicIPv4IscsiAddr",
					"vnicIPv4PooledIscsiAddr",
					"vnicIPv4StaticRoute",
					"vnicIScsi",
					"vnicIScsiAutoTargetIf",
					"vnicIScsiBootParams",
					"vnicIScsiBootVnic",
					"vnicIScsiLCP",
					"vnicIScsiNode",
					"vnicIScsiStaticTargetIf",
					"vnicInternalProfile",
					"vnicIpV4PooledAddr",
					"vnicIpV4ProfDerivedAddr",
					"vnicIpV4StaticAddr",
					"vnicIpc",
					"vnicIpcIf",
					"vnicLanConnPolicy",
					"vnicLanConnTempl",
					"vnicLifVlan",
					"vnicLifVsan",
					"vnicLun",
					"vnicOProfileAlias",
					"vnicProfile",
					"vnicProfileAlias",
					"vnicProfileSet",
					"vnicProfileSetFsm",
					"vnicProfileSetFsmStage",
					"vnicProfileSetFsmTask",
					"vnicRackServerDiscoveryProfile",
					"vnicSanConnPolicy",
					"vnicSanConnTempl",
					"vnicScsi",
					"vnicScsiIf",
					"vnicVhbaBehPolicy",
					"vnicVlan",
					"vnicVnicBehPolicy",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class ConfigMap(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ConfigMap")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("configMap")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"pair",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class ConfigSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "ConfigSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("configSet")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"aaaAuthRealm",
					"aaaAuthRealmFsm",
					"aaaAuthRealmFsmStage",
					"aaaConsoleAuth",
					"aaaDefaultAuth",
					"aaaDomain",
					"aaaDomainAuth",
					"aaaEpAuthProfile",
					"aaaEpFsm",
					"aaaEpFsmStage",
					"aaaEpFsmTask",
					"aaaEpLogin",
					"aaaEpUser",
					"aaaExtMgmtCutThruTkn",
					"aaaLdapEp",
					"aaaLdapEpFsm",
					"aaaLdapEpFsmStage",
					"aaaLdapGroup",
					"aaaLdapGroupRule",
					"aaaLdapProvider",
					"aaaLocale",
					"aaaLog",
					"aaaModLR",
					"aaaOrg",
					"aaaPreLoginBanner",
					"aaaProviderGroup",
					"aaaProviderRef",
					"aaaPwdProfile",
					"aaaRadiusEp",
					"aaaRadiusEpFsm",
					"aaaRadiusEpFsmStage",
					"aaaRadiusProvider",
					"aaaRealmFsm",
					"aaaRealmFsmStage",
					"aaaRealmFsmTask",
					"aaaRemoteUser",
					"aaaRole",
					"aaaSession",
					"aaaSessionLR",
					"aaaShellLogin",
					"aaaSshAuth",
					"aaaTacacsPlusEp",
					"aaaTacacsPlusEpFsm",
					"aaaTacacsPlusEpFsmStage",
					"aaaTacacsPlusProvider",
					"aaaUser",
					"aaaUserData",
					"aaaUserEp",
					"aaaUserEpFsm",
					"aaaUserEpFsmStage",
					"aaaUserEpFsmTask",
					"aaaUserLocale",
					"aaaUserRole",
					"aaaWebLogin",
					"adaptorCapQual",
					"adaptorCapSpec",
					"adaptorDiagCap",
					"adaptorEthCompQueueProfile",
					"adaptorEthFailoverProfile",
					"adaptorEthInterruptProfile",
					"adaptorEthOffloadProfile",
					"adaptorEthPortBySizeLargeStats",
					"adaptorEthPortBySizeLargeStatsHist",
					"adaptorEthPortBySizeSmallStats",
					"adaptorEthPortBySizeSmallStatsHist",
					"adaptorEthPortErrStats",
					"adaptorEthPortErrStatsHist",
					"adaptorEthPortMcastStats",
					"adaptorEthPortMcastStatsHist",
					"adaptorEthPortOutsizedStats",
					"adaptorEthPortOutsizedStatsHist",
					"adaptorEthPortStats",
					"adaptorEthPortStatsHist",
					"adaptorEthRecvQueueProfile",
					"adaptorEthWorkQueueProfile",
					"adaptorEtherIfStats",
					"adaptorEtherIfStatsHist",
					"adaptorExtEthIf",
					"adaptorExtEthIfFsm",
					"adaptorExtEthIfFsmStage",
					"adaptorExtEthIfFsmTask",
					"adaptorExtEthIfPc",
					"adaptorExtEthIfPcEp",
					"adaptorExtIpV6RssHashProfile",
					"adaptorFamilyTypeDef",
					"adaptorFcCdbWorkQueueProfile",
					"adaptorFcErrorRecoveryProfile",
					"adaptorFcIfEventStats",
					"adaptorFcIfEventStatsHist",
					"adaptorFcIfFC4Stats",
					"adaptorFcIfFC4StatsHist",
					"adaptorFcIfFrameStats",
					"adaptorFcIfFrameStatsHist",
					"adaptorFcInterruptProfile",
					"adaptorFcOEIf",
					"adaptorFcPortFLogiProfile",
					"adaptorFcPortPLogiProfile",
					"adaptorFcPortProfile",
					"adaptorFcPortStats",
					"adaptorFcPortStatsHist",
					"adaptorFcRecvQueueProfile",
					"adaptorFcWorkQueueProfile",
					"adaptorFruCapProvider",
					"adaptorFruCapRef",
					"adaptorFwCapProvider",
					"adaptorHostEthIf",
					"adaptorHostEthIfFsm",
					"adaptorHostEthIfFsmStage",
					"adaptorHostEthIfFsmTask",
					"adaptorHostEthIfProfile",
					"adaptorHostFcIf",
					"adaptorHostFcIfFsm",
					"adaptorHostFcIfFsmStage",
					"adaptorHostFcIfFsmTask",
					"adaptorHostFcIfProfile",
					"adaptorHostIscsiIf",
					"adaptorHostIscsiIfProfile",
					"adaptorHostMgmtCap",
					"adaptorHostethHwAddrCap",
					"adaptorHostfcHwAddrCap",
					"adaptorIScsiCap",
					"adaptorIpV4RssHashProfile",
					"adaptorIpV6RssHashProfile",
					"adaptorIscsiAuth",
					"adaptorIscsiProt",
					"adaptorIscsiTargetIf",
					"adaptorLanCap",
					"adaptorLldpCap",
					"adaptorMenloBaseErrorStats",
					"adaptorMenloBaseErrorStatsHist",
					"adaptorMenloDcePortStats",
					"adaptorMenloDcePortStatsHist",
					"adaptorMenloEthErrorStats",
					"adaptorMenloEthErrorStatsHist",
					"adaptorMenloEthStats",
					"adaptorMenloEthStatsHist",
					"adaptorMenloFcErrorStats",
					"adaptorMenloFcErrorStatsHist",
					"adaptorMenloFcStats",
					"adaptorMenloFcStatsHist",
					"adaptorMenloHostPortStats",
					"adaptorMenloHostPortStatsHist",
					"adaptorMenloMcpuErrorStats",
					"adaptorMenloMcpuErrorStatsHist",
					"adaptorMenloMcpuStats",
					"adaptorMenloMcpuStatsHist",
					"adaptorMenloNetEgStats",
					"adaptorMenloNetEgStatsHist",
					"adaptorMenloNetInStats",
					"adaptorMenloNetInStatsHist",
					"adaptorMenloQErrorStats",
					"adaptorMenloQErrorStatsHist",
					"adaptorMenloQStats",
					"adaptorMenloQStatsHist",
					"adaptorNwMgmtCap",
					"adaptorProtocolProfile",
					"adaptorQual",
					"adaptorRssProfile",
					"adaptorSanCap",
					"adaptorUnit",
					"adaptorUnitAssocCtx",
					"adaptorUnitExtn",
					"adaptorUplinkHwAddrCap",
					"adaptorVlan",
					"adaptorVnicStats",
					"adaptorVnicStatsHist",
					"adaptorVsan",
					"apeControllerChassis",
					"apeControllerEeprom",
					"apeControllerManager",
					"apeDcosAgManager",
					"apeFru",
					"apeHostAgent",
					"apeLANBoot",
					"apeLocalDiskBoot",
					"apeManager",
					"apeMc",
					"apeMcTable",
					"apeMenlo",
					"apeMenloVnic",
					"apeMenloVnicStats",
					"apeNicAgManager",
					"apePalo",
					"apePaloVnic",
					"apePaloVnicStats",
					"apeParam",
					"apeReading",
					"apeSANBoot",
					"apeSdr",
					"apeSwitchFirmwareInv",
					"apeVirtualMediaBoot",
					"biosBOT",
					"biosBootDev",
					"biosBootDevGrp",
					"biosFeatureRef",
					"biosParameterRef",
					"biosRef",
					"biosSettingRef",
					"biosSettings",
					"biosUnit",
					"biosVIdentityParams",
					"biosVProfile",
					"biosVfACPI10Support",
					"biosVfAssertNMIOnPERR",
					"biosVfAssertNMIOnSERR",
					"biosVfBootOptionRetry",
					"biosVfCPUPerformance",
					"biosVfConsoleRedirection",
					"biosVfCoreMultiProcessing",
					"biosVfDirectCacheAccess",
					"biosVfEnhancedIntelSpeedStepTech",
					"biosVfExecuteDisableBit",
					"biosVfFrontPanelLockout",
					"biosVfIntelEntrySASRAIDModule",
					"biosVfIntelHyperThreadingTech",
					"biosVfIntelTurboBoostTech",
					"biosVfIntelVTForDirectedIO",
					"biosVfIntelVirtualizationTechnology",
					"biosVfLvDIMMSupport",
					"biosVfMaxVariableMTRRSetting",
					"biosVfMaximumMemoryBelow4GB",
					"biosVfMemoryMappedIOAbove4GB",
					"biosVfMirroringMode",
					"biosVfNUMAOptimized",
					"biosVfOSBootWatchdogTimer",
					"biosVfOSBootWatchdogTimerPolicy",
					"biosVfOSBootWatchdogTimerTimeout",
					"biosVfOnboardSATAController",
					"biosVfOnboardStorage",
					"biosVfOptionROMEnable",
					"biosVfOptionROMLoad",
					"biosVfPCISlotOptionROMEnable",
					"biosVfPOSTErrorPause",
					"biosVfPackageCStateLimit",
					"biosVfProcessorC1E",
					"biosVfProcessorC3Report",
					"biosVfProcessorC6Report",
					"biosVfProcessorC7Report",
					"biosVfProcessorCState",
					"biosVfQuietBoot",
					"biosVfResumeOnACPowerLoss",
					"biosVfSelectMemoryRASConfiguration",
					"biosVfSerialPortAEnable",
					"biosVfSparingMode",
					"biosVfSriovConfig",
					"biosVfUCSMBootOrderRuleControl",
					"biosVfUEFIOSUseLegacyVideo",
					"biosVfUSBBootConfig",
					"biosVfUSBFrontPanelAccessLock",
					"biosVfUSBSystemIdlePowerOptimizingSetting",
					"bmcSELCounter",
					"callhomeDest",
					"callhomeEp",
					"callhomeEpFsm",
					"callhomeEpFsmStage",
					"callhomeEpFsmTask",
					"callhomePeriodicSystemInventory",
					"callhomePolicy",
					"callhomeProfile",
					"callhomeSmtp",
					"callhomeSource",
					"callhomeTestAlert",
					"capabilityCatalogue",
					"capabilityCatalogueFsm",
					"capabilityCatalogueFsmStage",
					"capabilityCatalogueFsmTask",
					"capabilityEp",
					"capabilityFeatureLimits",
					"capabilityMgmtExtension",
					"capabilityMgmtExtensionFsm",
					"capabilityMgmtExtensionFsmStage",
					"capabilityMgmtExtensionFsmTask",
					"capabilityNetworkLimits",
					"capabilityStorageLimits",
					"capabilitySystemLimits",
					"capabilityUpdate",
					"capabilityUpdater",
					"capabilityUpdaterFsm",
					"capabilityUpdaterFsmStage",
					"capabilityUpdaterFsmTask",
					"clitestTypeTest",
					"clitestTypeTest2",
					"clitestTypeTestChild",
					"commCimxml",
					"commDateTime",
					"commDns",
					"commDnsProvider",
					"commEvtChannel",
					"commHttp",
					"commHttps",
					"commNtpProvider",
					"commShellSvcLimits",
					"commSmashCLP",
					"commSnmp",
					"commSnmpTrap",
					"commSnmpUser",
					"commSsh",
					"commSvcEp",
					"commSvcEpFsm",
					"commSvcEpFsmStage",
					"commSvcEpFsmTask",
					"commSyslog",
					"commSyslogClient",
					"commSyslogConsole",
					"commSyslogFile",
					"commSyslogMonitor",
					"commSyslogSource",
					"commTelnet",
					"commWebChannel",
					"commWebSvcLimits",
					"commWsman",
					"commXmlClConnPolicy",
					"computeAutoconfigPolicy",
					"computeBlade",
					"computeBladeDiscPolicy",
					"computeBladeFsm",
					"computeBladeFsmStage",
					"computeBladeFsmTask",
					"computeBladeInheritPolicy",
					"computeBoard",
					"computeBoardController",
					"computeChassisConnPolicy",
					"computeChassisDiscPolicy",
					"computeChassisQual",
					"computeDefaults",
					"computeIOHub",
					"computeIOHubEnvStats",
					"computeIOHubEnvStatsHist",
					"computeMbPowerStats",
					"computeMbPowerStatsHist",
					"computeMbTempStats",
					"computeMbTempStatsHist",
					"computeMemoryUnitConstraintDef",
					"computePCIeFatalCompletionStats",
					"computePCIeFatalProtocolStats",
					"computePCIeFatalReceiveStats",
					"computePCIeFatalStats",
					"computePciCap",
					"computePciSlotScanDef",
					"computePhysicalAssocCtx",
					"computePhysicalFsm",
					"computePhysicalFsmStage",
					"computePhysicalFsmTask",
					"computePhysicalQual",
					"computePlatform",
					"computePnuOSImage",
					"computePool",
					"computePoolPolicyRef",
					"computePoolable",
					"computePooledRackUnit",
					"computePooledSlot",
					"computePoolingPolicy",
					"computePsuControl",
					"computePsuPolicy",
					"computeQual",
					"computeRackQual",
					"computeRackUnit",
					"computeRackUnitFsm",
					"computeRackUnitFsmStage",
					"computeRackUnitFsmTask",
					"computeRackUnitMbTempStats",
					"computeRackUnitMbTempStatsHist",
					"computeRtcBattery",
					"computeScrubPolicy",
					"computeServerDiscPolicy",
					"computeServerDiscPolicyFsm",
					"computeServerDiscPolicyFsmStage",
					"computeServerDiscPolicyFsmTask",
					"computeServerMgmtPolicy",
					"computeSlotQual",
					"configSorter",
					"dcxNs",
					"dcxUniverse",
					"dcxVIf",
					"dcxVc",
					"dcxVifEp",
					"dhcpAcquired",
					"dhcpInst",
					"dhcpLease",
					"diagBladeTest",
					"diagNetworkTest",
					"diagRslt",
					"diagRunPolicy",
					"diagSrvCapProvider",
					"diagSrvCtrl",
					"dpsecMac",
					"epqosDefinition",
					"epqosDefinitionDelTask",
					"epqosDefinitionDelTaskFsm",
					"epqosDefinitionDelTaskFsmStage",
					"epqosDefinitionDelTaskFsmTask",
					"epqosDefinitionFsm",
					"epqosDefinitionFsmStage",
					"epqosDefinitionFsmTask",
					"epqosEgress",
					"equipmentAdaptorConnDef",
					"equipmentAdaptorDef",
					"equipmentBaseBoardCapProvider",
					"equipmentBeaconCapProvider",
					"equipmentBeaconLed",
					"equipmentBeaconLedFsm",
					"equipmentBeaconLedFsmStage",
					"equipmentBeaconLedFsmTask",
					"equipmentBiosDef",
					"equipmentBladeAGLibrary",
					"equipmentBladeBiosCapProvider",
					"equipmentBladeCapProvider",
					"equipmentBladeConnDef",
					"equipmentBladeIOMConnDef",
					"equipmentBoardControllerDef",
					"equipmentCatalogCapProvider",
					"equipmentChassis",
					"equipmentChassisCapProvider",
					"equipmentChassisFsm",
					"equipmentChassisFsmStage",
					"equipmentChassisFsmTask",
					"equipmentChassisStats",
					"equipmentChassisStatsHist",
					"equipmentDbgPluginCapProvider",
					"equipmentDimmEntry",
					"equipmentDimmMapping",
					"equipmentDiscoveryCap",
					"equipmentFan",
					"equipmentFanModule",
					"equipmentFanModuleCapProvider",
					"equipmentFanModuleDef",
					"equipmentFanModuleStats",
					"equipmentFanModuleStatsHist",
					"equipmentFanStats",
					"equipmentFanStatsHist",
					"equipmentFex",
					"equipmentFexCapProvider",
					"equipmentFexEnvStats",
					"equipmentFexEnvStatsHist",
					"equipmentFexFsm",
					"equipmentFexFsmStage",
					"equipmentFexFsmTask",
					"equipmentFexPowerSummary",
					"equipmentFexPowerSummaryHist",
					"equipmentFexPsuInputStats",
					"equipmentFexPsuInputStatsHist",
					"equipmentGemCapProvider",
					"equipmentGemPortCap",
					"equipmentHDDFaultMonDef",
					"equipmentHostIfCapProvider",
					"equipmentIOCard",
					"equipmentIOCardCapProvider",
					"equipmentIOCardFsm",
					"equipmentIOCardFsmStage",
					"equipmentIOCardFsmTask",
					"equipmentIOCardStats",
					"equipmentIOCardStatsHist",
					"equipmentIOCardTypeDef",
					"equipmentIndicatorLed",
					"equipmentLocalDiskCapProvider",
					"equipmentLocalDiskControllerCapProvider",
					"equipmentLocalDiskControllerCapRef",
					"equipmentLocalDiskControllerDef",
					"equipmentLocalDiskDef",
					"equipmentLocatorLed",
					"equipmentLocatorLedFsm",
					"equipmentLocatorLedFsmStage",
					"equipmentLocatorLedFsmTask",
					"equipmentManufacturingDef",
					"equipmentMemoryUnitCapProvider",
					"equipmentMemoryUnitDiscoveryModifierDef",
					"equipmentMgmtCapProvider",
					"equipmentMgmtExtCapProvider",
					"equipmentNetworkElementFanStats",
					"equipmentNetworkElementFanStatsHist",
					"equipmentPOST",
					"equipmentPOSTCode",
					"equipmentPOSTCodeReporter",
					"equipmentPOSTCodeTemplate",
					"equipmentPciDef",
					"equipmentPhysicalDef",
					"equipmentPicture",
					"equipmentPortGroupAggregationDef",
					"equipmentPortGroupDef",
					"equipmentPortGroupSwComplexDef",
					"equipmentPortSwComplexRef",
					"equipmentProcessorUnitCapProvider",
					"equipmentProcessorUnitDef",
					"equipmentPsu",
					"equipmentPsuCapProvider",
					"equipmentPsuDef",
					"equipmentPsuInputStats",
					"equipmentPsuInputStatsHist",
					"equipmentPsuOutputStats",
					"equipmentPsuOutputStatsHist",
					"equipmentPsuStats",
					"equipmentPsuStatsHist",
					"equipmentRackUnitCapProvider",
					"equipmentRackUnitFanStats",
					"equipmentRackUnitFanStatsHist",
					"equipmentRackUnitPsuStats",
					"equipmentRackUnitPsuStatsHist",
					"equipmentRaidDef",
					"equipmentServerFeatureCap",
					"equipmentServiceDef",
					"equipmentSlotArray",
					"equipmentSlotArrayRef",
					"equipmentSwitchCap",
					"equipmentSwitchCapProvider",
					"equipmentSwitchCard",
					"equipmentUnifiedPortCapProvider",
					"equipmentXcvr",
					"etherErrStats",
					"etherErrStatsHist",
					"etherFcoeInterfaceStats",
					"etherFcoeInterfaceStatsHist",
					"etherLossStats",
					"etherLossStatsHist",
					"etherNicIfConfig",
					"etherPIo",
					"etherPIoEndPoint",
					"etherPIoFsm",
					"etherPIoFsmStage",
					"etherPauseStats",
					"etherPauseStatsHist",
					"etherPortChanIdElem",
					"etherPortChanIdUniverse",
					"etherRxStats",
					"etherRxStatsHist",
					"etherServerIntFIo",
					"etherServerIntFIoFsm",
					"etherServerIntFIoFsmStage",
					"etherServerIntFIoFsmTask",
					"etherServerIntFIoPc",
					"etherServerIntFIoPcEp",
					"etherSwIfConfig",
					"etherSwitchIntFIo",
					"etherSwitchIntFIoPc",
					"etherSwitchIntFIoPcEp",
					"etherTxStats",
					"etherTxStatsHist",
					"eventEpCtrl",
					"eventHolder",
					"eventInst",
					"eventLog",
					"eventPolicy",
					"eventRecord",
					"extmgmtArpTargets",
					"extmgmtGatewayPing",
					"extmgmtIf",
					"extmgmtIfMonPolicy",
					"extmgmtMiiStatus",
					"extpolClient",
					"extpolClientCont",
					"extpolController",
					"extpolControllerCont",
					"extpolEp",
					"extpolEpFsm",
					"extpolEpFsmStage",
					"extpolEpFsmTask",
					"extpolProvider",
					"extpolProviderCont",
					"extpolProviderFsm",
					"extpolProviderFsmStage",
					"extpolProviderFsmTask",
					"extpolRegistry",
					"extpolRegistryFsm",
					"extpolRegistryFsmStage",
					"extpolRegistryFsmTask",
					"extpolSystemContext",
					"extvmmEp",
					"extvmmEpFsm",
					"extvmmEpFsmStage",
					"extvmmEpFsmTask",
					"extvmmKeyInst",
					"extvmmKeyRing",
					"extvmmKeyStore",
					"extvmmKeyStoreFsm",
					"extvmmKeyStoreFsmStage",
					"extvmmKeyStoreFsmTask",
					"extvmmMasterExtKey",
					"extvmmMasterExtKeyFsm",
					"extvmmMasterExtKeyFsmStage",
					"extvmmMasterExtKeyFsmTask",
					"extvmmProvider",
					"extvmmProviderFsm",
					"extvmmProviderFsmStage",
					"extvmmProviderFsmTask",
					"extvmmSwitchDelTask",
					"extvmmSwitchDelTaskFsm",
					"extvmmSwitchDelTaskFsmStage",
					"extvmmSwitchDelTaskFsmTask",
					"extvmmSwitchSet",
					"fabricBHVlan",
					"fabricChassisEp",
					"fabricComputePhEp",
					"fabricComputeSlotEp",
					"fabricComputeSlotEpFsm",
					"fabricComputeSlotEpFsmStage",
					"fabricComputeSlotEpFsmTask",
					"fabricDceSrv",
					"fabricDceSwSrv",
					"fabricDceSwSrvEp",
					"fabricDceSwSrvPc",
					"fabricDceSwSrvPcEp",
					"fabricEp",
					"fabricEpMgr",
					"fabricEpMgrFsm",
					"fabricEpMgrFsmStage",
					"fabricEpMgrFsmTask",
					"fabricEthEstc",
					"fabricEthEstcCloud",
					"fabricEthEstcEp",
					"fabricEthEstcPc",
					"fabricEthEstcPcEp",
					"fabricEthLan",
					"fabricEthLanEp",
					"fabricEthLanPc",
					"fabricEthLanPcEp",
					"fabricEthMon",
					"fabricEthMonDestEp",
					"fabricEthMonFiltEp",
					"fabricEthMonFiltRef",
					"fabricEthMonLan",
					"fabricEthMonSrcEp",
					"fabricEthMonSrcRef",
					"fabricEthTargetEp",
					"fabricEthVlanPc",
					"fabricEthVlanPortEp",
					"fabricFcEstc",
					"fabricFcEstcCloud",
					"fabricFcEstcEp",
					"fabricFcMon",
					"fabricFcMonDestEp",
					"fabricFcMonFiltEp",
					"fabricFcMonFiltRef",
					"fabricFcMonSan",
					"fabricFcMonSrcEp",
					"fabricFcMonSrcRef",
					"fabricFcSan",
					"fabricFcSanEp",
					"fabricFcSanPc",
					"fabricFcSanPcEp",
					"fabricFcVsanPc",
					"fabricFcVsanPortEp",
					"fabricFcoeEstcEp",
					"fabricFcoeSanEp",
					"fabricFcoeSanPc",
					"fabricFcoeSanPcEp",
					"fabricFcoeVsanPc",
					"fabricFcoeVsanPortEp",
					"fabricIf",
					"fabricLanAccessMgr",
					"fabricLanCloud",
					"fabricLanCloudFsm",
					"fabricLanCloudFsmStage",
					"fabricLanCloudFsmTask",
					"fabricLanMonCloud",
					"fabricLanPinGroup",
					"fabricLanPinTarget",
					"fabricLastAckedSlot",
					"fabricLocale",
					"fabricMulticastPolicy",
					"fabricNetGroup",
					"fabricOrgVlanPolicy",
					"fabricPath",
					"fabricPathConn",
					"fabricPathEp",
					"fabricPoolableVlan",
					"fabricPooledVlan",
					"fabricSanCloud",
					"fabricSanCloudFsm",
					"fabricSanCloudFsmStage",
					"fabricSanCloudFsmTask",
					"fabricSanMonCloud",
					"fabricSanPinGroup",
					"fabricSanPinTarget",
					"fabricSwChPhEp",
					"fabricVCon",
					"fabricVConProfile",
					"fabricVlan",
					"fabricVlanEp",
					"fabricVlanGroupReq",
					"fabricVlanPermit",
					"fabricVlanReq",
					"fabricVsan",
					"fabricVsanEp",
					"fabricVsanMembership",
					"fabricZoneIdUniverse",
					"faultAffectedClass",
					"faultHolder",
					"faultInst",
					"faultLocalTypedHolder",
					"faultPolicy",
					"faultSuppressPolicy",
					"faultSuppressPolicyItem",
					"faultSuppressTask",
					"fcErrStats",
					"fcErrStatsHist",
					"fcNicIfConfig",
					"fcPIo",
					"fcPIoFsm",
					"fcPIoFsmStage",
					"fcStats",
					"fcStatsHist",
					"fcSwIfConfig",
					"fcpoolAddr",
					"fcpoolBlock",
					"fcpoolBootTarget",
					"fcpoolFormat",
					"fcpoolInitiator",
					"fcpoolInitiatorEp",
					"fcpoolInitiators",
					"fcpoolPoolable",
					"fcpoolUniverse",
					"firmwareAck",
					"firmwareBlade",
					"firmwareBootDefinition",
					"firmwareBootUnit",
					"firmwareBundleInfo",
					"firmwareBundleInfoDigest",
					"firmwareBundleType",
					"firmwareBundleTypeCapProvider",
					"firmwareCatalogPack",
					"firmwareCatalogue",
					"firmwareCompSource",
					"firmwareCompTarget",
					"firmwareComputeHostPack",
					"firmwareComputeMgmtPack",
					"firmwareDependency",
					"firmwareDistImage",
					"firmwareDistributable",
					"firmwareDistributableFsm",
					"firmwareDistributableFsmStage",
					"firmwareDistributableFsmTask",
					"firmwareDownloader",
					"firmwareDownloaderFsm",
					"firmwareDownloaderFsmStage",
					"firmwareDownloaderFsmTask",
					"firmwareHost",
					"firmwareHostPackModImpact",
					"firmwareImage",
					"firmwareImageFsm",
					"firmwareImageFsmStage",
					"firmwareImageFsmTask",
					"firmwareInfra",
					"firmwareInfraPack",
					"firmwareInstallImpact",
					"firmwareInstallable",
					"firmwarePackItem",
					"firmwareRack",
					"firmwareRunning",
					"firmwareSpec",
					"firmwareStatus",
					"firmwareSystem",
					"firmwareSystemCompCheckResult",
					"firmwareSystemFsm",
					"firmwareSystemFsmStage",
					"firmwareSystemFsmTask",
					"firmwareType",
					"firmwareUpdatable",
					"firmwareUpgradeConstraint",
					"firmwareUpgradeDetail",
					"firmwareUpgradeInfo",
					"flowctrlDefinition",
					"flowctrlItem",
					"fsmStatus",
					"hostimgPolicy",
					"hostimgTarget",
					"identIdentCtx",
					"identIdentRequest",
					"identIdentRequestFsm",
					"identIdentRequestFsmStage",
					"identIdentRequestFsmTask",
					"identMetaSystem",
					"identMetaSystemFsm",
					"identMetaSystemFsmStage",
					"identMetaSystemFsmTask",
					"identMetaVerse",
					"identRequestEp",
					"identSysInfo",
					"imgprovPolicy",
					"imgprovTarget",
					"imgsecKey",
					"imgsecPolicy",
					"initiatorFcInitiatorEp",
					"initiatorGroupEp",
					"initiatorIScsiInitiatorEp",
					"initiatorLunEp",
					"initiatorMemberEp",
					"initiatorRequestorEp",
					"initiatorRequestorGrpEp",
					"initiatorStoreEp",
					"initiatorUnitEp",
					"ipIPv4Dns",
					"ipIpV4StaticAddr",
					"ipServiceIf",
					"ippoolAddr",
					"ippoolBlock",
					"ippoolPool",
					"ippoolPoolable",
					"ippoolPooled",
					"ippoolUniverse",
					"iqnpoolAddr",
					"iqnpoolBlock",
					"iqnpoolFormat",
					"iqnpoolPool",
					"iqnpoolPoolable",
					"iqnpoolPooled",
					"iqnpoolUniverse",
					"iscsiAuthProfile",
					"iscsiProtocolProfile",
					"licenseContents",
					"licenseDownloader",
					"licenseDownloaderFsm",
					"licenseDownloaderFsmStage",
					"licenseDownloaderFsmTask",
					"licenseEp",
					"licenseFeature",
					"licenseFeatureCapProvider",
					"licenseFeatureLine",
					"licenseFile",
					"licenseFileFsm",
					"licenseFileFsmStage",
					"licenseFileFsmTask",
					"licenseInstance",
					"licenseInstanceFsm",
					"licenseInstanceFsmStage",
					"licenseInstanceFsmTask",
					"licenseProp",
					"licenseServerHostId",
					"licenseSource",
					"licenseSourceFile",
					"lldpAcquired",
					"lsAgentPolicy",
					"lsBinding",
					"lsFcLocale",
					"lsFcZone",
					"lsFcZoneGroup",
					"lsPower",
					"lsRequirement",
					"lsServer",
					"lsServerAssocCtx",
					"lsServerFsm",
					"lsServerFsmStage",
					"lsServerFsmTask",
					"lsTier",
					"lsVConAssign",
					"lsVersionBeh",
					"lsZoneInitiatorMember",
					"lsZoneTargetMember",
					"lsbootDef",
					"lsbootIScsi",
					"lsbootIScsiImagePath",
					"lsbootLan",
					"lsbootLanImagePath",
					"lsbootLocalStorage",
					"lsbootPolicy",
					"lsbootSanImage",
					"lsbootSanImagePath",
					"lsbootStorage",
					"lsbootVirtualMedia",
					"lsmaintAck",
					"lsmaintMaintPolicy",
					"macpoolAddr",
					"macpoolBlock",
					"macpoolFormat",
					"macpoolPool",
					"macpoolPoolable",
					"macpoolPooled",
					"macpoolUniverse",
					"managedObject",
					"memoryArray",
					"memoryArrayEnvStats",
					"memoryArrayEnvStatsHist",
					"memoryBufferUnit",
					"memoryBufferUnitEnvStats",
					"memoryBufferUnitEnvStatsHist",
					"memoryErrorStats",
					"memoryQual",
					"memoryRuntime",
					"memoryRuntimeHist",
					"memoryUnit",
					"memoryUnitEnvStats",
					"memoryUnitEnvStatsHist",
					"mgmtAccessPolicy",
					"mgmtAccessPolicyItem",
					"mgmtAccessPort",
					"mgmtBackup",
					"mgmtBackupFsm",
					"mgmtBackupFsmStage",
					"mgmtBackupFsmTask",
					"mgmtBackupPolicy",
					"mgmtBackupPolicyFsm",
					"mgmtBackupPolicyFsmStage",
					"mgmtCfgExportPolicy",
					"mgmtCfgExportPolicyFsm",
					"mgmtCfgExportPolicyFsmStage",
					"mgmtConnection",
					"mgmtController",
					"mgmtControllerFsm",
					"mgmtControllerFsmStage",
					"mgmtControllerFsmTask",
					"mgmtEntity",
					"mgmtExportPolicyFsm",
					"mgmtExportPolicyFsmStage",
					"mgmtExportPolicyFsmTask",
					"mgmtIf",
					"mgmtIfFsm",
					"mgmtIfFsmStage",
					"mgmtIfFsmTask",
					"mgmtImporter",
					"mgmtImporterFsm",
					"mgmtImporterFsmStage",
					"mgmtImporterFsmTask",
					"mgmtIntAuthPolicy",
					"mgmtPmonEntry",
					"networkElement",
					"networkIfStats",
					"nfsEp",
					"nfsMountDef",
					"nfsMountDefFsm",
					"nfsMountDefFsmStage",
					"nfsMountDefFsmTask",
					"nfsMountInst",
					"nfsMountInstFsm",
					"nfsMountInstFsmStage",
					"nfsMountInstFsmTask",
					"nwctrlDefinition",
					"observe",
					"observeObserved",
					"observeObservedCont",
					"observeObservedFsm",
					"observeObservedFsmStage",
					"observeObservedFsmTask",
					"orgOrg",
					"osAgent",
					"osInstance",
					"pciEquipSlot",
					"pciUnit",
					"pkiCertReq",
					"pkiEp",
					"pkiEpFsm",
					"pkiEpFsmStage",
					"pkiEpFsmTask",
					"pkiKeyRing",
					"pkiTP",
					"policyCommunication",
					"policyConfigBackup",
					"policyControlEp",
					"policyControlEpFsm",
					"policyControlEpFsmStage",
					"policyControlEpFsmTask",
					"policyControlledInstance",
					"policyControlledType",
					"policyDateTime",
					"policyDigest",
					"policyDiscovery",
					"policyDns",
					"policyFault",
					"policyInfraFirmware",
					"policyMEp",
					"policyMonitoring",
					"policyPolicyEp",
					"policyPolicyRequestor",
					"policyPolicyScope",
					"policyPolicyScopeCont",
					"policyPolicyScopeContext",
					"policyPolicyScopeFsm",
					"policyPolicyScopeFsmStage",
					"policyPolicyScopeFsmTask",
					"policyPowerMgmt",
					"policyPsu",
					"policySecurity",
					"portDomainEp",
					"portGroup",
					"portPIoFsm",
					"portPIoFsmStage",
					"portPIoFsmTask",
					"portTrustMode",
					"powerBudget",
					"powerChassisMember",
					"powerEp",
					"powerGroup",
					"powerGroupAdditionPolicy",
					"powerGroupQual",
					"powerGroupStats",
					"powerGroupStatsHist",
					"powerMgmtPolicy",
					"powerPlacement",
					"powerPolicy",
					"powerPrioWght",
					"powerRackUnitMember",
					"procDoer",
					"procManager",
					"procPrt",
					"procPrtCounts",
					"procStimulusCounts",
					"procSvc",
					"procTxCounts",
					"processorCore",
					"processorEnvStats",
					"processorEnvStatsHist",
					"processorErrorStats",
					"processorQual",
					"processorRuntime",
					"processorRuntimeHist",
					"processorThread",
					"processorUnit",
					"processorUnitAssocCtx",
					"qosclassDefinition",
					"qosclassDefinitionFsm",
					"qosclassDefinitionFsmStage",
					"qosclassDefinitionFsmTask",
					"qosclassEthBE",
					"qosclassEthClassified",
					"qosclassFc",
					"solConfig",
					"solIf",
					"solPolicy",
					"statsCollectionPolicy",
					"statsCollectionPolicyFsm",
					"statsCollectionPolicyFsmStage",
					"statsCollectionPolicyFsmTask",
					"statsHolder",
					"statsThr32Definition",
					"statsThr32Value",
					"statsThr64Definition",
					"statsThr64Value",
					"statsThrFloatDefinition",
					"statsThrFloatValue",
					"statsThresholdClass",
					"statsThresholdPolicy",
					"storageAuthKey",
					"storageConnectionDef",
					"storageConnectionPolicy",
					"storageController",
					"storageDomainEp",
					"storageDrive",
					"storageEnclosure",
					"storageEpUser",
					"storageEtherIf",
					"storageFcIf",
					"storageFcTargetEp",
					"storageFcTargetIf",
					"storageIScsiTargetIf",
					"storageIniGroup",
					"storageInitiator",
					"storageItem",
					"storageLocalDisk",
					"storageLocalDiskConfigDef",
					"storageLocalDiskConfigPolicy",
					"storageLocalDiskPartition",
					"storageLocalDiskSlotEp",
					"storageLocalLun",
					"storageLunDisk",
					"storageNodeEp",
					"storageQual",
					"storageRaidBattery",
					"storageSystem",
					"storageSystemFsm",
					"storageSystemFsmStage",
					"storageSystemFsmTask",
					"storageVirtualDrive",
					"storageVsanRef",
					"swAccessDomain",
					"swAccessDomainFsm",
					"swAccessDomainFsmStage",
					"swAccessDomainFsmTask",
					"swAccessEp",
					"swCardEnvStats",
					"swCardEnvStatsHist",
					"swEnvStats",
					"swEnvStatsHist",
					"swEthEstcEp",
					"swEthEstcPc",
					"swEthLanBorder",
					"swEthLanBorderFsm",
					"swEthLanBorderFsmStage",
					"swEthLanBorderFsmTask",
					"swEthLanEp",
					"swEthLanMon",
					"swEthLanPc",
					"swEthMon",
					"swEthMonDestEp",
					"swEthMonFsm",
					"swEthMonFsmStage",
					"swEthMonFsmTask",
					"swEthMonSrcEp",
					"swEthTargetEp",
					"swFabricZoneNs",
					"swFabricZoneNsOverride",
					"swFcEstcEp",
					"swFcMon",
					"swFcMonDestEp",
					"swFcMonFsm",
					"swFcMonFsmStage",
					"swFcMonFsmTask",
					"swFcMonSrcEp",
					"swFcSanBorder",
					"swFcSanBorderFsm",
					"swFcSanBorderFsmStage",
					"swFcSanBorderFsmTask",
					"swFcSanEp",
					"swFcSanMon",
					"swFcSanPc",
					"swFcServerZoneGroup",
					"swFcZone",
					"swFcZoneSet",
					"swFcoeEstcEp",
					"swFcoeSanEp",
					"swFcoeSanPc",
					"swPhys",
					"swPhysEtherEp",
					"swPhysFcEp",
					"swPhysFsm",
					"swPhysFsmStage",
					"swPhysFsmTask",
					"swSystemStats",
					"swSystemStatsHist",
					"swUlan",
					"swUtilityDomain",
					"swUtilityDomainFsm",
					"swUtilityDomainFsmStage",
					"swUtilityDomainFsmTask",
					"swVlan",
					"swVlanGroup",
					"swVlanPortNs",
					"swVlanPortNsOverride",
					"swVlanRef",
					"swVsan",
					"swZoneInitiatorMember",
					"swZoneTargetMember",
					"swatAction",
					"swatCondition",
					"swatInjection",
					"swatResultstats",
					"swatTarget",
					"swatTrigger",
					"syntheticDirectory",
					"syntheticFile",
					"syntheticFileSystem",
					"syntheticFsObj",
					"syntheticFsObjFsm",
					"syntheticFsObjFsmStage",
					"syntheticFsObjFsmTask",
					"syntheticTime",
					"sysdebugAutoCoreFileExportTarget",
					"sysdebugAutoCoreFileExportTargetFsm",
					"sysdebugAutoCoreFileExportTargetFsmStage",
					"sysdebugAutoCoreFileExportTargetFsmTask",
					"sysdebugBackupBehavior",
					"sysdebugCore",
					"sysdebugCoreFileRepository",
					"sysdebugCoreFsm",
					"sysdebugCoreFsmStage",
					"sysdebugCoreFsmTask",
					"sysdebugEp",
					"sysdebugLogControlDestinationFile",
					"sysdebugLogControlDestinationSyslog",
					"sysdebugLogControlDomain",
					"sysdebugLogControlEp",
					"sysdebugLogControlEpFsm",
					"sysdebugLogControlEpFsmStage",
					"sysdebugLogControlEpFsmTask",
					"sysdebugLogControlModule",
					"sysdebugMEpLog",
					"sysdebugMEpLogPolicy",
					"sysdebugManualCoreFileExportTarget",
					"sysdebugManualCoreFileExportTargetFsm",
					"sysdebugManualCoreFileExportTargetFsmStage",
					"sysdebugManualCoreFileExportTargetFsmTask",
					"sysdebugTechSupFileRepository",
					"sysdebugTechSupport",
					"sysdebugTechSupportCmdOpt",
					"sysdebugTechSupportFsm",
					"sysdebugTechSupportFsmStage",
					"sysdebugTechSupportFsmTask",
					"sysfileDigest",
					"sysfileMutation",
					"sysfileMutationFsm",
					"sysfileMutationFsmStage",
					"sysfileMutationFsmTask",
					"topMetaInf",
					"topRoot",
					"topSysDefaults",
					"topSystem",
					"trigAbsWindow",
					"trigClientToken",
					"trigLocalAbsWindow",
					"trigLocalSched",
					"trigMeta",
					"trigRecurrWindow",
					"trigSched",
					"trigTest",
					"trigTriggered",
					"uuidpoolAddr",
					"uuidpoolBlock",
					"uuidpoolFormat",
					"uuidpoolPool",
					"uuidpoolPoolable",
					"uuidpoolPooled",
					"uuidpoolUniverse",
					"versionApplication",
					"versionEp",
					"vmComputeEp",
					"vmDC",
					"vmDCOrg",
					"vmEp",
					"vmHba",
					"vmHv",
					"vmInstance",
					"vmLifeCyclePolicy",
					"vmLifeCyclePolicyFsm",
					"vmLifeCyclePolicyFsmStage",
					"vmLifeCyclePolicyFsmTask",
					"vmNic",
					"vmOrg",
					"vmSwitch",
					"vmVif",
					"vmVlan",
					"vmVnicProfCl",
					"vmVnicProfInst",
					"vmVsan",
					"vnicBootIpPolicy",
					"vnicBootTarget",
					"vnicConnDef",
					"vnicDefBeh",
					"vnicDynamicCon",
					"vnicDynamicConPolicy",
					"vnicDynamicConPolicyRef",
					"vnicDynamicIdUniverse",
					"vnicDynamicProvider",
					"vnicDynamicProviderEp",
					"vnicEthLif",
					"vnicEther",
					"vnicEtherIf",
					"vnicFc",
					"vnicFcGroupDef",
					"vnicFcGroupTempl",
					"vnicFcIf",
					"vnicFcLif",
					"vnicFcNode",
					"vnicFcOEIf",
					"vnicIPv4Dhcp",
					"vnicIPv4Dns",
					"vnicIPv4If",
					"vnicIPv4IscsiAddr",
					"vnicIPv4PooledIscsiAddr",
					"vnicIPv4StaticRoute",
					"vnicIScsi",
					"vnicIScsiAutoTargetIf",
					"vnicIScsiBootParams",
					"vnicIScsiBootVnic",
					"vnicIScsiLCP",
					"vnicIScsiNode",
					"vnicIScsiStaticTargetIf",
					"vnicInternalProfile",
					"vnicIpV4PooledAddr",
					"vnicIpV4ProfDerivedAddr",
					"vnicIpV4StaticAddr",
					"vnicIpc",
					"vnicIpcIf",
					"vnicLanConnPolicy",
					"vnicLanConnTempl",
					"vnicLifVlan",
					"vnicLifVsan",
					"vnicLun",
					"vnicOProfileAlias",
					"vnicProfile",
					"vnicProfileAlias",
					"vnicProfileSet",
					"vnicProfileSetFsm",
					"vnicProfileSetFsmStage",
					"vnicProfileSetFsmTask",
					"vnicRackServerDiscoveryProfile",
					"vnicSanConnPolicy",
					"vnicSanConnTempl",
					"vnicScsi",
					"vnicScsiIf",
					"vnicVhbaBehPolicy",
					"vnicVlan",
					"vnicVnicBehPolicy",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class Dn(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "Dn")
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("dn")
		else:
			x = w.createElement(elementName)
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class DnSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "DnSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("dnSet")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"dn",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class EqFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "EqFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("eq")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class FilterFilter(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "FilterFilter")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("filter")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"abstractFilter",
					"allbits",
					"and",
					"anybit",
					"bw",
					"eq",
					"ge",
					"gt",
					"le",
					"lt",
					"ne",
					"not",
					"or",
					"wcard",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class GeFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "GeFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("ge")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class GtFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "GtFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("gt")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class Id(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "Id")
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("id")
		else:
			x = w.createElement(elementName)
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class IdSet(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "IdSet")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("idSet")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"id",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class LeFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "LeFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("le")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class LtFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "LtFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("lt")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class NeFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "NeFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("ne")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class NotFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "NotFilter")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("not")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"abstractFilter",
					"allbits",
					"and",
					"anybit",
					"bw",
					"eq",
					"ge",
					"gt",
					"le",
					"lt",
					"ne",
					"not",
					"or",
					"wcard",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class OrFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "OrFilter")

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("or")
		else:
			x = w.createElement(elementName)
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"abstractFilter",
					"allbits",
					"and",
					"anybit",
					"bw",
					"eq",
					"ge",
					"gt",
					"le",
					"lt",
					"ne",
					"not",
					"or",
					"wcard",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class Pair(UcsBase):
	def __init__(self):
		UcsBase.__init__(self, "Pair")
		self.Key = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("pair")
		else:
			x = w.createElement(elementName)
		x.setAttribute("key", getattr(self,"Key"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
					"aaaAuthRealm",
					"aaaAuthRealmFsm",
					"aaaAuthRealmFsmStage",
					"aaaConsoleAuth",
					"aaaDefaultAuth",
					"aaaDomain",
					"aaaDomainAuth",
					"aaaEpAuthProfile",
					"aaaEpFsm",
					"aaaEpFsmStage",
					"aaaEpFsmTask",
					"aaaEpLogin",
					"aaaEpUser",
					"aaaExtMgmtCutThruTkn",
					"aaaLdapEp",
					"aaaLdapEpFsm",
					"aaaLdapEpFsmStage",
					"aaaLdapGroup",
					"aaaLdapGroupRule",
					"aaaLdapProvider",
					"aaaLocale",
					"aaaLog",
					"aaaModLR",
					"aaaOrg",
					"aaaPreLoginBanner",
					"aaaProviderGroup",
					"aaaProviderRef",
					"aaaPwdProfile",
					"aaaRadiusEp",
					"aaaRadiusEpFsm",
					"aaaRadiusEpFsmStage",
					"aaaRadiusProvider",
					"aaaRealmFsm",
					"aaaRealmFsmStage",
					"aaaRealmFsmTask",
					"aaaRemoteUser",
					"aaaRole",
					"aaaSession",
					"aaaSessionLR",
					"aaaShellLogin",
					"aaaSshAuth",
					"aaaTacacsPlusEp",
					"aaaTacacsPlusEpFsm",
					"aaaTacacsPlusEpFsmStage",
					"aaaTacacsPlusProvider",
					"aaaUser",
					"aaaUserData",
					"aaaUserEp",
					"aaaUserEpFsm",
					"aaaUserEpFsmStage",
					"aaaUserEpFsmTask",
					"aaaUserLocale",
					"aaaUserRole",
					"aaaWebLogin",
					"adaptorCapQual",
					"adaptorCapSpec",
					"adaptorDiagCap",
					"adaptorEthCompQueueProfile",
					"adaptorEthFailoverProfile",
					"adaptorEthInterruptProfile",
					"adaptorEthOffloadProfile",
					"adaptorEthPortBySizeLargeStats",
					"adaptorEthPortBySizeLargeStatsHist",
					"adaptorEthPortBySizeSmallStats",
					"adaptorEthPortBySizeSmallStatsHist",
					"adaptorEthPortErrStats",
					"adaptorEthPortErrStatsHist",
					"adaptorEthPortMcastStats",
					"adaptorEthPortMcastStatsHist",
					"adaptorEthPortOutsizedStats",
					"adaptorEthPortOutsizedStatsHist",
					"adaptorEthPortStats",
					"adaptorEthPortStatsHist",
					"adaptorEthRecvQueueProfile",
					"adaptorEthWorkQueueProfile",
					"adaptorEtherIfStats",
					"adaptorEtherIfStatsHist",
					"adaptorExtEthIf",
					"adaptorExtEthIfFsm",
					"adaptorExtEthIfFsmStage",
					"adaptorExtEthIfFsmTask",
					"adaptorExtEthIfPc",
					"adaptorExtEthIfPcEp",
					"adaptorExtIpV6RssHashProfile",
					"adaptorFamilyTypeDef",
					"adaptorFcCdbWorkQueueProfile",
					"adaptorFcErrorRecoveryProfile",
					"adaptorFcIfEventStats",
					"adaptorFcIfEventStatsHist",
					"adaptorFcIfFC4Stats",
					"adaptorFcIfFC4StatsHist",
					"adaptorFcIfFrameStats",
					"adaptorFcIfFrameStatsHist",
					"adaptorFcInterruptProfile",
					"adaptorFcOEIf",
					"adaptorFcPortFLogiProfile",
					"adaptorFcPortPLogiProfile",
					"adaptorFcPortProfile",
					"adaptorFcPortStats",
					"adaptorFcPortStatsHist",
					"adaptorFcRecvQueueProfile",
					"adaptorFcWorkQueueProfile",
					"adaptorFruCapProvider",
					"adaptorFruCapRef",
					"adaptorFwCapProvider",
					"adaptorHostEthIf",
					"adaptorHostEthIfFsm",
					"adaptorHostEthIfFsmStage",
					"adaptorHostEthIfFsmTask",
					"adaptorHostEthIfProfile",
					"adaptorHostFcIf",
					"adaptorHostFcIfFsm",
					"adaptorHostFcIfFsmStage",
					"adaptorHostFcIfFsmTask",
					"adaptorHostFcIfProfile",
					"adaptorHostIscsiIf",
					"adaptorHostIscsiIfProfile",
					"adaptorHostMgmtCap",
					"adaptorHostethHwAddrCap",
					"adaptorHostfcHwAddrCap",
					"adaptorIScsiCap",
					"adaptorIpV4RssHashProfile",
					"adaptorIpV6RssHashProfile",
					"adaptorIscsiAuth",
					"adaptorIscsiProt",
					"adaptorIscsiTargetIf",
					"adaptorLanCap",
					"adaptorLldpCap",
					"adaptorMenloBaseErrorStats",
					"adaptorMenloBaseErrorStatsHist",
					"adaptorMenloDcePortStats",
					"adaptorMenloDcePortStatsHist",
					"adaptorMenloEthErrorStats",
					"adaptorMenloEthErrorStatsHist",
					"adaptorMenloEthStats",
					"adaptorMenloEthStatsHist",
					"adaptorMenloFcErrorStats",
					"adaptorMenloFcErrorStatsHist",
					"adaptorMenloFcStats",
					"adaptorMenloFcStatsHist",
					"adaptorMenloHostPortStats",
					"adaptorMenloHostPortStatsHist",
					"adaptorMenloMcpuErrorStats",
					"adaptorMenloMcpuErrorStatsHist",
					"adaptorMenloMcpuStats",
					"adaptorMenloMcpuStatsHist",
					"adaptorMenloNetEgStats",
					"adaptorMenloNetEgStatsHist",
					"adaptorMenloNetInStats",
					"adaptorMenloNetInStatsHist",
					"adaptorMenloQErrorStats",
					"adaptorMenloQErrorStatsHist",
					"adaptorMenloQStats",
					"adaptorMenloQStatsHist",
					"adaptorNwMgmtCap",
					"adaptorProtocolProfile",
					"adaptorQual",
					"adaptorRssProfile",
					"adaptorSanCap",
					"adaptorUnit",
					"adaptorUnitAssocCtx",
					"adaptorUnitExtn",
					"adaptorUplinkHwAddrCap",
					"adaptorVlan",
					"adaptorVnicStats",
					"adaptorVnicStatsHist",
					"adaptorVsan",
					"apeControllerChassis",
					"apeControllerEeprom",
					"apeControllerManager",
					"apeDcosAgManager",
					"apeFru",
					"apeHostAgent",
					"apeLANBoot",
					"apeLocalDiskBoot",
					"apeManager",
					"apeMc",
					"apeMcTable",
					"apeMenlo",
					"apeMenloVnic",
					"apeMenloVnicStats",
					"apeNicAgManager",
					"apePalo",
					"apePaloVnic",
					"apePaloVnicStats",
					"apeParam",
					"apeReading",
					"apeSANBoot",
					"apeSdr",
					"apeSwitchFirmwareInv",
					"apeVirtualMediaBoot",
					"biosBOT",
					"biosBootDev",
					"biosBootDevGrp",
					"biosFeatureRef",
					"biosParameterRef",
					"biosRef",
					"biosSettingRef",
					"biosSettings",
					"biosUnit",
					"biosVIdentityParams",
					"biosVProfile",
					"biosVfACPI10Support",
					"biosVfAssertNMIOnPERR",
					"biosVfAssertNMIOnSERR",
					"biosVfBootOptionRetry",
					"biosVfCPUPerformance",
					"biosVfConsoleRedirection",
					"biosVfCoreMultiProcessing",
					"biosVfDirectCacheAccess",
					"biosVfEnhancedIntelSpeedStepTech",
					"biosVfExecuteDisableBit",
					"biosVfFrontPanelLockout",
					"biosVfIntelEntrySASRAIDModule",
					"biosVfIntelHyperThreadingTech",
					"biosVfIntelTurboBoostTech",
					"biosVfIntelVTForDirectedIO",
					"biosVfIntelVirtualizationTechnology",
					"biosVfLvDIMMSupport",
					"biosVfMaxVariableMTRRSetting",
					"biosVfMaximumMemoryBelow4GB",
					"biosVfMemoryMappedIOAbove4GB",
					"biosVfMirroringMode",
					"biosVfNUMAOptimized",
					"biosVfOSBootWatchdogTimer",
					"biosVfOSBootWatchdogTimerPolicy",
					"biosVfOSBootWatchdogTimerTimeout",
					"biosVfOnboardSATAController",
					"biosVfOnboardStorage",
					"biosVfOptionROMEnable",
					"biosVfOptionROMLoad",
					"biosVfPCISlotOptionROMEnable",
					"biosVfPOSTErrorPause",
					"biosVfPackageCStateLimit",
					"biosVfProcessorC1E",
					"biosVfProcessorC3Report",
					"biosVfProcessorC6Report",
					"biosVfProcessorC7Report",
					"biosVfProcessorCState",
					"biosVfQuietBoot",
					"biosVfResumeOnACPowerLoss",
					"biosVfSelectMemoryRASConfiguration",
					"biosVfSerialPortAEnable",
					"biosVfSparingMode",
					"biosVfSriovConfig",
					"biosVfUCSMBootOrderRuleControl",
					"biosVfUEFIOSUseLegacyVideo",
					"biosVfUSBBootConfig",
					"biosVfUSBFrontPanelAccessLock",
					"biosVfUSBSystemIdlePowerOptimizingSetting",
					"bmcSELCounter",
					"callhomeDest",
					"callhomeEp",
					"callhomeEpFsm",
					"callhomeEpFsmStage",
					"callhomeEpFsmTask",
					"callhomePeriodicSystemInventory",
					"callhomePolicy",
					"callhomeProfile",
					"callhomeSmtp",
					"callhomeSource",
					"callhomeTestAlert",
					"capabilityCatalogue",
					"capabilityCatalogueFsm",
					"capabilityCatalogueFsmStage",
					"capabilityCatalogueFsmTask",
					"capabilityEp",
					"capabilityFeatureLimits",
					"capabilityMgmtExtension",
					"capabilityMgmtExtensionFsm",
					"capabilityMgmtExtensionFsmStage",
					"capabilityMgmtExtensionFsmTask",
					"capabilityNetworkLimits",
					"capabilityStorageLimits",
					"capabilitySystemLimits",
					"capabilityUpdate",
					"capabilityUpdater",
					"capabilityUpdaterFsm",
					"capabilityUpdaterFsmStage",
					"capabilityUpdaterFsmTask",
					"clitestTypeTest",
					"clitestTypeTest2",
					"clitestTypeTestChild",
					"commCimxml",
					"commDateTime",
					"commDns",
					"commDnsProvider",
					"commEvtChannel",
					"commHttp",
					"commHttps",
					"commNtpProvider",
					"commShellSvcLimits",
					"commSmashCLP",
					"commSnmp",
					"commSnmpTrap",
					"commSnmpUser",
					"commSsh",
					"commSvcEp",
					"commSvcEpFsm",
					"commSvcEpFsmStage",
					"commSvcEpFsmTask",
					"commSyslog",
					"commSyslogClient",
					"commSyslogConsole",
					"commSyslogFile",
					"commSyslogMonitor",
					"commSyslogSource",
					"commTelnet",
					"commWebChannel",
					"commWebSvcLimits",
					"commWsman",
					"commXmlClConnPolicy",
					"computeAutoconfigPolicy",
					"computeBlade",
					"computeBladeDiscPolicy",
					"computeBladeFsm",
					"computeBladeFsmStage",
					"computeBladeFsmTask",
					"computeBladeInheritPolicy",
					"computeBoard",
					"computeBoardController",
					"computeChassisConnPolicy",
					"computeChassisDiscPolicy",
					"computeChassisQual",
					"computeDefaults",
					"computeIOHub",
					"computeIOHubEnvStats",
					"computeIOHubEnvStatsHist",
					"computeMbPowerStats",
					"computeMbPowerStatsHist",
					"computeMbTempStats",
					"computeMbTempStatsHist",
					"computeMemoryUnitConstraintDef",
					"computePCIeFatalCompletionStats",
					"computePCIeFatalProtocolStats",
					"computePCIeFatalReceiveStats",
					"computePCIeFatalStats",
					"computePciCap",
					"computePciSlotScanDef",
					"computePhysicalAssocCtx",
					"computePhysicalFsm",
					"computePhysicalFsmStage",
					"computePhysicalFsmTask",
					"computePhysicalQual",
					"computePlatform",
					"computePnuOSImage",
					"computePool",
					"computePoolPolicyRef",
					"computePoolable",
					"computePooledRackUnit",
					"computePooledSlot",
					"computePoolingPolicy",
					"computePsuControl",
					"computePsuPolicy",
					"computeQual",
					"computeRackQual",
					"computeRackUnit",
					"computeRackUnitFsm",
					"computeRackUnitFsmStage",
					"computeRackUnitFsmTask",
					"computeRackUnitMbTempStats",
					"computeRackUnitMbTempStatsHist",
					"computeRtcBattery",
					"computeScrubPolicy",
					"computeServerDiscPolicy",
					"computeServerDiscPolicyFsm",
					"computeServerDiscPolicyFsmStage",
					"computeServerDiscPolicyFsmTask",
					"computeServerMgmtPolicy",
					"computeSlotQual",
					"configSorter",
					"dcxNs",
					"dcxUniverse",
					"dcxVIf",
					"dcxVc",
					"dcxVifEp",
					"dhcpAcquired",
					"dhcpInst",
					"dhcpLease",
					"diagBladeTest",
					"diagNetworkTest",
					"diagRslt",
					"diagRunPolicy",
					"diagSrvCapProvider",
					"diagSrvCtrl",
					"dpsecMac",
					"epqosDefinition",
					"epqosDefinitionDelTask",
					"epqosDefinitionDelTaskFsm",
					"epqosDefinitionDelTaskFsmStage",
					"epqosDefinitionDelTaskFsmTask",
					"epqosDefinitionFsm",
					"epqosDefinitionFsmStage",
					"epqosDefinitionFsmTask",
					"epqosEgress",
					"equipmentAdaptorConnDef",
					"equipmentAdaptorDef",
					"equipmentBaseBoardCapProvider",
					"equipmentBeaconCapProvider",
					"equipmentBeaconLed",
					"equipmentBeaconLedFsm",
					"equipmentBeaconLedFsmStage",
					"equipmentBeaconLedFsmTask",
					"equipmentBiosDef",
					"equipmentBladeAGLibrary",
					"equipmentBladeBiosCapProvider",
					"equipmentBladeCapProvider",
					"equipmentBladeConnDef",
					"equipmentBladeIOMConnDef",
					"equipmentBoardControllerDef",
					"equipmentCatalogCapProvider",
					"equipmentChassis",
					"equipmentChassisCapProvider",
					"equipmentChassisFsm",
					"equipmentChassisFsmStage",
					"equipmentChassisFsmTask",
					"equipmentChassisStats",
					"equipmentChassisStatsHist",
					"equipmentDbgPluginCapProvider",
					"equipmentDimmEntry",
					"equipmentDimmMapping",
					"equipmentDiscoveryCap",
					"equipmentFan",
					"equipmentFanModule",
					"equipmentFanModuleCapProvider",
					"equipmentFanModuleDef",
					"equipmentFanModuleStats",
					"equipmentFanModuleStatsHist",
					"equipmentFanStats",
					"equipmentFanStatsHist",
					"equipmentFex",
					"equipmentFexCapProvider",
					"equipmentFexEnvStats",
					"equipmentFexEnvStatsHist",
					"equipmentFexFsm",
					"equipmentFexFsmStage",
					"equipmentFexFsmTask",
					"equipmentFexPowerSummary",
					"equipmentFexPowerSummaryHist",
					"equipmentFexPsuInputStats",
					"equipmentFexPsuInputStatsHist",
					"equipmentGemCapProvider",
					"equipmentGemPortCap",
					"equipmentHDDFaultMonDef",
					"equipmentHostIfCapProvider",
					"equipmentIOCard",
					"equipmentIOCardCapProvider",
					"equipmentIOCardFsm",
					"equipmentIOCardFsmStage",
					"equipmentIOCardFsmTask",
					"equipmentIOCardStats",
					"equipmentIOCardStatsHist",
					"equipmentIOCardTypeDef",
					"equipmentIndicatorLed",
					"equipmentLocalDiskCapProvider",
					"equipmentLocalDiskControllerCapProvider",
					"equipmentLocalDiskControllerCapRef",
					"equipmentLocalDiskControllerDef",
					"equipmentLocalDiskDef",
					"equipmentLocatorLed",
					"equipmentLocatorLedFsm",
					"equipmentLocatorLedFsmStage",
					"equipmentLocatorLedFsmTask",
					"equipmentManufacturingDef",
					"equipmentMemoryUnitCapProvider",
					"equipmentMemoryUnitDiscoveryModifierDef",
					"equipmentMgmtCapProvider",
					"equipmentMgmtExtCapProvider",
					"equipmentNetworkElementFanStats",
					"equipmentNetworkElementFanStatsHist",
					"equipmentPOST",
					"equipmentPOSTCode",
					"equipmentPOSTCodeReporter",
					"equipmentPOSTCodeTemplate",
					"equipmentPciDef",
					"equipmentPhysicalDef",
					"equipmentPicture",
					"equipmentPortGroupAggregationDef",
					"equipmentPortGroupDef",
					"equipmentPortGroupSwComplexDef",
					"equipmentPortSwComplexRef",
					"equipmentProcessorUnitCapProvider",
					"equipmentProcessorUnitDef",
					"equipmentPsu",
					"equipmentPsuCapProvider",
					"equipmentPsuDef",
					"equipmentPsuInputStats",
					"equipmentPsuInputStatsHist",
					"equipmentPsuOutputStats",
					"equipmentPsuOutputStatsHist",
					"equipmentPsuStats",
					"equipmentPsuStatsHist",
					"equipmentRackUnitCapProvider",
					"equipmentRackUnitFanStats",
					"equipmentRackUnitFanStatsHist",
					"equipmentRackUnitPsuStats",
					"equipmentRackUnitPsuStatsHist",
					"equipmentRaidDef",
					"equipmentServerFeatureCap",
					"equipmentServiceDef",
					"equipmentSlotArray",
					"equipmentSlotArrayRef",
					"equipmentSwitchCap",
					"equipmentSwitchCapProvider",
					"equipmentSwitchCard",
					"equipmentUnifiedPortCapProvider",
					"equipmentXcvr",
					"etherErrStats",
					"etherErrStatsHist",
					"etherFcoeInterfaceStats",
					"etherFcoeInterfaceStatsHist",
					"etherLossStats",
					"etherLossStatsHist",
					"etherNicIfConfig",
					"etherPIo",
					"etherPIoEndPoint",
					"etherPIoFsm",
					"etherPIoFsmStage",
					"etherPauseStats",
					"etherPauseStatsHist",
					"etherPortChanIdElem",
					"etherPortChanIdUniverse",
					"etherRxStats",
					"etherRxStatsHist",
					"etherServerIntFIo",
					"etherServerIntFIoFsm",
					"etherServerIntFIoFsmStage",
					"etherServerIntFIoFsmTask",
					"etherServerIntFIoPc",
					"etherServerIntFIoPcEp",
					"etherSwIfConfig",
					"etherSwitchIntFIo",
					"etherSwitchIntFIoPc",
					"etherSwitchIntFIoPcEp",
					"etherTxStats",
					"etherTxStatsHist",
					"eventEpCtrl",
					"eventHolder",
					"eventInst",
					"eventLog",
					"eventPolicy",
					"eventRecord",
					"extmgmtArpTargets",
					"extmgmtGatewayPing",
					"extmgmtIf",
					"extmgmtIfMonPolicy",
					"extmgmtMiiStatus",
					"extpolClient",
					"extpolClientCont",
					"extpolController",
					"extpolControllerCont",
					"extpolEp",
					"extpolEpFsm",
					"extpolEpFsmStage",
					"extpolEpFsmTask",
					"extpolProvider",
					"extpolProviderCont",
					"extpolProviderFsm",
					"extpolProviderFsmStage",
					"extpolProviderFsmTask",
					"extpolRegistry",
					"extpolRegistryFsm",
					"extpolRegistryFsmStage",
					"extpolRegistryFsmTask",
					"extpolSystemContext",
					"extvmmEp",
					"extvmmEpFsm",
					"extvmmEpFsmStage",
					"extvmmEpFsmTask",
					"extvmmKeyInst",
					"extvmmKeyRing",
					"extvmmKeyStore",
					"extvmmKeyStoreFsm",
					"extvmmKeyStoreFsmStage",
					"extvmmKeyStoreFsmTask",
					"extvmmMasterExtKey",
					"extvmmMasterExtKeyFsm",
					"extvmmMasterExtKeyFsmStage",
					"extvmmMasterExtKeyFsmTask",
					"extvmmProvider",
					"extvmmProviderFsm",
					"extvmmProviderFsmStage",
					"extvmmProviderFsmTask",
					"extvmmSwitchDelTask",
					"extvmmSwitchDelTaskFsm",
					"extvmmSwitchDelTaskFsmStage",
					"extvmmSwitchDelTaskFsmTask",
					"extvmmSwitchSet",
					"fabricBHVlan",
					"fabricChassisEp",
					"fabricComputePhEp",
					"fabricComputeSlotEp",
					"fabricComputeSlotEpFsm",
					"fabricComputeSlotEpFsmStage",
					"fabricComputeSlotEpFsmTask",
					"fabricDceSrv",
					"fabricDceSwSrv",
					"fabricDceSwSrvEp",
					"fabricDceSwSrvPc",
					"fabricDceSwSrvPcEp",
					"fabricEp",
					"fabricEpMgr",
					"fabricEpMgrFsm",
					"fabricEpMgrFsmStage",
					"fabricEpMgrFsmTask",
					"fabricEthEstc",
					"fabricEthEstcCloud",
					"fabricEthEstcEp",
					"fabricEthEstcPc",
					"fabricEthEstcPcEp",
					"fabricEthLan",
					"fabricEthLanEp",
					"fabricEthLanPc",
					"fabricEthLanPcEp",
					"fabricEthMon",
					"fabricEthMonDestEp",
					"fabricEthMonFiltEp",
					"fabricEthMonFiltRef",
					"fabricEthMonLan",
					"fabricEthMonSrcEp",
					"fabricEthMonSrcRef",
					"fabricEthTargetEp",
					"fabricEthVlanPc",
					"fabricEthVlanPortEp",
					"fabricFcEstc",
					"fabricFcEstcCloud",
					"fabricFcEstcEp",
					"fabricFcMon",
					"fabricFcMonDestEp",
					"fabricFcMonFiltEp",
					"fabricFcMonFiltRef",
					"fabricFcMonSan",
					"fabricFcMonSrcEp",
					"fabricFcMonSrcRef",
					"fabricFcSan",
					"fabricFcSanEp",
					"fabricFcSanPc",
					"fabricFcSanPcEp",
					"fabricFcVsanPc",
					"fabricFcVsanPortEp",
					"fabricFcoeEstcEp",
					"fabricFcoeSanEp",
					"fabricFcoeSanPc",
					"fabricFcoeSanPcEp",
					"fabricFcoeVsanPc",
					"fabricFcoeVsanPortEp",
					"fabricIf",
					"fabricLanAccessMgr",
					"fabricLanCloud",
					"fabricLanCloudFsm",
					"fabricLanCloudFsmStage",
					"fabricLanCloudFsmTask",
					"fabricLanMonCloud",
					"fabricLanPinGroup",
					"fabricLanPinTarget",
					"fabricLastAckedSlot",
					"fabricLocale",
					"fabricMulticastPolicy",
					"fabricNetGroup",
					"fabricOrgVlanPolicy",
					"fabricPath",
					"fabricPathConn",
					"fabricPathEp",
					"fabricPoolableVlan",
					"fabricPooledVlan",
					"fabricSanCloud",
					"fabricSanCloudFsm",
					"fabricSanCloudFsmStage",
					"fabricSanCloudFsmTask",
					"fabricSanMonCloud",
					"fabricSanPinGroup",
					"fabricSanPinTarget",
					"fabricSwChPhEp",
					"fabricVCon",
					"fabricVConProfile",
					"fabricVlan",
					"fabricVlanEp",
					"fabricVlanGroupReq",
					"fabricVlanPermit",
					"fabricVlanReq",
					"fabricVsan",
					"fabricVsanEp",
					"fabricVsanMembership",
					"fabricZoneIdUniverse",
					"faultAffectedClass",
					"faultHolder",
					"faultInst",
					"faultLocalTypedHolder",
					"faultPolicy",
					"faultSuppressPolicy",
					"faultSuppressPolicyItem",
					"faultSuppressTask",
					"fcErrStats",
					"fcErrStatsHist",
					"fcNicIfConfig",
					"fcPIo",
					"fcPIoFsm",
					"fcPIoFsmStage",
					"fcStats",
					"fcStatsHist",
					"fcSwIfConfig",
					"fcpoolAddr",
					"fcpoolBlock",
					"fcpoolBootTarget",
					"fcpoolFormat",
					"fcpoolInitiator",
					"fcpoolInitiatorEp",
					"fcpoolInitiators",
					"fcpoolPoolable",
					"fcpoolUniverse",
					"firmwareAck",
					"firmwareBlade",
					"firmwareBootDefinition",
					"firmwareBootUnit",
					"firmwareBundleInfo",
					"firmwareBundleInfoDigest",
					"firmwareBundleType",
					"firmwareBundleTypeCapProvider",
					"firmwareCatalogPack",
					"firmwareCatalogue",
					"firmwareCompSource",
					"firmwareCompTarget",
					"firmwareComputeHostPack",
					"firmwareComputeMgmtPack",
					"firmwareDependency",
					"firmwareDistImage",
					"firmwareDistributable",
					"firmwareDistributableFsm",
					"firmwareDistributableFsmStage",
					"firmwareDistributableFsmTask",
					"firmwareDownloader",
					"firmwareDownloaderFsm",
					"firmwareDownloaderFsmStage",
					"firmwareDownloaderFsmTask",
					"firmwareHost",
					"firmwareHostPackModImpact",
					"firmwareImage",
					"firmwareImageFsm",
					"firmwareImageFsmStage",
					"firmwareImageFsmTask",
					"firmwareInfra",
					"firmwareInfraPack",
					"firmwareInstallImpact",
					"firmwareInstallable",
					"firmwarePackItem",
					"firmwareRack",
					"firmwareRunning",
					"firmwareSpec",
					"firmwareStatus",
					"firmwareSystem",
					"firmwareSystemCompCheckResult",
					"firmwareSystemFsm",
					"firmwareSystemFsmStage",
					"firmwareSystemFsmTask",
					"firmwareType",
					"firmwareUpdatable",
					"firmwareUpgradeConstraint",
					"firmwareUpgradeDetail",
					"firmwareUpgradeInfo",
					"flowctrlDefinition",
					"flowctrlItem",
					"fsmStatus",
					"hostimgPolicy",
					"hostimgTarget",
					"identIdentCtx",
					"identIdentRequest",
					"identIdentRequestFsm",
					"identIdentRequestFsmStage",
					"identIdentRequestFsmTask",
					"identMetaSystem",
					"identMetaSystemFsm",
					"identMetaSystemFsmStage",
					"identMetaSystemFsmTask",
					"identMetaVerse",
					"identRequestEp",
					"identSysInfo",
					"imgprovPolicy",
					"imgprovTarget",
					"imgsecKey",
					"imgsecPolicy",
					"initiatorFcInitiatorEp",
					"initiatorGroupEp",
					"initiatorIScsiInitiatorEp",
					"initiatorLunEp",
					"initiatorMemberEp",
					"initiatorRequestorEp",
					"initiatorRequestorGrpEp",
					"initiatorStoreEp",
					"initiatorUnitEp",
					"ipIPv4Dns",
					"ipIpV4StaticAddr",
					"ipServiceIf",
					"ippoolAddr",
					"ippoolBlock",
					"ippoolPool",
					"ippoolPoolable",
					"ippoolPooled",
					"ippoolUniverse",
					"iqnpoolAddr",
					"iqnpoolBlock",
					"iqnpoolFormat",
					"iqnpoolPool",
					"iqnpoolPoolable",
					"iqnpoolPooled",
					"iqnpoolUniverse",
					"iscsiAuthProfile",
					"iscsiProtocolProfile",
					"licenseContents",
					"licenseDownloader",
					"licenseDownloaderFsm",
					"licenseDownloaderFsmStage",
					"licenseDownloaderFsmTask",
					"licenseEp",
					"licenseFeature",
					"licenseFeatureCapProvider",
					"licenseFeatureLine",
					"licenseFile",
					"licenseFileFsm",
					"licenseFileFsmStage",
					"licenseFileFsmTask",
					"licenseInstance",
					"licenseInstanceFsm",
					"licenseInstanceFsmStage",
					"licenseInstanceFsmTask",
					"licenseProp",
					"licenseServerHostId",
					"licenseSource",
					"licenseSourceFile",
					"lldpAcquired",
					"lsAgentPolicy",
					"lsBinding",
					"lsFcLocale",
					"lsFcZone",
					"lsFcZoneGroup",
					"lsPower",
					"lsRequirement",
					"lsServer",
					"lsServerAssocCtx",
					"lsServerFsm",
					"lsServerFsmStage",
					"lsServerFsmTask",
					"lsTier",
					"lsVConAssign",
					"lsVersionBeh",
					"lsZoneInitiatorMember",
					"lsZoneTargetMember",
					"lsbootDef",
					"lsbootIScsi",
					"lsbootIScsiImagePath",
					"lsbootLan",
					"lsbootLanImagePath",
					"lsbootLocalStorage",
					"lsbootPolicy",
					"lsbootSanImage",
					"lsbootSanImagePath",
					"lsbootStorage",
					"lsbootVirtualMedia",
					"lsmaintAck",
					"lsmaintMaintPolicy",
					"macpoolAddr",
					"macpoolBlock",
					"macpoolFormat",
					"macpoolPool",
					"macpoolPoolable",
					"macpoolPooled",
					"macpoolUniverse",
					"managedObject",
					"memoryArray",
					"memoryArrayEnvStats",
					"memoryArrayEnvStatsHist",
					"memoryBufferUnit",
					"memoryBufferUnitEnvStats",
					"memoryBufferUnitEnvStatsHist",
					"memoryErrorStats",
					"memoryQual",
					"memoryRuntime",
					"memoryRuntimeHist",
					"memoryUnit",
					"memoryUnitEnvStats",
					"memoryUnitEnvStatsHist",
					"mgmtAccessPolicy",
					"mgmtAccessPolicyItem",
					"mgmtAccessPort",
					"mgmtBackup",
					"mgmtBackupFsm",
					"mgmtBackupFsmStage",
					"mgmtBackupFsmTask",
					"mgmtBackupPolicy",
					"mgmtBackupPolicyFsm",
					"mgmtBackupPolicyFsmStage",
					"mgmtCfgExportPolicy",
					"mgmtCfgExportPolicyFsm",
					"mgmtCfgExportPolicyFsmStage",
					"mgmtConnection",
					"mgmtController",
					"mgmtControllerFsm",
					"mgmtControllerFsmStage",
					"mgmtControllerFsmTask",
					"mgmtEntity",
					"mgmtExportPolicyFsm",
					"mgmtExportPolicyFsmStage",
					"mgmtExportPolicyFsmTask",
					"mgmtIf",
					"mgmtIfFsm",
					"mgmtIfFsmStage",
					"mgmtIfFsmTask",
					"mgmtImporter",
					"mgmtImporterFsm",
					"mgmtImporterFsmStage",
					"mgmtImporterFsmTask",
					"mgmtIntAuthPolicy",
					"mgmtPmonEntry",
					"networkElement",
					"networkIfStats",
					"nfsEp",
					"nfsMountDef",
					"nfsMountDefFsm",
					"nfsMountDefFsmStage",
					"nfsMountDefFsmTask",
					"nfsMountInst",
					"nfsMountInstFsm",
					"nfsMountInstFsmStage",
					"nfsMountInstFsmTask",
					"nwctrlDefinition",
					"observe",
					"observeObserved",
					"observeObservedCont",
					"observeObservedFsm",
					"observeObservedFsmStage",
					"observeObservedFsmTask",
					"orgOrg",
					"osAgent",
					"osInstance",
					"pciEquipSlot",
					"pciUnit",
					"pkiCertReq",
					"pkiEp",
					"pkiEpFsm",
					"pkiEpFsmStage",
					"pkiEpFsmTask",
					"pkiKeyRing",
					"pkiTP",
					"policyCommunication",
					"policyConfigBackup",
					"policyControlEp",
					"policyControlEpFsm",
					"policyControlEpFsmStage",
					"policyControlEpFsmTask",
					"policyControlledInstance",
					"policyControlledType",
					"policyDateTime",
					"policyDigest",
					"policyDiscovery",
					"policyDns",
					"policyFault",
					"policyInfraFirmware",
					"policyMEp",
					"policyMonitoring",
					"policyPolicyEp",
					"policyPolicyRequestor",
					"policyPolicyScope",
					"policyPolicyScopeCont",
					"policyPolicyScopeContext",
					"policyPolicyScopeFsm",
					"policyPolicyScopeFsmStage",
					"policyPolicyScopeFsmTask",
					"policyPowerMgmt",
					"policyPsu",
					"policySecurity",
					"portDomainEp",
					"portGroup",
					"portPIoFsm",
					"portPIoFsmStage",
					"portPIoFsmTask",
					"portTrustMode",
					"powerBudget",
					"powerChassisMember",
					"powerEp",
					"powerGroup",
					"powerGroupAdditionPolicy",
					"powerGroupQual",
					"powerGroupStats",
					"powerGroupStatsHist",
					"powerMgmtPolicy",
					"powerPlacement",
					"powerPolicy",
					"powerPrioWght",
					"powerRackUnitMember",
					"procDoer",
					"procManager",
					"procPrt",
					"procPrtCounts",
					"procStimulusCounts",
					"procSvc",
					"procTxCounts",
					"processorCore",
					"processorEnvStats",
					"processorEnvStatsHist",
					"processorErrorStats",
					"processorQual",
					"processorRuntime",
					"processorRuntimeHist",
					"processorThread",
					"processorUnit",
					"processorUnitAssocCtx",
					"qosclassDefinition",
					"qosclassDefinitionFsm",
					"qosclassDefinitionFsmStage",
					"qosclassDefinitionFsmTask",
					"qosclassEthBE",
					"qosclassEthClassified",
					"qosclassFc",
					"solConfig",
					"solIf",
					"solPolicy",
					"statsCollectionPolicy",
					"statsCollectionPolicyFsm",
					"statsCollectionPolicyFsmStage",
					"statsCollectionPolicyFsmTask",
					"statsHolder",
					"statsThr32Definition",
					"statsThr32Value",
					"statsThr64Definition",
					"statsThr64Value",
					"statsThrFloatDefinition",
					"statsThrFloatValue",
					"statsThresholdClass",
					"statsThresholdPolicy",
					"storageAuthKey",
					"storageConnectionDef",
					"storageConnectionPolicy",
					"storageController",
					"storageDomainEp",
					"storageDrive",
					"storageEnclosure",
					"storageEpUser",
					"storageEtherIf",
					"storageFcIf",
					"storageFcTargetEp",
					"storageFcTargetIf",
					"storageIScsiTargetIf",
					"storageIniGroup",
					"storageInitiator",
					"storageItem",
					"storageLocalDisk",
					"storageLocalDiskConfigDef",
					"storageLocalDiskConfigPolicy",
					"storageLocalDiskPartition",
					"storageLocalDiskSlotEp",
					"storageLocalLun",
					"storageLunDisk",
					"storageNodeEp",
					"storageQual",
					"storageRaidBattery",
					"storageSystem",
					"storageSystemFsm",
					"storageSystemFsmStage",
					"storageSystemFsmTask",
					"storageVirtualDrive",
					"storageVsanRef",
					"swAccessDomain",
					"swAccessDomainFsm",
					"swAccessDomainFsmStage",
					"swAccessDomainFsmTask",
					"swAccessEp",
					"swCardEnvStats",
					"swCardEnvStatsHist",
					"swEnvStats",
					"swEnvStatsHist",
					"swEthEstcEp",
					"swEthEstcPc",
					"swEthLanBorder",
					"swEthLanBorderFsm",
					"swEthLanBorderFsmStage",
					"swEthLanBorderFsmTask",
					"swEthLanEp",
					"swEthLanMon",
					"swEthLanPc",
					"swEthMon",
					"swEthMonDestEp",
					"swEthMonFsm",
					"swEthMonFsmStage",
					"swEthMonFsmTask",
					"swEthMonSrcEp",
					"swEthTargetEp",
					"swFabricZoneNs",
					"swFabricZoneNsOverride",
					"swFcEstcEp",
					"swFcMon",
					"swFcMonDestEp",
					"swFcMonFsm",
					"swFcMonFsmStage",
					"swFcMonFsmTask",
					"swFcMonSrcEp",
					"swFcSanBorder",
					"swFcSanBorderFsm",
					"swFcSanBorderFsmStage",
					"swFcSanBorderFsmTask",
					"swFcSanEp",
					"swFcSanMon",
					"swFcSanPc",
					"swFcServerZoneGroup",
					"swFcZone",
					"swFcZoneSet",
					"swFcoeEstcEp",
					"swFcoeSanEp",
					"swFcoeSanPc",
					"swPhys",
					"swPhysEtherEp",
					"swPhysFcEp",
					"swPhysFsm",
					"swPhysFsmStage",
					"swPhysFsmTask",
					"swSystemStats",
					"swSystemStatsHist",
					"swUlan",
					"swUtilityDomain",
					"swUtilityDomainFsm",
					"swUtilityDomainFsmStage",
					"swUtilityDomainFsmTask",
					"swVlan",
					"swVlanGroup",
					"swVlanPortNs",
					"swVlanPortNsOverride",
					"swVlanRef",
					"swVsan",
					"swZoneInitiatorMember",
					"swZoneTargetMember",
					"swatAction",
					"swatCondition",
					"swatInjection",
					"swatResultstats",
					"swatTarget",
					"swatTrigger",
					"syntheticDirectory",
					"syntheticFile",
					"syntheticFileSystem",
					"syntheticFsObj",
					"syntheticFsObjFsm",
					"syntheticFsObjFsmStage",
					"syntheticFsObjFsmTask",
					"syntheticTime",
					"sysdebugAutoCoreFileExportTarget",
					"sysdebugAutoCoreFileExportTargetFsm",
					"sysdebugAutoCoreFileExportTargetFsmStage",
					"sysdebugAutoCoreFileExportTargetFsmTask",
					"sysdebugBackupBehavior",
					"sysdebugCore",
					"sysdebugCoreFileRepository",
					"sysdebugCoreFsm",
					"sysdebugCoreFsmStage",
					"sysdebugCoreFsmTask",
					"sysdebugEp",
					"sysdebugLogControlDestinationFile",
					"sysdebugLogControlDestinationSyslog",
					"sysdebugLogControlDomain",
					"sysdebugLogControlEp",
					"sysdebugLogControlEpFsm",
					"sysdebugLogControlEpFsmStage",
					"sysdebugLogControlEpFsmTask",
					"sysdebugLogControlModule",
					"sysdebugMEpLog",
					"sysdebugMEpLogPolicy",
					"sysdebugManualCoreFileExportTarget",
					"sysdebugManualCoreFileExportTargetFsm",
					"sysdebugManualCoreFileExportTargetFsmStage",
					"sysdebugManualCoreFileExportTargetFsmTask",
					"sysdebugTechSupFileRepository",
					"sysdebugTechSupport",
					"sysdebugTechSupportCmdOpt",
					"sysdebugTechSupportFsm",
					"sysdebugTechSupportFsmStage",
					"sysdebugTechSupportFsmTask",
					"sysfileDigest",
					"sysfileMutation",
					"sysfileMutationFsm",
					"sysfileMutationFsmStage",
					"sysfileMutationFsmTask",
					"topMetaInf",
					"topRoot",
					"topSysDefaults",
					"topSystem",
					"trigAbsWindow",
					"trigClientToken",
					"trigLocalAbsWindow",
					"trigLocalSched",
					"trigMeta",
					"trigRecurrWindow",
					"trigSched",
					"trigTest",
					"trigTriggered",
					"uuidpoolAddr",
					"uuidpoolBlock",
					"uuidpoolFormat",
					"uuidpoolPool",
					"uuidpoolPoolable",
					"uuidpoolPooled",
					"uuidpoolUniverse",
					"versionApplication",
					"versionEp",
					"vmComputeEp",
					"vmDC",
					"vmDCOrg",
					"vmEp",
					"vmHba",
					"vmHv",
					"vmInstance",
					"vmLifeCyclePolicy",
					"vmLifeCyclePolicyFsm",
					"vmLifeCyclePolicyFsmStage",
					"vmLifeCyclePolicyFsmTask",
					"vmNic",
					"vmOrg",
					"vmSwitch",
					"vmVif",
					"vmVlan",
					"vmVnicProfCl",
					"vmVnicProfInst",
					"vmVsan",
					"vnicBootIpPolicy",
					"vnicBootTarget",
					"vnicConnDef",
					"vnicDefBeh",
					"vnicDynamicCon",
					"vnicDynamicConPolicy",
					"vnicDynamicConPolicyRef",
					"vnicDynamicIdUniverse",
					"vnicDynamicProvider",
					"vnicDynamicProviderEp",
					"vnicEthLif",
					"vnicEther",
					"vnicEtherIf",
					"vnicFc",
					"vnicFcGroupDef",
					"vnicFcGroupTempl",
					"vnicFcIf",
					"vnicFcLif",
					"vnicFcNode",
					"vnicFcOEIf",
					"vnicIPv4Dhcp",
					"vnicIPv4Dns",
					"vnicIPv4If",
					"vnicIPv4IscsiAddr",
					"vnicIPv4PooledIscsiAddr",
					"vnicIPv4StaticRoute",
					"vnicIScsi",
					"vnicIScsiAutoTargetIf",
					"vnicIScsiBootParams",
					"vnicIScsiBootVnic",
					"vnicIScsiLCP",
					"vnicIScsiNode",
					"vnicIScsiStaticTargetIf",
					"vnicInternalProfile",
					"vnicIpV4PooledAddr",
					"vnicIpV4ProfDerivedAddr",
					"vnicIpV4StaticAddr",
					"vnicIpc",
					"vnicIpcIf",
					"vnicLanConnPolicy",
					"vnicLanConnTempl",
					"vnicLifVlan",
					"vnicLifVsan",
					"vnicLun",
					"vnicOProfileAlias",
					"vnicProfile",
					"vnicProfileAlias",
					"vnicProfileSet",
					"vnicProfileSetFsm",
					"vnicProfileSetFsmStage",
					"vnicProfileSetFsmTask",
					"vnicRackServerDiscoveryProfile",
					"vnicSanConnPolicy",
					"vnicSanConnTempl",
					"vnicScsi",
					"vnicScsiIf",
					"vnicVhbaBehPolicy",
					"vnicVlan",
					"vnicVnicBehPolicy",
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

class WcardFilter(AbstractFilter):
	def __init__(self):
		UcsBase.__init__(self, "WcardFilter")
		self.Class = None
		self.Property = None
		self.Value = None

	def AddChild(self, mo):
		self.child.append(mo)

	def WriteXml(self, w, option, elementName=None):
		if (elementName == None):
			x = w.createElement("wcard")
		else:
			x = w.createElement(elementName)
		x.setAttribute("class", getattr(self,"Class"));
		x.setAttribute("property", getattr(self,"Property"));
		x.setAttribute("value", getattr(self,"Value"));
		x_child = self.childWriteXml(w, option);
		for xc in x_child:
			if (xc != None):
				x.appendChild(xc)
		return x

	def setattr(self, key, value):
		self.__dict__[key] = value

	def getattr(self, key):
		return self.__dict__[key]

	def LoadFromXml(self, node, handle):
		self.SetHandle(handle)

		if node.hasAttributes():
			attributes = node._get_attributes()
			attCount = attributes._get_length()
			for i in range(attCount):
				attNode = attributes.item(i)
				#Need to check if name in valid attribues
				self.setattr(UcsUtils.WordU(attNode._get_name()), str(attNode.nodeValue))

		if(node.hasChildNodes()):
			childList = node._get_childNodes()
			childCount = childList._get_length()
			for i in range(childCount):
				childNode = childList.item(i)
				if (childNode.nodeType != Node.ELEMENT_NODE):
					continue
				childFieldNames = [
				]

				cln = UcsUtils.WordU(childNode.localName)
				c = ClassFactory(cln)
				self.child.append(c)
				c.LoadFromXml(childNode, handle)

