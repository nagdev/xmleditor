import wx; import os; import wx.dataview as dv
from XmlLoader import XmlLoader as LoaderClass
import PanelViews
from KeyEvents import KeyEvents as kyEvnts

class XmlBaseClass(wx.Frame):
    """ xml Editor. """
    
    __treePanel = None
    __editPanel = None
    __keyEvents = None
    __notBook = None
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, wx.ID_ANY, title, pos=(0, 0), size=wx.DisplaySize())
        self.CreateStatusBar()
        
        
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open xml file")
        filemenu.AppendSeparator()
        menuSave = filemenu.Append(wx.ID_SAVE, "&Save", "Save xml file")
        filemenu.AppendSeparator()
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        filemenu.AppendSeparator()        
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Exit the program")
        
        ##edit menu
        
        
        self.Bind(wx.EVT_MENU, self.onOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.onExit, menuExit)
        self.Bind(wx.EVT_MENU, self.onSave, menuSave)
        
        
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")
        
        self.SetMenuBar(menubar)
        
        splitter = wx.SplitterWindow(self, style = wx.SP_BORDER)
        leftPanel = wx.Panel(splitter)
        rightPanel = wx.Panel(splitter)
        
        
        self.__treePanel = localTree = PanelViews.TreePanelView(leftPanel)
        leftSizer = wx.BoxSizer(wx.VERTICAL)
        leftSizer.Add(localTree, 1, wx.EXPAND | wx.ALL)
        leftPanel.SetSizer(leftSizer)
        leftPanel.SetAutoLayout(True)
        
        self.__editPanel = wx.Panel(rightPanel)
        rightSizer = wx.BoxSizer(wx.VERTICAL)
        rightSizer.Add(self.__editPanel, 1, wx.EXPAND | wx.ALL)
        rightPanel.SetSizer(rightSizer)
        rightPanel.SetAutoLayout(True)
        
        
        splitter.SplitVertically(leftPanel, rightPanel)
        splitter.SetMinimumPaneSize(200)
        splitter.SetSashGravity(0.5)
        
        
        
        
        self.Maximize()
        
        
    def onAbout(self, e):
        dlg = wx.MessageDialog(self, "XML Editor", "About XML Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
        
    def DisplayInfo(self, infoText):
        dlg = wx.MessageDialog(self, infoText, "Info", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()  
    
    def onSave(self, e):
        self.__editPanel.SaveXML(e = None)
        
        
    def onExit(self, e):
        self.Close()
        
        
    def onOpen(self, e):
        """ Open Text file """
       
        self.dirname = ""
        baseclass = self
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.xml", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            cls1 = LoaderClass(os.path.join(self.dirname, self.filename))
            cls1.LoadXMLFile(baseclass)
            
        dlg.Destroy()
        
    
    def CreateNewTab(self, xmltree):
        
        self.__treePanel.updateTree(xmltree.getroot())
        
        
        self.__notBook = wx.Notebook(self.__editPanel)
        newTab = PanelViews.EditPanelView(self.__notBook)
        self.__notBook.AddPage(newTab, "XML Document")
        
        sizer = wx.BoxSizer()
        sizer.Add(self.__notBook, 1, wx.EXPAND)
        self.__editPanel.SetSizer(sizer)

  
        
app = wx.App(False)
frame = XmlBaseClass(None, "XML Editor")
frame.Show(True)
app.MainLoop()