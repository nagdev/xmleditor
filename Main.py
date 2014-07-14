'''
Created on Jul 7, 2014

@author: user
'''
import wx
import XMLEditor.XmlBaseClass as BaseClass

class XMLEditor(wx.App):
    """
        XML Editor Class
    """
    def OnInit(self):
        self.frame = BaseClass.XmlBaseClass(None, "XML Editor")
        self.frame.Show(True)
        return True
        
        
if __name__ == "__main__":
    app = XMLEditor(False)
    app.MainLoop()
