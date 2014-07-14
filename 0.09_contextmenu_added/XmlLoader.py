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
        self.__fileName = fileName
        
        """
         #<xsl:output method="xml" indent="yes" omit-xml-declaration="no"/>
        xslt_root = etree.XML('''\
            <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
                <xsl:variable name="vAllowedSymbols"
                    select="'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'"/>
                <xsl:template match="node() | @*">
                    <xsl:copy>
                        <xsl:apply-templates select="node() | @*"/>
                    </xsl:copy>
                </xsl:template>
                <xsl:function name="lancet:stripSpecialChars">
    <xsl:param name="string" />
    <xsl:variable name="AllowedSymbols" select="'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()*%$#@!~&lt;&gt;,.?[]=- +   /\ '"/>
    <xsl:value-of select="
        translate(
            $string,
            translate($string, $AllowedSymbols, ''),
            ' ')
        "/>
</xsl:function> 
                <xsl:value-of select="lancet:stripSpecialChars($string)"/>
                </xsl:template>
            </xsl:stylesheet>
        ''')
        transform = etree.XSLT(xslt_root)
        
        """
        
        xmlschema_doc = etree.parse("schema/proced.xsd")
        xmlschema = etree.XMLSchema(xmlschema_doc)
        
        recovering_parser = etree.XMLParser(recover=True)
        self.__tree = etree.parse(self.__txt, parser=recovering_parser)
        
        if not xmlschema(self.__tree):
            self.__baseClass.DisplayInfo("Loaded XML is not valid against Schema proced.xsd")            
        else:
            
            root = self.__tree.getroot()
            
            #get entity 
            
            xmlstr =  etree.tostring(self.__tree, xml_declaration=True, encoding="utf-8")
            xmlstr.find("<"+root.tag, 0)
            
            xmlstrPos = etree.tostring(self.__tree, xml_declaration=True, encoding="utf-8").find("<"+root.tag, 0)
            xmlEntity = xmlstr[0:xmlstrPos]
                        
            treePanel.updateTree(root)
            editPanel.updateEditor(root, self.__tree, fileName, keyEvents, dir, self.__txt, xmlEntity, xmlschema_doc)
         
            
            
            
                
                
            