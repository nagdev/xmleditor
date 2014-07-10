import wx; import os; import wx.dataview as dv
from XmlLoader import XmlLoader as LoaderClass
import PanelViews
from KeyEvents import KeyEvents as kyEvnts

class XmlBaseClass(wx.Frame):
    """ xml Editor. """
    
    __treePanel = PanelViews.TreePanelView
    __editPanel = PanelViews.EditPanelView
    __keyEvents = kyEvnts
    
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
        
        #split window
        splitter = wx.SplitterWindow(self)
        
        
        
        self.__treePanel = leftP = PanelViews.TreePanelView(splitter)
        self.__editPanel = rightP = PanelViews.EditPanelView(splitter)
        
        self.__editPanel.SetFocus()
        
        #split
        splitter.SplitVertically(leftP, rightP)
        splitter.SetMinimumPaneSize(200)
        splitter.SetSashGravity(0.5)
        
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        
        self.Maximize()
        
        self.__keyEvents =  kyEventclass = kyEvnts(self.__treePanel, self.__editPanel, self)
         
        
        
        
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
            cls1.LoadXMLFile(baseclass, self.__treePanel, self.__editPanel, self.filename, self.__keyEvents)
        dlg.Destroy()
        
        
        
app = wx.App(False)
frame = XmlBaseClass(None, "XML Editor")
frame.Show(True)
app.MainLoop()