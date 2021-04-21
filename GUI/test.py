import  wx

class AppUi():
    def __init__(self):
        self.app = wx.App(False);

        self.mainFrame = wx.Frame(None, wx.ID_ANY, "Secure Messanger",size=(350, 450))
        self.mainFrame.CreateStatusBar()
        Panel = wx.Panel(self.mainFrame)
        appGrid = wx.GridBagSizer(0,0)

        #conversation box where you can see al the messages.
        conversationText = wx.TextCtrl(Panel, size =(200,200), style=wx.TE_MULTILINE)
        #the txt input that should move to the other client.
        msgInput = wx.TextCtrl(Panel, size=(200,50), style=wx.TE_MULTILINE)
        #the send message box
        sendButton = wx.Button(Panel, size=(100,50), label="Send")

        #list of friends to chat with.
        self.sampleList = ['ariel', 'yoav', 'yarin', 'lidon']
        #the combo box that hold the friend list.
        edithear = wx.ComboBox(Panel, pos=(150, 90), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        #button for changing the current chat.
        changeButton = wx.Button(Panel, size=(100,50), label="Change Chat")

        #add everything to a gridBag and arrange.
        appGrid.Add(conversationText, pos=(0, 1), flag=wx.ALL, border=5)
        appGrid.Add(edithear, pos=(0, 0), flag=wx.ALL, border=5)
        appGrid.Add(changeButton, pos=(1, 0), flag=wx.ALL, border=5)
        appGrid.Add(msgInput, pos=(2, 1), flag=wx.ALL, border=5)
        appGrid.Add(sendButton, pos=(2, 0), flag=wx.ALL, border=5)

        #apply the gridBag arrangment to the panel.
        Panel.SetSizerAndFit(appGrid)

    def setMenuBar(self):
        # Setting up the menu.
        filemenu = wx.Menu()
        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        filemenu.Append(wx.ID_ABOUT, "&About", " Information about this program")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT, "E&xit", " Terminate the program")

        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar

        #add the menu bar to the main frame.
        self.mainFrame.SetMenuBar(menuBar)

    def StartApp(self):
        self.mainFrame.Show(True)
        self.setMenuBar()
        #self.conversationText.Show(True)
        self.app.MainLoop()



test = AppUi()
test.StartApp()