'''
Created on Jul 7, 2014

@author: user
'''

import wx
import wx.richtext


class MyFrame(wx.Frame):
    def __init__(self, parent, mytitle, mysize):
        wx.Frame.__init__(self, parent, wx.ID_ANY, mytitle, size=mysize)
        self.SetBackgroundColour("white")
        self.rich = wx.richtext.RichTextCtrl(self, wx.ID_ANY, value="")
        self.rich.WriteText("Default is black text.\n")
        self.rich.BeginBold()
        self.rich.WriteText("Write this text in bold")
        self.rich.BeginTextColour('red')
        self.rich.WriteText(" and this text in bold and red.\n")
        self.rich.EndTextColour()
        self.rich.EndBold()
        self.rich.BeginFontSize(30)
        self.rich.WriteText("This text has point size 30\n")
        self.rich.EndFontSize()
        font = wx.Font(16, wx.SCRIPT, wx.NORMAL, wx.LIGHT)
        self.rich.BeginFont(font)
        self.rich.WriteText("This text has a different font\n")
        self.rich.EndFont()
        self.rich.Newline()
        # indent the next items 100 units (tenths of a millimeter)
        self.rich.BeginLeftIndent(100)
        # insert an image you have in the work directory
        # or give the full path, can be .bmp .gif .png .jpg
       
        self.rich.Newline()
        self.rich.EndLeftIndent()
        
app = wx.App()
mytitle = 'testing wx.RichTextCtrl'
width = 560
height = 400
# create the MyFrame instance and show the frame
MyFrame(None, mytitle, (width, height)).Show()
app.MainLoop()