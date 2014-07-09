'''
Created on Jul 8, 2014

@author: user
'''

import wx
import wx.richtext
from lxml import etree
import wx.dataview as dv


class TreePanelView(wx.Panel):
    '''
    shows tree control in this panel
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        wx.Panel.__init__(self, parent = parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetBackgroundColour('#ffffff')
        self.SetSizerAndFit(sizer)
        
    def updateTree(self, root):
        self.dvtc = dvtc = dv.DataViewTreeCtrl(self)

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
        bsizer = wx.BoxSizer()
        bsizer.Add(self.dvtc, 1, wx.EXPAND)
        self.SetSizerAndFit(bsizer)
        
        
class EditPanelView(wx.Panel):
    '''
    shows tree control in this panel
    '''
    def __init__(self, parent):
        '''
        Constructor
        '''
        wx.Panel.__init__(self, parent = parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetBackgroundColour('#D3D3D3')
        self.SetSizerAndFit(sizer)
    
    def updateEditor(self, root):
        
        self.SetBackgroundColour("white")
        
        xmltr = etree.tostring(root, encoding='utf8', method='xml')
        
        
        self.rich = wx.richtext.RichTextCtrl( self, size = wx.DisplaySize(), style = wx.WANTS_CHARS | wx.richtext.RE_MULTILINE )
        
        bsizer = wx.BoxSizer()
        bsizer.Add(self.rich, 1, wx.EXPAND)
        self.SetSizerAndFit(bsizer)
        
        self.rich.WriteText(xmltr)
        self.rich.Newline()
        self.rich.EndLeftIndent()