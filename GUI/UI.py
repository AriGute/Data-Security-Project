import wx

class AppUi():
    def __init__(self):
        self.app = wx.App(False);

        #fixed position for all the elements on the frame.
        fixPosX = 10;
        fixPosY = 10;

        #get the center of the screen(screen resolution/2 - app frane size)
        w = (wx.GetDisplaySize()[0]/2)-(350/2)
        h = (wx.GetDisplaySize()[1]/2)-(380/2)
        screenCenter = (w,h)

        #main frain of the app and syle->cannot be resize
        self.mainFrame = wx.Frame(None, wx.ID_ANY, "Secure Messanger",size=(350, 380), pos=screenCenter, style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.mainFrame.CreateStatusBar()
        Panel = wx.Panel(self.mainFrame)

        #conversation box where you can see al the messages.
        self.conversationBox = wx.TextCtrl(Panel, size =(200, 200), pos=(100 + fixPosX, 0 + fixPosY),  style=wx.TE_MULTILINE|wx.TE_READONLY)
        #the txt input that should move to the other client.
        self.msgInput = wx.TextCtrl(Panel, size=(200,50),pos=(100+fixPosX,210+fixPosY),  style=wx.TE_MULTILINE)
        #the send message box
        sendButton = wx.Button(Panel, size=(100,50), pos=(0+fixPosX,210+fixPosY), label="Send")
        #bind methond to the button.
        #sendButton.Bind(wx.EVT_BUTTON,self.SendMessage())
        sendButton.Bind(wx.EVT_BUTTON, self.SendMessage)

        #for the moment we use this to connect(specific ip and port numbers).
        self.ipInput = wx.TextCtrl(Panel, size=(90, 20), pos=(0 + fixPosX,  30 + fixPosY))
        self.ipInput.SetValue("ip")
        self.portInput = wx.TextCtrl(Panel, size=(90, 20), pos=(0 + fixPosX, 50 + fixPosY))
        self.portInput.SetValue("port")
        connectButton = wx.Button(Panel, size=(100,20), pos=(0+fixPosX,70+fixPosY), label="Send")

        #list of friends to chat with.
        self.friendList = []
        self.namesList = []
        #the combo box that hold the friend list.
        edithear = wx.ComboBox(Panel, pos=(0+fixPosX, 0+fixPosY), size=(95, -1),  choices=self.namesList, style=wx.CB_DROPDOWN)
        #button for changing the current chat.
        changeButton = wx.Button(Panel, size=(100,50), pos=(0+fixPosX,150+fixPosY), label="Change Chat")



    def setMenuBar(self):
        # Setting up the menu.
        filemenu = wx.Menu()
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()
        # Adding the "filemenu" to the MenuBar
        menuBar.Append(filemenu, "&File")

        #add the menu bar to the main frame.
        self.mainFrame.SetMenuBar(menuBar)

    def StartApp(self):
        self.mainFrame.Show(True)
        self.setMenuBar()
        self.app.MainLoop()

    def AddFriend(self,name,ip,port):
        #the friendList and the nameList have connection through identical index position in the lists.
        connectDetails = (ip,port)
        self.friendList.append(connectDetails)
        self.namesList.append(name)

    def GetIpAndPort(self):
        #get the ip and the port from the input field as a touple.
        return (self.ipInput.GetValue(), self.portInput.GetValue())

    def SendMessage(self, msg):
        #pass a message to the conversation box.
        tempString = self.conversationBox.GetValue()
        tempString+=msg+"\n"
        self.conversationBox.SetValue(tempString)

    def GetMessage(self, event):
        #for testing at the moment... send form the input msg box to the conversation box.
        btn = event.GetEventObject().GetLabel()
        self.GetMessage(self.msgInput.GetValue())
        self.msgInput.SetValue("")


# exemple:
test = AppUi()
test.StartApp()
