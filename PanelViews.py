'''
Created on Jul 8, 2014

@author: user
'''

import wx
import wx.richtext
from lxml import etree


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
        self.SetSizer(sizer)
        
    def updateTree(self, root):
       pass
        
        
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
        self.SetSizer(sizer)
    
    def updateEditor(self, root):
        
        self.SetBackgroundColour("white")
        
        xmltr = etree.tostring(root, encoding='utf8', method='xml')
        
        
        self.rich = wx.richtext.RichTextCtrl( self, size = ( 300, 800 ), style = wx.WANTS_CHARS | wx.richtext.RE_MULTILINE )
        self.rich.WriteText(xmltr)
        self.rich.Newline()
        self.rich.EndLeftIndent()