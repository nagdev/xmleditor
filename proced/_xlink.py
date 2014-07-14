# .\_xlink.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:b43cd366527ddb6a0e58594876e07421e0148f30
# Generated 2014-07-13 21:22:00.733000 by PyXB version 1.2.3
# Namespace http://www.w3.org/1999/xlink [xmlns:xlink]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6151674f-0b0e-11e4-b5d8-7071bcf839fc')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/xlink', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 23, 2)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.onLoad = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'onLoad', tag=u'onLoad')
STD_ANON.onRequest = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'onRequest', tag=u'onRequest')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 61, 2)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.new = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'new', tag=u'new')
STD_ANON_.replace = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'replace', tag=u'replace')
STD_ANON_.embed = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'embed', tag=u'embed')
STD_ANON_.other = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'other', tag=u'other')
STD_ANON_.none = STD_ANON_._CF_enumeration.addEnumeration(unicode_value=u'none', tag=u'none')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 74, 2)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.simple = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'simple', tag=u'simple')
STD_ANON_2.extended = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value=u'extended', tag=u'extended')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)

# Complex type [anonymous] with content type EMPTY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 46, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'href'), 'href', '__httpwww_w3_org1999xlink_CTD_ANON_httpwww_w3_org1999xlinkhref', pyxb.binding.datatypes.string, required=True)
    __href._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 39, 1)
    __href._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 48, 3)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'label'), 'label', '__httpwww_w3_org1999xlink_CTD_ANON_httpwww_w3_org1999xlinklabel', pyxb.binding.datatypes.NMTOKEN, required=True)
    __label._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 44, 1)
    __label._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 50, 3)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_w3_org1999xlink_CTD_ANON_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default=u'locator')
    __type._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 47, 3)
    __type._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 47, 3)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org1999xlink_CTD_ANON_httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 71, 1)
    __title._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 49, 3)
    
    title = property(__title.value, __title.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __href.name() : __href,
        __label.name() : __label,
        __type.name() : __type,
        __title.name() : __title
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}label uses Python identifier label
    __label = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'label'), 'label', '__httpwww_w3_org1999xlink_CTD_ANON__httpwww_w3_org1999xlinklabel', pyxb.binding.datatypes.NMTOKEN, required=True)
    __label._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 44, 1)
    __label._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 57, 3)
    
    label = property(__label.value, __label.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_w3_org1999xlink_CTD_ANON__httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default=u'resource')
    __type._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 55, 3)
    __type._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 55, 3)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_w3_org1999xlink_CTD_ANON__httpwww_w3_org1999xlinktitle', pyxb.binding.datatypes.string)
    __title._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 71, 1)
    __title._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 56, 3)
    
    title = property(__title.value, __title.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __label.name() : __label,
        __type.name() : __type,
        __title.name() : __title
    })



# Complex type [anonymous] with content type EMPTY
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 31, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'actuate'), 'actuate', '__httpwww_w3_org1999xlink_CTD_ANON_2_httpwww_w3_org1999xlinkactuate', STD_ANON)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 22, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 117, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'type'), 'type', '__httpwww_w3_org1999xlink_CTD_ANON_2_httpwww_w3_org1999xlinktype', pyxb.binding.datatypes.anySimpleType, fixed=True, unicode_default=u'arc')
    __type._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 32, 3)
    __type._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 32, 3)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'from'), 'from_', '__httpwww_w3_org1999xlink_CTD_ANON_2_httpwww_w3_org1999xlinkfrom', pyxb.binding.datatypes.NMTOKEN)
    __from._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 38, 1)
    __from._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 33, 3)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'show'), 'show', '__httpwww_w3_org1999xlink_CTD_ANON_2_httpwww_w3_org1999xlinkshow', STD_ANON_)
    __show._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 60, 1)
    __show._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 116, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'to'), 'to', '__httpwww_w3_org1999xlink_CTD_ANON_2_httpwww_w3_org1999xlinkto', pyxb.binding.datatypes.NMTOKEN)
    __to._DeclarationLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 72, 1)
    __to._UseLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 34, 3)
    
    to = property(__to.value, __to.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __actuate.name() : __actuate,
        __type.name() : __type,
        __from.name() : __from,
        __show.name() : __show,
        __to.name() : __to
    })



locator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'locator'), CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 45, 1))
Namespace.addCategoryObject('elementBinding', locator.name().localName(), locator)

resource = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'resource'), CTD_ANON_, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 53, 1))
Namespace.addCategoryObject('elementBinding', resource.name().localName(), resource)

arc = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'arc'), CTD_ANON_2, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\xlink.xsd', 30, 1))
Namespace.addCategoryObject('elementBinding', arc.name().localName(), arc)
