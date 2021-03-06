#                                                         -*- coding: utf-8 -*-
#! \file    ~/doit_doc_template/templates/base/library/cmd_adduri.py
#! \author  Jiří Kučera, <sanczes AT gmail.com>
#! \stamp   2019-07-21 14:48:48 +0200
#! \project DoIt! Doc: Sphinx Extension for DoIt! Documentation
#! \license MIT
#! \version See doit_doc_template.__version__
#! \brief   See __doc__
#
"""\
adduri command.\
"""

__license__ = """\
Copyright (c) 2014 - 2019 Jiří Kučera.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.\
"""

from doit_doc_template.core.action import get_str
from doit_doc_template.core.errors import BadArgsError
from doit_doc_template.core.keywords import \
    KW_NAMES, KW_NODE, KW_REFURI, KW_TRANSLATOR

from .type_page import Page

def cmd_adduri(action, context):
    """
    """

    varname = get_str(action, context, "Variable name is expected")
    page = context.kwargs[KW_TRANSLATOR].context.get(varname)
    if page is None:
        raise BadArgsError(varname, "{} is undefined".format(varname))
    if not isinstance(page, Page):
        raise BadArgsError(varname, "{} is not a page".format(varname))
    node = context.kwargs[KW_NODE]
    if KW_REFURI not in node.attributes:
        return
    names = node.attributes.get(KW_NAMES, [])
    uri = node.attributes[KW_REFURI]
    for name in names:
        page.adduri(name, uri)
#-def
