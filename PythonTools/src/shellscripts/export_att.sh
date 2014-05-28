########################################################################################
# Script export AT&T
########################################################################################

echo "Start ReplicationExport...."
#ReplicationExport -u Administrator -p Openet01  -o PCRF_1.xml CTE PCRF_1
#ReplicationExport -u Administrator -p Openet01  -o CTE_PGW.xml CTE CTE_DEV_2_PGW
#ReplicationExport -u Administrator -p Openet01  -o PMATF.xml CTE PMATF
#ReplicationExport -u Administrator -p Openet01  -o CTEPeers.xml CTEPeers
#ReplicationExport -u Administrator -p Openet01  -o TopLevelPeers.xml TopLevelPeers
#ReplicationExport -u Administrator -p Openet01  -o SessionStoreSolutionModules.xml SessionStoreSolutionModules
#ReplicationExport -u Administrator -p Openet01  -o RefData.xml RefData
#ReplicationExport -u Administrator -p Openet01  -o AccountInterfaceSolutionModules.xml AccountInterfaceSolutionModules
#ReplicationExport -u Administrator -p Openet01  -o AlarmManagement.xml AlarmManagement
ReplicationExport -u Administrator -p Openet01  -o Parameters.xml Parameters
ReplicationExport -u Administrator -p Openet01  -o RMS.xml RMS
#ReplicationExport -u Administrator -p Openet01  -o DeploymentMatrix.xml DeploymentMatrix
#ReplicationExport -u Administrator -p Openet01  -o Policy_ReferenceData.xml Policy ReferenceData
#ReplicationExport -u Administrator -p Openet01  -o Policy_DATA.xml Policy ReferenceData
#ReplicationExport -u Administrator -p Openet01  -o Policy_OBJECTS.xml Policy PolicyObjects
#ReplicationExport -u Administrator -p Openet01  -o Policy_CONFIG.xml Policy Configuration CFG_71
#ReplicationExport -u Administrator -p Openet01  -o Policy_TAG.xml Policy Tag 20111116_1516_DTNotifications
#ReplicationExport -u Administrator -p Openet01  -o Policy.xml Policy All
ReplicationExport -u Administrator -p Openet01  -o Applications.xml Applications
ReplicationExport -u Administrator -p Openet01  -o Custom.xml Custom
#ReplicationExport -u Administrator -p Openet01  -o InMemoryRefDataSolutionModules.xml InMemoryRefDataSolutionModules
ReplicationExport -u Administrator -p Openet01  -o Logging.xml Logging
ReplicationExport -u Administrator -p Openet01  -o OpenetDB.xml OpenetDB
#ReplicationExport -u Administrator -p Openet01  -o RecordWriterSolutionModules.xml RecordWriterSolutionModules
#ReplicationExport -u Administrator -p Openet01  -o SchedulerSolutionModules.xml SchedulerSolutionModules
#ReplicationExport -u Administrator -p Openet01  -o Security.xml Security
#ReplicationExport -u Administrator -p Openet01  -o Statistics.xml Statistics
ReplicationExport -u Administrator -p Openet01  -o UDE.xml UDE
cp /export/home/telus3/FW7/home/alarms/AlarmDefs_TelusCustomPoints.xml .

echo "End ReplicationExport...."

