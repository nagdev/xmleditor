'''
Created on Jul 8, 2014

@author: user
'''

import wx
import wx.grid as gridlib

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