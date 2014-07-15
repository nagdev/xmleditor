'''
Created on Jul 9, 2014

@author: user
'''

import wx

class KeyEvents(wx.Frame):
    '''
    classdocs
    '''
    __treePanel = None
    __sourcePanel = None
    __baseClass = None
    
    def __init__(self, treePanel, sourcePanel, baseClass):
        '''
        Constructor
        '''
        
        self.__treePanel = treePanel
        self.__sourcePanel = sourcePanel
        self.__baseClass = baseClass
        sourcePanel.Bind(wx.EVT_KEY_DOWN, self.KeyPressed, sourcePanel)
        
        
    def InitializeEditorEvents(self, editor):
        editor.Bind(wx.EVT_KEY_DOWN, self.KeyPressed, editor)
            
        
    
    def KeyPressed(self, e):
        key = GetKeyPress(e)
        print key
        if key == "Ctrl+O":
            self.__baseClass.onOpen(e = None)
        if key == "Ctrl+Q":
            self.__baseClass.onExit(e = None)
        if key == "Ctrl+S":
            self.__baseClass.onSave(e = None)
        if key == "Ctrl+Shift+K":
            self.__sourcePanel.ShowTagLists()
            
    
            
        e.Skip()
        
    def SaveDocument(self, e):
        #key = GetKeyPress(e)
        #if key == "Ctrl+S":
        #    self.__baseClass.onSave(e = None)
        #e.Skip()
        print "apple"  
        
        
        
        
keyMap = {}

def gen_keymap():
    keys = ("BACK", "TAB", "RETURN", "ESCAPE", "SPACE", "DELETE", "START",
        "LBUTTON", "RBUTTON", "CANCEL", "MBUTTON", "CLEAR", "PAUSE",
        "CAPITAL", "PRIOR", "NEXT", "END", "HOME", "LEFT", "UP", "RIGHT",
        "DOWN", "SELECT", "PRINT", "EXECUTE", "SNAPSHOT", "INSERT", "HELP",
        "NUMPAD0", "NUMPAD1", "NUMPAD2", "NUMPAD3", "NUMPAD4", "NUMPAD5",
        "NUMPAD6", "NUMPAD7", "NUMPAD8", "NUMPAD9", "MULTIPLY", "ADD",
        "SEPARATOR", "SUBTRACT", "DECIMAL", "DIVIDE", "F1", "F2", "F3", "F4",
        "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13", "F14",
        "F15", "F16", "F17", "F18", "F19", "F20", "F21", "F22", "F23", "F24",
        "NUMLOCK", "SCROLL", "PAGEUP", "PAGEDOWN", "NUMPAD_SPACE",
        "NUMPAD_TAB", "NUMPAD_ENTER", "NUMPAD_F1", "NUMPAD_F2", "NUMPAD_F3",
        "NUMPAD_F4", "NUMPAD_HOME", "NUMPAD_LEFT", "NUMPAD_UP",
        "NUMPAD_RIGHT", "NUMPAD_DOWN", "NUMPAD_PRIOR", "NUMPAD_PAGEUP",
        "NUMPAD_NEXT", "NUMPAD_PAGEDOWN", "NUMPAD_END", "NUMPAD_BEGIN",
        "NUMPAD_INSERT", "NUMPAD_DELETE", "NUMPAD_EQUAL", "NUMPAD_MULTIPLY",
        "NUMPAD_ADD", "NUMPAD_SEPARATOR", "NUMPAD_SUBTRACT", "NUMPAD_DECIMAL",
        "NUMPAD_DIVIDE")

    for i in keys:
        keyMap[getattr(wx, "WXK_"+i)] = i
    for i in ("SHIFT", "ALT", "CONTROL", "MENU"):
        keyMap[getattr(wx, "WXK_"+i)] = ''
        
        
def GetKeyPress(evt):
    keycode = evt.GetKeyCode()
    keyname = keyMap.get(keycode, None)
    modifiers = ""
    for mod, ch in ((evt.ControlDown(), 'Ctrl+'),
                    (evt.AltDown(),     'Alt+'),
                    (evt.ShiftDown(),   'Shift+'),
                    (evt.MetaDown(),    'Meta+')):
        if mod:
            modifiers += ch

    if keyname is None:
        if 27 < keycode < 256:
            keyname = chr(keycode)
        else:
            keyname = "(%s)unknown" % keycode
    return modifiers + keyname
        
        
        
        
        