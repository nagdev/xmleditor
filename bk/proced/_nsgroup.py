# .\_nsgroup.py
# -*- coding: utf-8 -*-
# PyXB bindings for NGM:eda8ee6049a70cff4ee5ef1b322739b6f309f050
# Generated 2014-07-13 21:22:00.732000 by PyXB version 1.2.3
# Group contents:
# Namespace http://www.purl.org/dc/elements/1.1/ [xmlns:dc]
# Namespace http://www.w3.org/1999/02/22-rdf-syntax-ns# [xmlns:rdf]


import pyxb
import pyxb.binding
import pyxb.utils.utility

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6151674f-0b0e-11e4-b5d8-7071bcf839fc')

# Import bindings for schemas in group
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
_Namespace_dc = pyxb.namespace.NamespaceForURI(u'http://www.purl.org/dc/elements/1.1/', create_if_missing=True)
_Namespace_dc.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_rdf = pyxb.namespace.NamespaceForURI(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#', create_if_missing=True)
_Namespace_rdf.configureCategories(['typeBinding', 'elementBinding'])

# Atomic simple type: {http://www.purl.org/dc/elements/1.1/}SECURITY
class SECURITY (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dc, u'SECURITY')
    _XSDLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 50, 1)
    _Documentation = None
SECURITY._CF_pattern = pyxb.binding.facets.CF_pattern()
SECURITY._CF_pattern.addPattern(pattern=u'[0-9]{1,2}(_(cc[0-9]{2})?(_cv[0-9]{2})?)?')
SECURITY._InitializeFacetMap(SECURITY._CF_pattern)
_Namespace_dc.addCategoryObject('typeBinding', u'SECURITY', SECURITY)

# Atomic simple type: {http://www.purl.org/dc/elements/1.1/}LANGUAGE-COUNTRY
class LANGUAGE_COUNTRY (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_dc, u'LANGUAGE-COUNTRY')
    _XSDLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 56, 1)
    _Documentation = None
LANGUAGE_COUNTRY._CF_pattern = pyxb.binding.facets.CF_pattern()
LANGUAGE_COUNTRY._CF_pattern.addPattern(pattern=u'[a-z]{2,3}(-[A-Z]{2})?')
LANGUAGE_COUNTRY._InitializeFacetMap(LANGUAGE_COUNTRY._CF_pattern)
_Namespace_dc.addCategoryObject('typeBinding', u'LANGUAGE-COUNTRY', LANGUAGE_COUNTRY)

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\rdf.xsd', 24, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.purl.org/dc/elements/1.1/}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'title'), 'title', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1title', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 22, 1), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}creator uses Python identifier creator
    __creator = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'creator'), 'creator', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1creator', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 23, 1), )

    
    creator = property(__creator.value, __creator.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}subject uses Python identifier subject
    __subject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'subject'), 'subject', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1subject', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 24, 1), )

    
    subject = property(__subject.value, __subject.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}publisher uses Python identifier publisher
    __publisher = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'publisher'), 'publisher', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1publisher', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 25, 1), )

    
    publisher = property(__publisher.value, __publisher.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}contributor uses Python identifier contributor
    __contributor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'contributor'), 'contributor', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1contributor', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 26, 1), )

    
    contributor = property(__contributor.value, __contributor.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}date uses Python identifier date
    __date = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'date'), 'date', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1date', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 27, 1), )

    
    date = property(__date.value, __date.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}type uses Python identifier type
    __type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'type'), 'type', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1type', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 28, 1), )

    
    type = property(__type.value, __type.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}format uses Python identifier format
    __format = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'format'), 'format', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1format', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 29, 1), )

    
    format = property(__format.value, __format.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}identifier uses Python identifier identifier
    __identifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'identifier'), 'identifier', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1identifier', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 30, 1), )

    
    identifier = property(__identifier.value, __identifier.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}language uses Python identifier language
    __language = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'language'), 'language', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1language', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 31, 1), )

    
    language = property(__language.value, __language.set, None, None)

    
    # Element {http://www.purl.org/dc/elements/1.1/}rights uses Python identifier rights
    __rights = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_dc, u'rights'), 'rights', '__httpwww_w3_org19990222_rdf_syntax_ns_CTD_ANON_httpwww_purl_orgdcelements1_1rights', True, pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 32, 1), )

    
    rights = property(__rights.value, __rights.set, None, None)

    _ElementMap.update({
        __title.name() : __title,
        __creator.name() : __creator,
        __subject.name() : __subject,
        __publisher.name() : __publisher,
        __contributor.name() : __contributor,
        __date.name() : __date,
        __type.name() : __type,
        __format.name() : __format,
        __identifier.name() : __identifier,
        __language.name() : __language,
        __rights.name() : __rights
    })
    _AttributeMap.update({
        
    })



title = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'title'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 22, 1))
_Namespace_dc.addCategoryObject('elementBinding', title.name().localName(), title)

creator = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'creator'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 23, 1))
_Namespace_dc.addCategoryObject('elementBinding', creator.name().localName(), creator)

subject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'subject'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 24, 1))
_Namespace_dc.addCategoryObject('elementBinding', subject.name().localName(), subject)

publisher = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'publisher'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 25, 1))
_Namespace_dc.addCategoryObject('elementBinding', publisher.name().localName(), publisher)

contributor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'contributor'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 26, 1))
_Namespace_dc.addCategoryObject('elementBinding', contributor.name().localName(), contributor)

date = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'date'), pyxb.binding.datatypes.date, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 27, 1))
_Namespace_dc.addCategoryObject('elementBinding', date.name().localName(), date)

type = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'type'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 28, 1), fixed=True, unicode_default=u'text')
_Namespace_dc.addCategoryObject('elementBinding', type.name().localName(), type)

format = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'format'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 29, 1), fixed=True, unicode_default=u'text/xml')
_Namespace_dc.addCategoryObject('elementBinding', format.name().localName(), format)

identifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'identifier'), pyxb.binding.datatypes.string, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 30, 1))
_Namespace_dc.addCategoryObject('elementBinding', identifier.name().localName(), identifier)

language = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'language'), LANGUAGE_COUNTRY, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 31, 1))
_Namespace_dc.addCategoryObject('elementBinding', language.name().localName(), language)

rights = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'rights'), SECURITY, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 32, 1))
_Namespace_dc.addCategoryObject('elementBinding', rights.name().localName(), rights)

Description = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_rdf, u'Description'), CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\rdf.xsd', 23, 1))
_Namespace_rdf.addCategoryObject('elementBinding', Description.name().localName(), Description)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'title'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 22, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'creator'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 23, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'subject'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 24, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'publisher'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 25, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'contributor'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 26, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'date'), pyxb.binding.datatypes.date, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 27, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'type'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 28, 1), fixed=True, unicode_default=u'text'))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'format'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 29, 1), fixed=True, unicode_default=u'text/xml'))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'identifier'), pyxb.binding.datatypes.string, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 30, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'language'), LANGUAGE_COUNTRY, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 31, 1)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_dc, u'rights'), SECURITY, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 32, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\rdf.xsd', 26, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'title')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'creator')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 37, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'subject')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 38, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'publisher')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 39, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'contributor')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 40, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'date')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 41, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'type')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 42, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'format')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 43, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'identifier')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 44, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'language')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 45, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(_Namespace_dc, u'rights')), pyxb.utils.utility.Location(u'i:\\xml_editor\\xml_editor\\schema\\dc.xsd', 46, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()

