import wx; import os; import wx.dataview as dv
from XmlLoader import XmlLoader as LoaderClass
import PanelViews

class XmlBaseClass(wx.Frame):
    """ xml Editor. """
    
    __treePanel = PanelViews.TreePanelView
    __editPanel = PanelViews.EditPanelView
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(800, 600))
        self.CreateStatusBar()
        
        filemenu = wx.Menu()
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open", "Open xml file")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        filemenu.AppendSeparator()        
        menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", "Exit the program")
        
        self.Bind(wx.EVT_MENU, self.onOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.onAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.onExit, menuExit)
        
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")
        
        self.SetMenuBar(menubar)
        
        #split window
        splitter = wx.SplitterWindow(self)
        
        self.__treePanel = leftP = PanelViews.TreePanelView(splitter)
        self.__editPanel = rightP = PanelViews.EditPanelView(splitter)
        
        #split
        splitter.SplitVertically(leftP, rightP)
        splitter.SetMinimumPaneSize(200)
        
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
        
    
        
    def onAbout(self, e):
        dlg = wx.MessageDialog(self, "XML Editor", "About XML Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def DisplayInfo(self, infoText):
        dlg = wx.MessageDialog(self, infoText, "Info", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()  
       
        
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
            cls1.LoadXMLFile(baseclass, self.__treePanel, self.__editPanel)
        dlg.Destroy()
    
        
        
app = wx.App(False)
frame = XmlBaseClass(None, "XML Editor")
frame.Show(True)
app.MainLoop()