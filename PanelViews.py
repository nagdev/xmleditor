'''
Created on Jul 8, 2014

@author: user
'''

import wx
import wx.richtext
from lxml import etree
import wx.dataview as dv
import wx.stc as stc
from KeyEvents import KeyEvents
import xml.etree.ElementTree as ET
import os
import StringIO
import re
from types import NoneType
from operator import pos
import proced.proced as schemadoc


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
        # Set the layout so the treectrl fills the panel
        bsizer = wx.BoxSizer()
        bsizer.Add(self.dvtc, 1, wx.EXPAND)
        self.SetSizerAndFit(bsizer)
        

class ContextMenu(object):
    
    winpos = None
    editor = None
    dict = {}
    
    
    def __init__(self, winpos, editor, tags):
        super(ContextMenu, self).__init__()
        self._menu = None
        self.winpos = winpos
        self.editor = editor
        self.tags = tags
        self.OnContextMenu()
        

    def OnContextMenu(self):
        if self._menu is not None:
            self._menu.Destroy()
        self._menu = wx.Menu()
        self.CreateContextMenu(self._menu)
        self.PopupMenu(self._menu, self.winpos)
        
        
    
    def CreateContextMenu(self, menu):
        listCt = 205
        for tag in self.tags:
            contextMenuAdd = self._menu.Append(listCt, "&"+tag.get("ref"))
            self._menu.Bind(wx.EVT_MENU, self.onAddClick, id=listCt)
            self.dict[listCt] = tag.get("ref")
            listCt = listCt + 1
            
        
    def onAddClick(self, event):
        self._menu.Destroy()
        self.editor.AddNewTag(self.dict[event.GetId()])
        
    
class AttributesDialog(wx.Dialog):
    """
     pop dialog for adding tag attriubues
    """
    attibutesDialog = {}
    
    def __init__(self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE):
        
        
        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, ID, title, pos, size, style)
        
        self.PostCreate(pre)
        
        
        # contents
        sizer = wx.BoxSizer(wx.VERTICAL)

        label = wx.StaticText(self, -1, "Element: "+parent.childTag)
        label.SetHelpText("Attributes for "+parent.childTag)
        sizer.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)

        ##################################attribues
        
        for attribute in parent.attributes:
            attr =  attribute.get("ref")
            
            box = wx.BoxSizer(wx.HORIZONTAL)

            label = wx.StaticText(self, -1, attr+":")
            label.SetHelpText("This is the help text for the "+attr)
            box.Add(label, 0, wx.ALIGN_CENTRE|wx.ALL, 5)
    
            text = wx.TextCtrl(self, -1, "", size=(80,-1))
            text.SetHelpText("Here's some help text for "+attr)
            box.Add(text, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
            
            self.attibutesDialog[attr] = text
    
            sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        #######################################end

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        btnsizer = wx.StdDialogButtonSizer()
        
        if wx.Platform != "__WXMSW__":
            btn = wx.ContextHelpButton(self)
            btnsizer.AddButton(btn)
        
        btn = wx.Button(self, wx.ID_OK)
        btn.SetHelpText("The OK button completes the dialog")
        btn.SetDefault()
        btnsizer.AddButton(btn)

        btn = wx.Button(self, wx.ID_CANCEL)
        btn.SetHelpText("The Cancel button cancels the dialog. (Cool, huh?)")
        btnsizer.AddButton(btn)
        btnsizer.Realize()

        sizer.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)
    
        
class EditPanelView(wx.Panel, ContextMenu):
    '''
    shows tree control in this panel
    '''
    
    __xmlRoot = None;
    __xmlFile = None;
    __xmlFileName = None;
    __editor = None
    __keyEvents = None
    __dir = None
    __filePath = None
    __xmlEntity = None
    
    
    def __init__(self, parent):
        '''
        Constructor
        '''
        
        
        wx.Panel.__init__(self, parent = parent)
        
        
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetBackgroundColour('#D3D3D3')
        self.SetSizerAndFit(sizer)
    
    def updateEditor(self, root, xmlFile, fileName, keyEvents, dir, filepath, xmlEntity, xmlschema_doc):
        
        self.__xmlRoot = root
        self.__xmlFile = xmlFile
        self.__xmlFileName = fileName
        self.__keyEvents = keyEvents
        self.__dir = dir
        self.__filePath = filepath
        self.__xmlEntity = xmlEntity
        self.xmlschema_doc = xmlschema_doc
       
        
        self.SetBackgroundColour("white")
        
        xmltr = etree.tostring(root, encoding='utf8', method='xml')
        
        self.__editor = editor = SourceXMLText(self, wx.ID_ANY)
        
        bsizer = wx.BoxSizer()
        bsizer.Add(editor, 1, wx.EXPAND)
        self.SetSizerAndFit(bsizer)
        
        editor.SetText(xmltr)
        editor.EmptyUndoBuffer()
        editor.Colourise(0, -1)
        
        
        # line numbers in the margin
        editor.SetMarginType(1, stc.STC_MARGIN_NUMBER)
        editor.SetMarginWidth(1, 40)
        
        
        #editor.autoindent() 
        
        self.__keyEvents.InitializeEditorEvents(editor)
        
    def SaveXML(self, e):
            """
                save current xml file
            """
            if self.__editor is not None:
                newXmlElement = self.__xmlEntity+""+self.__editor.GetTextUTF8();
                recovering_parser = etree.XMLParser(recover=True)
                newTree = etree.parse(StringIO.StringIO(newXmlElement), parser=recovering_parser)
                newTree.write(os.path.join(self.__dir, self.__xmlFileName), pretty_print=True, xml_declaration=True, encoding="utf-8")
    
    def FindAndReplace(self):
        searchText = self.__editor.GetSelectedText()
        
        data = wx.FindReplaceData()
        data.SetFindString(searchText)
        self.findReplaceData = data
        dlg = wx.FindReplaceDialog(self, data, "Find")
        
    
        dlg.Bind(wx.EVT_FIND, self.OnFind)
        dlg.Bind(wx.EVT_FIND_NEXT, self.OnFind)
        dlg.Bind(wx.EVT_FIND_REPLACE, self.OnFind)
        dlg.Bind(wx.EVT_FIND_REPLACE_ALL, self.OnFind)
        dlg.Bind(wx.EVT_FIND_CLOSE, self.OnFindClose)
        
        dlg.Show()
        self.findDialog = dlg
       
    def OnFind(self, evt):
        #print repr(evt.GetFindString()), repr(self.findData.GetFindString())
        self.__editor.FindText(1, 200, "dmAddressItems")
        
        map = {
            wx.wxEVT_COMMAND_FIND : "FIND",
            wx.wxEVT_COMMAND_FIND_NEXT : "FIND_NEXT",
            wx.wxEVT_COMMAND_FIND_REPLACE : "REPLACE",
            wx.wxEVT_COMMAND_FIND_REPLACE_ALL : "REPLACE_ALL",
            }

        et = evt.GetEventType()
        
        if et in map:
            evtType = map[et]
        else:
            evtType = "**Unknown Event Type**"

        if et in [wx.wxEVT_COMMAND_FIND_REPLACE, wx.wxEVT_COMMAND_FIND_REPLACE_ALL]:
            replaceTxt = "Replace text: %s" % evt.GetReplaceString()
        else:
            replaceTxt = ""

    


    def OnFindClose(self, evt):
        evt.GetDialog().Destroy()
        
                    
            
    def ShowTagLists(self):
        pos =  self.__editor.GetInsertionPoint()
        tagNameStartPos = self.__editor.GetText().rfind('<', 0, pos)
        tagNameEndPos = self.__editor.GetText().rfind('>', 0, pos)
        tagNamePos =  self.__editor.GetText()[tagNameStartPos:tagNameEndPos]
        if tagNamePos.find("/", 0) < 0:
            tagstate = "child"
        else:
            tagstate = "parent"
        self.targetTag = re.search("[\w+]+", tagNamePos)
        appendToText = self.targetTag.group() 
                
        if self.targetTag is not None:
            tags = self.getElems(self.xmlschema_doc, appendToText)
            winpos = self.__editor.PointFromPosition(self.__editor.GetCurrentPos())
            ContextMenu.__init__(self, winpos, self, tags)
        
    def getElems(self, xmlschema_doc, typeName):
        names = xmlschema_doc.xpath("//xs:complexType[@name = $n]/xs:sequence/xs:element",
                                    namespaces={
                                      "xs":"http://www.w3.org/2001/XMLSchema"},
                                       n=typeName+"ElemType"
                                   )
        
        
     
        return names
        
        #print etree.SubElement(xmlschema_doc, names[0])
            
    def AddNewTag(self, tag):
        """
         get all attribute for given parent tag using xpath
        """
        self.childTag = tag
        attributes = self.xmlschema_doc.xpath("//xs:complexType[@name = $n]/xs:attribute",
                                    namespaces={
                                      "xs":"http://www.w3.org/2001/XMLSchema"},
                                       n=tag+"ElemType"
                                   )
        
        
        self.attributes = attributes
        
        if len(attributes) > 0:
            dlg = AttributesDialog(self, -1, "Attributes", size=(350, 200), pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE)
            dlg.CenterOnScreen()
            # this does not return until the dialog is closed.
            val = dlg.ShowModal()
            attr = ""
            if val == wx.ID_OK:
               print dlg.attibutesDialog
               for attrlist in dlg.attibutesDialog:
                   attrvalue = dlg.attibutesDialog[attrlist].GetValue()
                   attr += attrlist+"=\""+attrvalue+"\" "
                    
            else:
                pass
            dlg.Destroy()
            newChildTag = "<"+tag+" "+attr+"></"+tag+">"
            self.__editor.InsertText(self.__editor.GetInsertionPoint(), newChildTag)
        else:
            #add child tag directly
            newChildTag = "<"+tag+"></"+tag+">"
            self.__editor.InsertText(self.__editor.GetInsertionPoint(), newChildTag) 
        
    def updateXML(self):
        pass
    
            
        
        
        

         

class SourceXMLText(stc.StyledTextCtrl):
        """
        styled text control
        """
        fold_symbols = 2
        
        def __init__(self, parent, ID,
                pos=wx.DefaultPosition, size=wx.DefaultSize,
                style=0):
                stc.StyledTextCtrl.__init__(self, parent, ID, pos, size, style)
        
                self.CmdKeyAssign(ord('='), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMIN)
                self.CmdKeyAssign(ord('-'), stc.STC_SCMOD_CTRL, stc.STC_CMD_ZOOMOUT)
        
                self.SetLexer(stc.STC_LEX_XML)
                
                self.SetProperty("fold", "1")
                self.SetProperty("fold.html", "1")
                self.SetMargins(0,0)
        
                self.SetViewWhiteSpace(False)
                
                self.SetWrapMode(stc.STC_WRAP_CHAR) 
                #self.SetEdgeMode(stc.STC_EDGE_BACKGROUND)
                #self.SetEdgeColumn(78)

                # Setup a margin to hold fold markers
                #self.SetFoldFlags(16)  ###  WHAT IS THIS VALUE?  WHAT ARE THE OTHER FLAGS?  DOES IT MATTER?
                self.SetMarginType(2, stc.STC_MARGIN_SYMBOL)
                self.SetMarginMask(2, stc.STC_MASK_FOLDERS)
                self.SetMarginSensitive(2, True)
                self.SetMarginWidth(2, 12)
                

                if self.fold_symbols == 0:
                    # Arrow pointing right for contracted folders, arrow pointing down for expanded
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_ARROWDOWN, "black", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_ARROW, "black", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_EMPTY, "black", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_EMPTY, "black", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_EMPTY,     "white", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_EMPTY,     "white", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_EMPTY,     "white", "black")
                    
                elif self.fold_symbols == 1:
                    # Plus for contracted folders, minus for expanded
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_MINUS, "white", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_PLUS,  "white", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_EMPTY, "white", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_EMPTY, "white", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_EMPTY, "white", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_EMPTY, "white", "black")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_EMPTY, "white", "black")
        
                elif self.fold_symbols == 2:
                    # Like a flattened tree control using circular headers and curved joins
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_CIRCLEMINUS,          "white", "#404040")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_CIRCLEPLUS,           "white", "#404040")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,                "white", "#404040")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNERCURVE,         "white", "#404040")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_CIRCLEPLUSCONNECTED,  "white", "#404040")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_CIRCLEMINUSCONNECTED, "white", "#404040")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNERCURVE,         "white", "#404040")
        
                elif self.fold_symbols == 3:
                    # Like a flattened tree control using square headers
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPEN,    stc.STC_MARK_BOXMINUS,          "white", "#808080")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDER,        stc.STC_MARK_BOXPLUS,           "white", "#808080")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERSUB,     stc.STC_MARK_VLINE,             "white", "#808080")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERTAIL,    stc.STC_MARK_LCORNER,           "white", "#808080")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEREND,     stc.STC_MARK_BOXPLUSCONNECTED,  "white", "#808080")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDEROPENMID, stc.STC_MARK_BOXMINUSCONNECTED, "white", "#808080")
                    self.MarkerDefine(stc.STC_MARKNUM_FOLDERMIDTAIL, stc.STC_MARK_TCORNER,           "white", "#808080")


                
    
                # Make some styles,  The lexer defines what each style is used for, we
                # just have to define what each style looks like.  This set is adapted from
                # Scintilla sample property files.
        
                # Global default styles for all languages
                self.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
                self.StyleClearAll()  # Reset all to be like the default
        
                # Global default styles for all languages
                self.StyleSetSpec(stc.STC_STYLE_DEFAULT,     "face:%(helv)s,size:%(size)d" % faces)
                self.StyleSetSpec(stc.STC_STYLE_LINENUMBER,  "back:#C0C0C0,face:%(helv)s,size:%(size2)d" % faces)
                self.StyleSetSpec(stc.STC_STYLE_CONTROLCHAR, "face:%(other)s" % faces)
                self.StyleSetSpec(stc.STC_STYLE_BRACELIGHT,  "fore:#FFFFFF,back:#0000FF,bold")
                self.StyleSetSpec(stc.STC_STYLE_BRACEBAD,    "fore:#000000,back:#FF0000,bold")
    
                # Python styles
                # Default 
                self.StyleSetSpec(stc.STC_P_DEFAULT, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
                # Comments
                self.StyleSetSpec(stc.STC_P_COMMENTLINE, "fore:#007F00,face:%(other)s,size:%(size)d" % faces)
                # Number
                self.StyleSetSpec(stc.STC_P_NUMBER, "fore:#007F7F,size:%(size)d" % faces)
                # String
                self.StyleSetSpec(stc.STC_P_STRING, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
                # Single quoted string
                self.StyleSetSpec(stc.STC_P_CHARACTER, "fore:#7F007F,face:%(helv)s,size:%(size)d" % faces)
                # Keyword
                self.StyleSetSpec(stc.STC_P_WORD, "fore:#00007F,bold,size:%(size)d" % faces)
                # Triple quotes
                self.StyleSetSpec(stc.STC_P_TRIPLE, "fore:#7F0000,size:%(size)d" % faces)
                # Triple double quotes
                self.StyleSetSpec(stc.STC_P_TRIPLEDOUBLE, "fore:#7F0000,size:%(size)d" % faces)
                # Class name definition
                self.StyleSetSpec(stc.STC_P_CLASSNAME, "fore:#0000FF,bold,size:%(size)d" % faces)
                # Function or method name definition
                self.StyleSetSpec(stc.STC_P_DEFNAME, "fore:#007F7F,bold,size:%(size)d" % faces)
                # Operators
                self.StyleSetSpec(stc.STC_P_OPERATOR, "size:%(size)d" % faces)
                # Identifiers
                self.StyleSetSpec(stc.STC_P_IDENTIFIER, "fore:#000000,face:%(helv)s,size:%(size)d" % faces)
                # Comment-blocks
                self.StyleSetSpec(stc.STC_P_COMMENTBLOCK, "fore:#7F7F7F,size:%(size)d" % faces)
                # End of line where string is not closed
                self.StyleSetSpec(stc.STC_P_STRINGEOL, "fore:#7F7F7F,face:%(mono)s,eol,size:%(size)d" % faces)
        
                self.SetCaretForeground("BLUE")
            
        
                
                
provider = wx.SimpleHelpProvider()
wx.HelpProvider.Set(provider)                
        


if wx.Platform == '__WXMSW__':
    faces = { 'times': 'Arial',
              'mono' : 'Arial',
              'helv' : 'Arial',
              'other': 'Arial',
              'size' : 12,
              'size2': 10,
             }
elif wx.Platform == '__WXMAC__':
    faces = { 'times': 'Arial',
              'mono' : 'Arial',
              'helv' : 'Arial',
              'other': 'Arial',
              'size' : 12,
              'size2': 12,
             }
else:
    faces = { 'times': 'Arial',
              'mono' : 'Arial',
              'helv' : 'Arial',
              'other': 'Arial',
              'size' : 12,
              'size2': 12,
             }
 
        