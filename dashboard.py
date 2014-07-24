from Tkinter import *
import os, time, tkMessageBox, os
import getpass, thread, threading                   #import subprocess #ttk #from multiprocessing import Process

root = Tk()
root.title("Android M-Dashboard")

frame = Frame(root)
frame.pack()

frame = Frame(root)
frame.pack()

frame1 = Frame(frame,relief=GROOVE, borderwidth=2)
frame1.pack()

frame2 = Frame(frame,relief=GROOVE, borderwidth=2)
frame2.pack()


class myClass(object):

    global device_name
    global device
    global incrementalNo
    global buildID, device_build, device_productname
    
    device_name = os.popen("adb shell getprop ro.product.name").read().strip()
    device = os.popen("adb shell getprop ro.product.device").read().strip()
    incrementalNo = os.popen("adb shell getprop ro.build.version.incremental").read().strip()
    buildID = os.popen("adb shell getprop ro.build.id").read().strip()
    device_build = os.popen("adb shell getprop ro.build.description").read().strip()
    device_productname = os.popen("adb shell getprop ro.product.model").read().strip()

    def __init__(self):
        try:
            #print "\t\t\tClick \"Connect to device\" to proceed"
            self.ROOT()
            """
            if os.name == 'nt':
                print "System is Windows...\n"
                #os.system('cls')
            else:
                print "System is Linux...\n"
                #os.system('clear')
            """
            print "\n\b\t\tConnected to: ", device_productname,'-',device_name
            print 'Build No:', device_build
            print 'Build Id:', buildID
            print "\b---------------------------------------------------------------------"
        except:
            self.Devicenotfound()
            print '\n\n', '-'*15,'Device Not Found!', '-'*15
            print 'Connect your device and then select \'Connect to Device\''

    def ROOT(self):
        #a = android.connect()
        os.system("adb wait-for-device")
        os.system("adb root"),
        time.sleep(3)
        os.system("adb wait-for-device")
        os.system("adb remount")
        time.sleep(1)
        os.system("adb wait-for-device")
        
    def snapshot(self):
        timestamp = time.strftime("%H%M%S")
        os.system("adb shell screencap -p /mnt/sdcard/screenshot_"+timestamp+'.png')
        os.system("adb pull /mnt/sdcard/screenshot_"+timestamp+".png") # >> /dev/null 2&>1")  "/home/"+getpass.getuser()+"/Desktop/"+device)
        """
        if os.name == 'posix':
            print 'done'
            #a.device.screenshot('/home/'+ getpass.getuser() + '/Desktop/screenshot'+timestamp+'.png')
        elif os.name == 'nt':
            print 'done'
            #a.device.screenshot("D:\\Profiles\\"+getpass.getuser()+"\\Desktop\\screenshot"+timestamp+".png")
        """
        print '\bSnapshot dumped !'

    def EXIT(self):
        root.quit()

    def wifi(self):
        #a=android.connect()
        a.device.adb('install PythonAutoHelper.apk')
        time.sleep(2)
        a.device.adb('shell am instrument -e class com.android.mohit.test.DecreaseVolume com.android.mohit.test/android.test.InstrumentationTestRunner')
      
    def ERASE(self):
        print 'Phone will reboot now. Please wait..'
        os.system("adb wait-for-device")
        os.system("adb reboot-bootloader")
        os.system("adb fastboot erase userdata")
        time.sleep(1)
        os.system("fastboot erase misc")
        time.sleep(1)
        val = raw_input('Do you want to reboot? y/n ')
        if val == 'y':
            os.system("fastboot reboot")
        elif val == 'n':
            pass

    def REBOOT(self):
        os.system("adb reboot")

    def LOG(self):
        print 'Please wait..'
        timestamp = time.strftime("%H%M%S")
        #buildID = os.popen("adb shell getprop ro.build.id").read().strip()
        #incrementalNo = os.popen("adb shell getprop ro.build.version.incremental").read().strip()
        if os.name == 'posix':
            Loc = ("/home/"+getpass.getuser()+"/Desktop/"+device)
            if not os.path.isdir(Loc):
                os.mkdir(Loc)
            #os.system("adb logcat -d >" + Loc + "/"+buildID+"_"+incrementalNo+"_Logcat_"+timestamp+".txt")
            os.system("adb logcat -d >" + "./"+buildID+"_"+incrementalNo+"_logcat_"+timestamp+".txt")
        elif os.name == 'nt':
            Loc = ("D:\\Profiles\\"+getpass.getuser()+"\\Desktop\\" + device)   #+ "_" + buildID)
            if not os.path.isdir(Loc):
                os.mkdir(Loc)
            #os.system("adb logcat -d >" + Loc + "\\"+buildID+"_"+incrementalNo+"_Logcat_"+timestamp+".txt")
            os.system("adb logcat -d >" + "\\"+buildID+"_"+incrementalNo+"_Logcat_"+timestamp+".txt")
        print '\bLogcat dumped!'
        
    def BUGREPORT(self):
        print 'Please wait..'
        timestamp = time.strftime("%H%M%S")
        #buildID = os.popen("adb shell getprop ro.build.id").read().strip()
        device = os.popen("adb shell getprop ro.product.device").read().strip()
        if os.name == 'posix':
            Loc = ("/home/"+getpass.getuser()+"/Desktop/" + device)  # + "_" + buildID)
            if not os.path.isdir(Loc):
                os.mkdir(Loc)
            os.system("adb shell bugreport >" + "./"+buildID+"_"+incrementalNo+"_bugreport_"+timestamp+".txt")
            #os.system("adb pull /data/logger " + Loc + "/flash-logger")
            #os.system("adb pull /sdcard-ext/logger " + Loc + "/sdcard-ext-logger")
            #os.system("adb pull /sdcard/logger " + Loc + "/sdcard-logger")
        elif os.name == 'nt':
            Loc = ("D:\\Profiles\\"+getpass.getuser()+"\\Desktop\\" + device)  # + "_" + buildID)
            if not os.path.isdir(Loc):
                os.mkdir(Loc)
            os.system("adb shell bugreport >" + "\\"+buildID+"_"+incrementalNo+"_bugreport_"+timestamp+".txt")
            #os.system("adb pull /data/logger " + Loc + "\\flash-logger")
            #os.system("adb pull /sdcard-ext/logger " + Loc + "\\sdcard-ext-logger")
            #os.system("adb pull /sdcard/logger " + Loc + "\\sdcard-logger")
        print '\bBugreport dumped!'

    def WDOCK(self):
        print 'Please wait..',
        process = "D:\Dashboard\WhisperDockFiles\\NewWhisper.bat"
        subprocess.call(process)
        print '\bDone! Files pushed.'

    #Declaring global varilable "div" to be used in WhichDeivce method
    var = IntVar()
    div = IntVar()  
    div = 0

    def WhichDevice(self):
        global div
        if (var.get() == 1):
            div = 1
        elif (var.get() == 2):
            div = 2

    def ClearCheckinDB(self):
        a=android.connect()
        print 'Clearing DB...',
        a.device.sh('sqlite3 /data/system/checkin_mot.db "delete from events;"')
            
    def Wizard(self):
        print 'Please wait..',
        a=android.connect()
        if a.ui.screen().widget(id='welcomeTitle'):
            os.system('adb shell pm disable com.motorola.setupwizard.controller')
            os.system('adb shell pm disable com.android.setupwizard/com.android.setupwizard.SetupWizardActivity')
        print '\bScreen skipped!'
        
    def Devicenotfound(self):
        tkMessageBox.showinfo("Device not found","Connect device \n& Select Connect to device")

    def ConnectToDevice(self):
        try:
            print 'Connecting.... '
            self.ROOT()
            os.system('clear')
            device_name = os.popen("adb shell getprop ro.product.device").read().strip()
            device_productname = os.popen("adb shell getprop ro.product.model").read().strip()
            print "\n\b\t\tConnected to: ", device_productname,'-',device_name, '\n'
            print 'Build No:', device_build
            print 'Build Id:', buildID
            print "\b---------------------------------------------------------------------"
        except:
            #tkMessageBox.showinfo("Device not found","Connect device \n& Select Connect to device")
            self.Devicenotfound()

    def check_handle_device_not_found(self, text, number):
        s=a.ui.screen()
        temp=-1
        for name in s.widgets():
            if name.text()==text:
                temp=0;
            if temp==number:
                print name.is_checked()
                return(name.is_checked())

    def clear_log(self):
        os.system("adb shell logcat -c")
        print "Logs clear !"

#----------------------------------------------Menubar code starts here------------------------------------------------

    def MenuHelp(self):
        tkMessageBox.showinfo("Help", "M-Dashboard "+"\n" + "By Mohit"+"\n" + "<mohits@nvidia.com>")
    def DeviceAwake(self):
        a=android.connect()
        a.ui.unlock()
        if a.ui.window() != 'com.motorola.blur.home/com.motorola.blur.home.HomeActivity':
            a.input.back(5)
        else:
            pass
        a.input.menu()
        a.ui.waitfor(text='Settings', timeout=30).tap()
        a.ui.scrollto(text='Applications').tap()
        a.ui.scrollto(text='Development').tap()
        a.ui.waitfor(text='Stay awake', timeout=30).tap()
        a.input.home()
        time.sleep(1)
    def EraseLog(self):
        os.system('adb logcat -c')
        print " \bDone!"
    def CLS(self):
        os.system('clear')
    def FastbootMode(self):
        os.system('adb reboot bootloader')
        print " \bDone!"
    def RestartServer(self):
        os.system('adb kill-server')
        time.sleep (1)
        os.system('adb devices')
        time.sleep(2)
    def MACAddress(self):
        val = raw_input("Please enter value of MACAddress like 56:da:36:16:de:eb \n: ")
        os.system("adb shell calibrator set nvs_mac  /system/etc/firmware/ti-connectivity/wl1271-nvs.bin " + val)
        print " \bDone!"
    def CheckinLogDump(self):
        timestamp = time.strftime("%H%M%S")
        if os.name == 'posix':
            os.system("adb shell sqlite3 /data/system/checkin_mot.db  \"select datetime(date/1000,'unixepoch','localtime'),tag,value from events\" >"+"/home/"+getpass.getuser()+"/Desktop/CheckinLog_"+timestamp+".txt")
        elif os.name == 'nt':
            os.system("adb shell sqlite3 /data/system/checkin_mot.db .dump >"+"D:\\Profiles\\"+getpass.getuser()+"\\Desktop\\CheckinLog_"+timestamp+".txt")
    def MYWIFI(self):
        a=android.connect()
        os.system('adb shell am start -a android.intenet.action.MAIN -n com.android.settings/com.android.settings.wifi.WifiSettings')
        time.sleep(3)
        if a.ui.screen().widget(text='MMI-Internet'):
            a.ui.waitfor(text='MMI-Internet').tap()
            time.sleep(1)
            a.input.text('2012InternetAccess')
            a.ui.waitfor(text='Connect', timeout=30).tap()
            time.sleep(2)
            a.input.home()
        elif a.ui.waitfor(id='checkbox').is_checked() == False:
            a.ui.waitfor(text='Wi-Fi').tap()
            time.sleep(5)
            a.ui.scrollto(text='MMI-Internet').tap()
            time.sleep(1)
            a.input.text('InternetAccess2011')
            a.ui.waitfor(text='Connect', timeout=30).tap()
            time.sleep(2)
            a.input.home()
        elif a.ui.waitfor(id='checkbox').is_checked() == True:
            a.ui.scrollto(text='MMI-Internet').tap()
            time.sleep(1)
            a.input.text('InternetAccess2011')
            a.ui.waitfor(text='Connect', timeout=30).tap()
            time.sleep(2)
            a.input.home()
        #elif anyof=[a.ui.widgetspec(text='An'),a.ui.widgetspec(id='incomingCallWidget')] )
    def EventLog(self):
        timestamp = time.strftime("%H%M%S")
        os.system("adb shell sqlite3 /data/system/checkin_mot.db .dump >D:\\Profiles\\"+getpass.getuser()+"\\Desktop\\EventLog"+timestamp+".txt")
    def ToHome(self):
        os.system('adb shell am broadcast -a com.android.launcher/com.android.launcher2.Launcher')
        print " \bDone!"
    def CarDock(self):
        a=android.connect()
        a.device.sh('am broadcast -a android.intent.action.DOCK_EVENT --ei android.intent.extra.DOCK_STATE 2')
        time.sleep(1)
    def CarUndock(self):
        a=android.connect()
        a.device.sh('am broadcast -a android.intent.action.DOCK_EVENT --ei android.intent.extra.DOCK_STATE 0')
        time.sleep(1)
    def DeskDock(self):
        a=android.connect()
        a.device.sh('setprop hw.whisper 14E66C22828B,0AC000')
        a.device.sh('am broadcast -a android.intent.action.DOCK_EVENT --ei android.intent.extra.DOCK_STATE 1')
    def DeskUndock(self):
        a=android.connect()
        a.device.sh('setprop hw.whisper 14E66C22828B,0AC000')
        a.device.sh('am broadcast -a android.intent.action.DOCK_EVENT --ei android.intent.extra.DOCK_STATE 0')
    def myThread(self):
        print 

    
cInstance = myClass()

#--------------------------------------------------- Button code starts here---------------------------------------------

Button(frame1, text='Snapshot', width=15, command=cInstance.snapshot, fg="green").grid(row=0,column=0)
Button(frame1, text='Logcat', width=15, command=cInstance.LOG, fg="green").grid(row=1,column=0)
Button(frame1, text='Bugreport', width=15, command=cInstance.BUGREPORT, fg="green").grid(row=2,column=0)
Button(frame1, text='Clear Logcat', width=15, command=cInstance.clear_log, fg="red").grid(row=0,column=1)
Button(frame1, text='Reset Device', width=15, command=cInstance.ERASE, fg="red").grid(row=1,column=1)
Button(frame1, text='Connect to device', width=15, command=cInstance.ConnectToDevice, fg="blue").grid(row=1,column=2)
Button(frame1, text='SkipWizard', width=15, command=cInstance.Wizard).grid(row=0,column=2)
#Button(frame1, text='CarDock', width=15, command=cInstance.CarDock).grid(row=2,column=1)
#Button(frame1, text='DeskDock', width=15, command=cInstance.DeskDock).grid(row=2,column=2)
Button(frame1, text='Reboot Device', width=15, command=cInstance.REBOOT, fg="green").grid(row=3,column=0)
#Button(frame1, text='EventLog', width=15, command=cInstance.EventLog).grid(row=3,column=1)
#Button(frame1, text='UnDock', width=15, command=cInstance.CarUndock).grid(row=3,column=2)
#Button(frame1, text='MACAddress', width=15, command=cInstance.MACAddress).grid(row=4,column=0)
#Button(frame1, text='Clear CheckinDB', width=15, command=cInstance.ClearCheckinDB).grid(row=4,column=1)
#Button(frame1, text='CheckinLogDump', width=15, command=cInstance.CheckinLogDump).grid(row=4,column=2)
#Button(frame1, text='WiFi', width=15, command=cInstance.MYWIFI).grid(row=5,column=2)
Button(frame2, text='Exit', width=15, command=cInstance.EXIT).grid(row=6,column=1)
#var.set(None)

#-------------------------------------------Menubar widgets-------------------------------------------------
menubar=Menu(root)

filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Stay Awake", command=cInstance.DeviceAwake)
filemenu.add_command(label="ToHome", command=cInstance.ToHome)
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

settingmenu=Menu(menubar, tearoff=0)
settingmenu.add_command(label="FastbootMode", command=cInstance.FastbootMode)
settingmenu.add_command(label="Erase logcat", command=cInstance.EraseLog)
settingmenu.add_command(label="Root", command=cInstance.ROOT)
settingmenu.add_command(label="Restart-Server", command=cInstance.RestartServer)
settingmenu.add_command(label="Clear Screen", command=cInstance.CLS)
menubar.add_cascade(label="Settings", menu=settingmenu)

checkinmenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label="CheckIn", menu=checkinmenu)

dockmenu=Menu(menubar, tearoff=0)
dockmenu.add_command(label="CarDock", command=cInstance.CarDock)
dockmenu.add_command(label="CarUndock", command=cInstance.CarUndock)
dockmenu.add_command(label="DeskDock", command=cInstance.DeskDock)
dockmenu.add_command(label="DeskUndock", command=cInstance.DeskUndock)
menubar.add_cascade(label="Dock", menu=dockmenu)

helpmenu=Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=cInstance.MenuHelp)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
#-------------------------------------------- Menu Bar Code Ends Here ------------------------------------------


root.mainloop()
