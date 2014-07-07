import wx; import os; import wx.dataview as dv
from XmlLoader import XmlLoader as LoaderClass

class XmlBaseClass(wx.Frame):
    """ xml Editor. """
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(700, 500))
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
        
        self.Show(True)
        
        #self.showXML()  
    
    def UpdateTree(self, dict):
        
        self.dvtc = dvtc = dv.DataViewTreeCtrl(self, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)

        isz = (16,16)
        il = wx.ImageList(*isz)
        fldridx     = il.AddIcon(wx.ArtProvider.GetIcon(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.AddIcon(wx.ArtProvider.GetIcon(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.AddIcon(wx.ArtProvider.GetIcon(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        dvtc.SetImageList(il)

        self.root = dvtc.AppendContainer(dv.NullDataViewItem,
                                         "The Root Item",
                                         fldridx, fldropenidx)
        for x in range(15):
            child = dvtc.AppendContainer(self.root, "Item %d" % x,
                                         fldridx, fldropenidx)

            for y in range(5):
                last = dvtc.AppendContainer(
                    child, "item %d-%s" % (x, chr(ord("a")+y)),
                    fldridx, fldropenidx)

                for z in range(5):
                    item = dvtc.AppendItem(
                        last, "item %d-%s-%d" % (x, chr(ord("a")+y), z),
                        fileidx)

        # Set the layout so the treectrl fills the panel
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(dvtc, 1, wx.EXPAND)
        
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
            #f = open(os.path.join(self.dirname, self.filename), 'r')
            #self.control.SetValue(f.read())
            cls1 = LoaderClass(os.path.join(self.dirname, self.filename))
            cls1.LoadXMLFile(baseclass)
            
            
            
        dlg.Destroy()
        
        
app = wx.App(False)
frame = XmlBaseClass(None, "XML Editor")
app.MainLoop()