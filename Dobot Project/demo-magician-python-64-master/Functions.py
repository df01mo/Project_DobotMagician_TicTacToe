# -*- coding: utf-8 -*-
"""
Created on Thu May  4 11:49:51 2023

@author: danie
"""

import threading
import DobotDllType as dType
#from config import available_ports, d, connectedPhysicalDobot
# from config import createDobotInterface
#from dobot import Dobot
# d=0
# available_ports=0
# connectedPhysicalDobot=0

initPose = [0,0,0,0,0,0,0,0]


def suctionCup(x):
	
	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "", 115200)[0]
	#print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):
		if x == 1:
			suction = True
		else:
			suction = False
		lastIndex = dType.SetEndEffectorSuctionCup(api, True,  suction, isQueued=0)
		dType.SetQueuedCmdStopExec(api)
		dType.DisconnectDobot(api)
	else:
		raise Exception


def calibration():
	
	#aux=0
	
	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "", 115200)[0]
	print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):


		#Clean Command Queued
		dType.SetQueuedCmdClear(api)
		#Async Motion Params Setting
		dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
		dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
		dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

		#Async Home- calibração
		lastIndex = dType.SetHOMECmd(api, temp = 0, isQueued = 1) #verificar isto e o while 
		dType.dSleep(100)
		
        
		#lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, x1, y1, z1, 0.0, isQueued = 1)[0]		#movimento por salto vai a x depois y depois z
		#lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, x1, y1, z1, 0.0, isQueued = 1)[0]
		#dType.dSleep(100)

		#Start to Execute Command Queued
		dType.SetQueuedCmdStartExec(api)
		#Wait for Executing Last Command
		#while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
			#dType.dSleep(100)
		#Stop to Execute Command Queued
		dType.SetQueuedCmdStopExec(api)
		dType.DisconnectDobot(api)
	else:
		raise Exception
	

def setPosition(x1,y1,z1):

	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "", 115200)[0]
	print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):


		#Clean Command Queued
		dType.SetQueuedCmdClear(api)
		#Async Motion Params Setting
		dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
		dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
		dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

		#Async Home- calibração
		#dType.SetHOMECmd(api, temp = 0, isQueued = 1)
		
        
		lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, x1, y1, z1, 0.0, isQueued = 1)[0]		#movimento por salto vai a x depois y depois z
		#lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, x1, y1, z1, 0.0, isQueued = 1)[0]
		dType.dSleep(100)

		#Start to Execute Command Queued
		dType.SetQueuedCmdStartExec(api)
		#Wait for Executing Last Command
		while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
			dType.dSleep(100)
		#Stop to Execute Command Queued
		dType.SetQueuedCmdStopExec(api)
		dType.DisconnectDobot(api)
	else:
		raise Exception

def setdanca(x1,y1,z1):

	CON_STR = {
	dType.DobotConnect.DobotConnect_NoError:  "Dobot_Connected",
	dType.DobotConnect.DobotConnect_NotFound: "Dobot_NotFound",
	dType.DobotConnect.DobotConnect_Occupied: "Dobot_Occupied"}

	#Load Dll
	api = dType.load()

	state = dType.ConnectDobot(api, "", 115200)[0]
	#print("Connect status:",CON_STR[state])

	if (state == dType.DobotConnect.DobotConnect_NoError):


		#Clean Command Queued
		dType.SetQueuedCmdClear(api)
		#Async Motion Params Setting
		dType.SetHOMEParams(api, 200, 200, 200, 200, isQueued = 1)
		dType.SetPTPJointParams(api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
		dType.SetPTPCommonParams(api, 100, 100, isQueued = 1)

		#Async Home- calibração
		#dType.SetHOMECmd(api, temp = 0, isQueued = 1)
		
        
		#lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPJUMPXYZMode, x1, y1, z1, 0.0, isQueued = 1)[0]		#movimento por salto vai a x depois y depois z
		lastIndex = dType.SetPTPCmd(api, dType.PTPMode.PTPMOVJXYZMode, x1, y1, z1, 0.0, isQueued = 1)[0]
		#dType.dSleep(100)

		#Start to Execute Command Queued
		dType.SetQueuedCmdStartExec(api)
		#Wait for Executing Last Command
		while lastIndex > dType.GetQueuedCmdCurrentIndex(api)[0]:
			dType.dSleep(100)
		#Stop to Execute Command Queued
		dType.SetQueuedCmdStopExec(api)
		dType.DisconnectDobot(api)
	else:
		raise Exception