#!/bin/sh

if [ "$1" = "" ]
then
  echo "Error INSTALLATION_ID is empty"
  exit
fi

#Put here the installation id
INSTALLATION_ID=$1

cd /export/home/telus1/install/FW_7.0.1B1277
java -jar installer.jar -install '~'$INSTALLATION_ID'/install.properties'
java -jar patch_FW_7.0.1.1_x86_64.jar -patch '~'$INSTALLATION_ID'/install.properties'
java -jar patch_FW_7_0_1_2B1_x86_64.jar -patch '~'$INSTALLATION_ID'/install.properties'
java -jar patch_FW_7.0.1.3B1_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
java -jar patch_FW_7.0.1.4B3_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
java -jar patch_FW_7_0_1_5B1_VFNL_MOSA_CS_SOAPClient_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
java -jar patch_FW_7_0_1_5B1_VFNL_MOSA_CS_SOAPServer_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
java -jar patch_FW_7_0_1_5B1_VFNL_MOSA_SS_SOAPClient_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
java -jar patch_FW_7_0_1_5B1_VFNL_MOSA_SS_SOAPServer_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
java -jar patch_FW_7_0_1_5B1_VFPS_SOAPClient_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
java -jar patch_FW_7_0_1_5B1_VFPS_SOAPServer_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
java -jar patch_FW_7.0.1.6B1_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
java -jar patch_FW_7_0_1_7B1_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
 
#cd /export/home/telus1/install/PM_4.0B455
#java -jar installer.jar -install ~$INSTALLATION_ID/install.properties
#java -jar patch_PM_4.0.0.1B1_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
 
#cd /export/home/telus1/install/PM_PRDE_4.0B568
#java -jar installer.jar -install ~$INSTALLATION_ID/install.properties
#java -jar patch_PM_PRDE_4.0.0.1B1_x86_64.jar -patch ~$INSTALLATION_ID/install.properties
#java -jar patch_PM_PRDE_4.0.0.2B1_x86_64.jar -patch ~$INSTALLATION_ID/install.properties

cd /export/home/telus1/install/PM_4.0B455
java -jar patch_PM_4.0.0.3B1_x86_64.jar -patch ~$INSTALLATION_ID/install.properties

cd /export/home/telus1/install/PM_PRDE_4.0B568
java -jar patch_PM_PRDE_4.0.0.5B2_x86_64.jar -patch ~$INSTALLATION_ID/install.properties

$FUSIONWORKS_PROD/share/scripts/database/BMCreateInMemoryRefData.sh $INSTALLATION_ID'bl' $INSTALLATION_ID'bl' RA21122E

for ((  i = 1 ;  i <= 2;  i++  )) do
        $FUSIONWORKS_PROD/share/scripts/database/AccountInterface/BMCreateAccountInterface.sh $INSTALLATION_ID'AI_'$i $INSTALLATION_ID'AI'_$i RA21122E
        $FUSIONWORKS_PROD/share/scripts/database/SessionStore/CreateSessionStore.sh $INSTALLATION_ID'PM_'$i $INSTALLATION_ID'PM_'$i RA21122E SessionStore USERS USERS
done

sqlplus $INSTALLATION_ID'bl'/$INSTALLATION_ID'bl'@RA21122E @reference_table.sql


./FW7/prod/bin/InstallExternalLibraries.sh

vncserver :62
