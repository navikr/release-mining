import globalParser
import nolioRequestParser
import globalValidation
class RAMining:
    globalParse=globalParser.CommonParser()
    nolioreq=nolioRequestParser.NolioRequest()
    globalVal=globalValidation.LogValidator()
    fpath="C://Cases//Barclays//00701311//PerformanceIssue_PostHotfix_8640//PerformanceIssue_PostHotfix_8640//logs//nolio_requests.log"
    dPath="C://Cases//Barclays//00701311//PerformanceIssue_PostHotfix_8640//PerformanceIssue_PostHotfix_8640"
    lines=globalParse.fileReader(fpath)
    #temp=globalParse.columnParser("nolio_requests.log",lines)
    #globalParse.writeCSV(temp,"testing.csv",dPath,seperator=',', headers=['Log Name','Date','Time','Thread','Log Level','Protocol','Method','API','User','RemoteHost','RemoteAddress','START_DATE','START_TIME','Duration'])
    #6.2 and Higher##['Log Name','Date','Time','Thread','Log Level','Protocol','Method','CODE','API','User','RemoteHost','RemoteAddress','X-Forwarded-For','START_DATE','START_TIME','Duration']
    #5.5.2 and Higher##['Log Name','Date','Time','Thread','Log Level','Protocol','Method','CODE','API','User','RemoteHost','RemoteAddress','START_DATE','START_TIME','Duration']
    #temp=globalParse.readCSVAsDict(dPath+"//testing.csv")
    #nolioreq.engagementInsight(temp,dPath,"engagementInsight.csv",headers=['Log Name','Date','Time','Thread','Log Level','Protocol','Method','API','User','RemoteHost','RemoteAddress','X-Forwarded-For','START_DATE','START_TIME','Duration'])
    #nolioreq.featureInsight(temp,dPath,"featureInsight.csv",headers=['Date','API'])
    #temp=globalParse.apiParser(dPath,"testing.csv",'a/reports/releasesReportsPage');
    #globalParse.writeCSV(temp,"apiInsight.csv",dPath,seperator=',', headers=['Date-Time','User','API','TimeTaken(seconds)'])
    

    #globalVal.timeOrderValidator("C://Cases//ING//00686751//logsplainapp//logsplainapp",["C://Cases//ING//00686751//logsplainapp//logsplainapp"])
    #globalVal.timeOrderValidator("C://Saurabh//Movies//EURO Issue",["C://Saurabh//Movies//EURO Issue//logs_primaryNAC//logs","C://Saurabh//Movies//EURO Issue//logs_secondaryNAC//logs"])
    globalParse.releaseParser("C://Cases//BNPP//00721401//NAC_Backup_logs-Optima//customPick",52294574)
    #globalParse.processIdParser('releaseDetails.txt',"C://Cases//Swisscom//00580829//NolioAutomationCenterLogs",'12863')

