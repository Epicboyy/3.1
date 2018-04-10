# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl = LINE("LINE帳號","LINE密碼")
oepoll = OEPoll(cl)
settingsOpen = codecs.open("temp.json","r","utf-8")
blackOpen = codecs.open("blacklist.json","r","utf-8")
adminsOpen = codecs.open("creator.json","r","utf-8")
settings = json.load(settingsOpen)
black = json.load(blackOpen)
admins = json.load(adminsOpen)
clMID = cl.profile.mid
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
msg_dict = {}
bl = ["u28d781fa3ba9783fd5144390352b0c24"]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器 重新啟動")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('blacklist.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = admins
        f = codecs.open('creator.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
for admi_d in admins["lv1"]:
    admin = [clMID,admi_d]
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x \n'
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """
╔═══════════
♥ ✿ CoCo指令表 ✿ ♥
════✪〘 查看指令表 〙✪════
↪ 「Help」查看指令
↪ 「HelpBot」查看機器設定指令
↪ 「Rebot」重新啟動機器
↪ 「Runtime」查看機器運行時間
↪ 「Speed」查看機器速度
↪ 「Set」查看設定
↪ 「About」查看自己的狀態
↪ 「Bio @」標註查看狀態消息
↪ 「Tk @」標注踢出成員
↪ 「Nk Name」使用名子踢出成員
↪ 「Zt」標註名字0字成員
↪ 「Ban @」標註加入黑單
↪ 「Unban @」標註解除黑單
↪ 「Tagall」標註全部人
↪ 「SR」設定已讀點
↪ 「R」查看已讀
"""
    return helpMessage
def helpmessagebot():
    helpMessageBot ="""
╔══〘 設定 〙✪═══════
↪ 「Add On/Off」自動加入好友 打開/關閉
↪ 「Join On/Off」邀請自動進入群組 打開/關閉
↪ 「Leave On/Off」自動離開副本 打開/關閉
↪ 「Reread On/Off」查看收回 打開/關閉
"""
    return helpMessageBot
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 13:
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
        if op.type == 24:
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
              if sender in admin:
                if msg.text is None:
                    pass
                elif text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendContact(to, "u28d781fa3ba9783fd5144390352b0c24")
                elif text.lower() == 'helpbot':
                    helpMessageBot = helpmessagebot()
                    cl.sendMessage(to, str(helpMessageBot))
                elif text.startswith("/jgurlx"):
                    str1 = find_between_r(msg.text, "gid: ", " gid")
                    str2 = find_between_r(msg.text, "url: http://line.me/R/ti/g/", " url")
                    cl.acceptGroupInvitationByTicket(str1, str2)
                    JoinedGroups.append(str1)
                    group = cl.getGroup(str1)
                    try:
                        cl.reissueGroupTicket(str1)
                        group.preventedJoinByTicket = True
                        cl.updateGroup(group)
                    except Exception as e:
                        print(e)
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                except:
                                    pass
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to, "這個群組沒有名字0字的人")
                    else:
                        for target in targets:
                            sendMessageWithMention(to, target)
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "取消人數:" + sinvitee)
                    else:
                        cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif "Ban:" in msg.text:
                    midd = msg.text.replace("Ban:","")
                    try:
                        black["blacklist"][midd] = True
                        backupData()
                        cl.sendMessage(to, "已加入黑名單")
                    except:
                        pass
                elif "Unban:" in msg.text:
                    midd = msg.text.replace("Unban:","")
                    try:
                        del black["blacklist"][midd]
                        backupData()
                        cl.sendMessage(to, "已解除黑名單")
                    except:
                        pass
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    black["blacklist"][target] = True
                                    backupData()
                                    cl.sendMessage(to, "已加入黑名單")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del black["blacklist"][target]
                                    backupData()
                                    cl.sendMessage(to, "已解除黑名單")
                                except:
                                    pass
                elif text.lower() == 'clear ban':
                    for mi_d in black["blacklist"]:
                        black["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower() == 'banlist':
                    if black["blacklist"] == {}:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        cl.sendMessage(to, "以下是黑名單")
                        mc = ""
                        for mi_d in black["blacklist"]:
                            mc += "->" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc)
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in black["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendMessage(to, "沒有黑名單")
                        else:
                            for jj in matched_list:
                                cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "黑名單以踢除")
                elif msg.text in ["SR","Setread"]:
                    cl.sendMessage(msg.to, "設置已讀點")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("設置已讀點")
                elif msg.text in ["R","r"]:
                    if msg.to in wait2['readPoint']:
                        print ("查詢已讀")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "||已讀順序||%s\n\n%s\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入SR設置已讀點")
                elif text.lower() == 'speed' or text.lower() == 'sp':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    curTime = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    rtime = time.time()
                    xtime = rtime - curTime
                    cl.sendMessage(to,'指令反應\n' + format(str(xtime)) + '秒')
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "機器運行時間 {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : Bate測試版"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔══[ 設定 ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠ 自動加入好友 ✅"
                        else: ret_ += "\n╠ 自動加入好友 ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ 自動加入群組 ✅"
                        else: ret_ += "\n╠ 自動加入群組 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ 自動離開副本 ✅"
                        else: ret_ += "\n╠ 自動離開副本 ❌"
                        if settings["reread"] == True: ret_ += "\n╠ 查詢收回開啟 ✅"
                        else: ret_ += "\n╠ 查詢收回關閉 ❌"
                        ret_ += "\n╚══[ 設定 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    backupData()
                    cl.sendMessage(to, "自動加入好友已開啟")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    backupData()
                    cl.sendMessage(to, "自動加入好友已關閉")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    backupData()
                    cl.sendMessage(to, "自動加入群組已開啟")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    backupData()
                    cl.sendMessage(to, "自動加入群組已關閉")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    backupData()
                    cl.sendMessage(to, "自動離開副本已開啟")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    backupData()
                    cl.sendMessage(to, "自動離開副本已關閉")
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    backupData()
                    cl.sendMessage(to, "查詢收回開啟")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    backupData()
                    cl.sendMessage(to, "查詢收回關閉")
                elif msg.text.lower().startswith("bio "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ 狀態消息 ]\n{}" + contact.statusMessage)
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "總共 {} 個成員".format(str(len(nama))))
        if op.type == 26:
            if msg.contentType == 0:
              try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
              except Exception as e:
                print(e)
            else:
                pass
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"%s\n[收回了]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[•]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[•]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
