# xml loader
from lxml import etree
import PanelViews
import wx



class XmlLoader():
    
    __txt = None
    __tree = None
    __baseClass = None
    __keyEvents = None
    
    def __init__(self, filePath):
        """ app """#
        self.__txt = filePath
            
    def LoadXMLFile(self, baseclass, treePanel, editPanel, fileName, keyEvents, dir):
        self.__baseClass = baseclass
        xmlschema_doc = etree.parse("schema/proced.xsd")
        xmlschema = etree.XMLSchema(xmlschema_doc)
        
        recovering_parser = etree.XMLParser(recover=True)
        self.__tree = etree.parse(self.__txt, parser=recovering_parser)
        
        if not xmlschema(self.__tree):
            self.__baseClass.DisplayInfo("Loaded XML is not valid against Schema proced.xsd")            
        else:
            #self.__baseClass.DisplayInfo("Loaded XML is valid against Schema proced.xsd")
            root = self.__tree.getroot()
            treePanel.updateTree(root)
            editPanel.updateEditor(root, self.__tree, fileName, keyEvents, dir, self.__txt)
            
            
            
            
                
                
            