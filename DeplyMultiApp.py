#!/u01/app/oracle/middleware/wl12c_silent/oracle_common/common/bin/wlst.sh

def wlDeployUndeploy(username, password, adminURL, appName, location, targets):
    try:
        #connect to admin server
        connect(username, password, adminURL)
        #start edit operation
        edit()
        startEdit()

        #stop application
        stopApplication(appName)

        #start undeploying application to "AdminServer" server
        progress = undeploy(appName, timeout=60000)
        progress.printStatus()
        save()
        activate(20000,block="true")
        #start deploying application to ""AdminServer" server
        progress = deploy(appName,location,targets)
        progress.printStatus()
        #print 'Done deploying application' +appname

    except Exception, e:
         print ex.toString()
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.139.114:8001','benefits','/u01/app/oracle/middleware/Applications/benefits.war','cluster1')
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.139.114:8001','messaging','/u01/app/oracle/middleware/Applications/messaging.war','cluster1')
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.139.114:8001','contacts','/u01/app/oracle/middleware/Applications/contacts.war','cluster1')
