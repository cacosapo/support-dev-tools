#!/bin/sh

fileConf=$1
IFS=';'
cat $fileConf | while read INSTALLATION_ID PREFIX PM_PRODUCTSCHEMAUSERNAME PM_PRODUCTSCHEMAPASSWORD PM_SHAREDSCHEMAUSERNAME PM_SHAREDSCHEMAPASSWORD SP_ORASTATUSER SP_ORASTATPASSWORD

do

    if [[ $INSTALLATION_ID == "#" ]]
    then
        continue
    fi


echo "#################################################################"
echo "Start - Replace Tokens"
echo "#################################################################"


for fn in *.xml; do

        sed -i '/brandedTypeChecksum/d' $fn
        sed -i 's/@@@INSTALLATION_ID@@@/'$INSTALLATION_ID'/g' $fn
        sed -i 's/@@@PREFIX@@@/'$PREFIX'/g' $fn
        sed -i 's/@@@PM_PRODUCTSCHEMAUSERNAME@@@/'$PM_PRODUCTSCHEMAUSERNAME'/g' $fn
        sed -i 's/@@@PM_PRODUCTSCHEMAPASSWORD@@@/'$PM_PRODUCTSCHEMAPASSWORD'/g' $fn
        sed -i 's/@@@PM_SHAREDSCHEMAUSERNAME@@@/'$PM_SHAREDSCHEMAUSERNAME'/g' $fn
        sed -i 's/@@@PM_SHAREDSCHEMAPASSWORD@@@/'$PM_SHAREDSCHEMAPASSWORD'/g' $fn
        sed -i 's/@@@SP_ORASTATUSER@@@/'$SP_ORASTATUSER'/g' $fn
        sed -i 's/@@@SP_ORASTATPASSWORD@@@/'$SP_ORASTATPASSWORD'/g' $fn
        
    done

echo "#################################################################"
echo "End - Replace Tokens"
echo "#################################################################"

USER=Administrator
PASSWD=Openet01

echo "#################################################################"
echo "Start - Replication Import"
echo "#################################################################"


ReplicationImport -u $USER -p $PASSWD  Parameters.xml
ReplicationImport -u $USER -p $PASSWD  UDE.xml
ReplicationImport -u $USER -p $PASSWD  CTEPeers.xml
ReplicationImport -u $USER -p $PASSWD  TopLevelPeers.xml
ReplicationImport -u $USER -p $PASSWD  InMemoryRefDataSolutionModules.xml
ReplicationImport -u $USER -p $PASSWD  AccountInterfaceSolutionModules.xml
ReplicationImport -u $USER -p $PASSWD  SessionStoreSolutionModules.xml
ReplicationImport -u $USER -p $PASSWD  RecordWriterSolutionModules.xml
ReplicationImport -u $USER -p $PASSWD  RMS.xml
ReplicationImport -u $USER -p $PASSWD  RefData.xml
mkdir /export/home/$INSTALLATION_ID/FW7/home/alarms
cp AlarmDefs_TelusCustomPoints.xml /export/home/$INSTALLATION_ID/FW7/home/alarms
ReplicationImport -u $USER -p $PASSWD  AlarmManagement.xml
ReplicationImport -u $USER -p $PASSWD  CTE_PGW.xml
ReplicationImport -u $USER -p $PASSWD  CTE_GGSN.xml
ReplicationImport -u $USER -p $PASSWD  CTE_PERFMON.xml
ReplicationImport -u $USER -p $PASSWD  Statistics.xml
ReplicationImport -u $USER -p $PASSWD  Logging.xml

ReplicationImport -u $USER -p $PASSWD  DeploymentMatrix.xml
ReplicationImport -u $USER -p $PASSWD  Applications.xml

ReplicationImport -u $USER -p $PASSWD  OpenetDB.xml

ReplicationImport -u $USER -p $PASSWD  Policy.xml

ReplicationImport -u $USER -p $PASSWD  Policy_OBJECTS.xml
ReplicationImport -u $USER -p $PASSWD  Policy_DATA.xml
ReplicationImport -u $USER -p $PASSWD  Policy_TAG.xml
ReplicationImport -u $USER -p $PASSWD  Policy_ReferenceData.xml
ReplicationImport -u $USER -p $PASSWD  Policy_CONFIG.xml

echo "#################################################################"
echo "End - Replication Import"
echo "#################################################################"

done
