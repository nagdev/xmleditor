# .\_dc.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0e3b9156ff17f2d5b8c4bd3a824a7282543d8f4d
# Generated 2014-07-13 21:21:53.982000 by PyXB version 1.2.3
# Namespace http://www.purl.org/dc/elements/1.1/ [xmlns:dc]

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
import _nsgroup as _ImportedBinding__nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.purl.org/dc/elements/1.1/', create_if_missing=True)
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

from _nsgroup import title # {http://www.purl.org/dc/elements/1.1/}title
from _nsgroup import creator # {http://www.purl.org/dc/elements/1.1/}creator
from _nsgroup import subject # {http://www.purl.org/dc/elements/1.1/}subject
from _nsgroup import publisher # {http://www.purl.org/dc/elements/1.1/}publisher
from _nsgroup import contributor # {http://www.purl.org/dc/elements/1.1/}contributor
from _nsgroup import date # {http://www.purl.org/dc/elements/1.1/}date
from _nsgroup import type # {http://www.purl.org/dc/elements/1.1/}type
from _nsgroup import format # {http://www.purl.org/dc/elements/1.1/}format
from _nsgroup import identifier # {http://www.purl.org/dc/elements/1.1/}identifier
from _nsgroup import language # {http://www.purl.org/dc/elements/1.1/}language
from _nsgroup import rights # {http://www.purl.org/dc/elements/1.1/}rights
from _nsgroup import SECURITY # {http://www.purl.org/dc/elements/1.1/}SECURITY
from _nsgroup import LANGUAGE_COUNTRY # {http://www.purl.org/dc/elements/1.1/}LANGUAGE-COUNTRY
