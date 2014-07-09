import wx
import wx.dataview as dv
from lxml import etree

#----------------------------------------------------------------------


class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, wx.ID_ANY, "title", wx.DefaultPosition, size=(300, 300))

        # create the treectrl
        self.dvtc = dvtc = dv.DataViewTreeCtrl(self)

        isz = (16,16)
        il = wx.ImageList(*isz)
        fldridx     = il.AddIcon(wx.ArtProvider.GetIcon(wx.ART_FOLDER,      wx.ART_OTHER, isz))
        fldropenidx = il.AddIcon(wx.ArtProvider.GetIcon(wx.ART_FOLDER_OPEN, wx.ART_OTHER, isz))
        fileidx     = il.AddIcon(wx.ArtProvider.GetIcon(wx.ART_NORMAL_FILE, wx.ART_OTHER, isz))
        dvtc.SetImageList(il)
        
        recovering_parser = etree.XMLParser(recover=True)
        tree = etree.parse("DMC-TRENTXWB-A-26-12-19-00A01-720A-D_000-09_SX-US.xml", parser=recovering_parser)
        root = tree.getroot()
        
        parenttag = dvtc.AppendContainer(dv.NullDataViewItem,
                                         root.tag,
                                         fileidx, fileidx)
        
        
        def add(parenttag, elem):
            for e in elem:
                if elem.tag is etree.PI:
                    break
                item = dvtc.AppendContainer(parenttag, e.tag, fileidx, fileidx)
                dvtc.Expand(item)
                if e.text is not None:
                    #text = e.text.strip()
                    #dvtc.AppendItem(item, text, fileidx)
                    pass
                else:
                    #text = "None"
                    #dvtc.AppendItem(item, text, fileidx)
                    pass
                add(item, e)
        add(parenttag, root[1])
         
        
        """
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
        
        """
        # Set the layout so the treectrl fills the panel
        dvtc.__Collapse = False
        self.Sizer = wx.BoxSizer()
        self.Sizer.Add(dvtc, 1, wx.EXPAND)
        
        
app = wx.App(False)
frame = MyFrame(None)
frame.Show(True)
app.MainLoop()