# -*- coding: utf-8 -*-

import pkg_resources
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
# We need plone.folder 1.0.5 or later to support simple reversing.
try:
    plone_folder = pkg_resources.get_distribution('plone.folder')
except pkg_resources.DistributionNotFound:
    SIMPLE_REVERSING = False
else:
    if plone_folder.version >= '1.0.5':
        SIMPLE_REVERSING = True
    else:
        SIMPLE_REVERSING = False


class SortContentsView(BrowserView):
    """The view for sorting folders"""

    template = ViewPageTemplateFile("sort_contents.pt")

    def __init__(self, context, request):
        self.context = context
        self.request = request
        # Watch out: if the restrictedTraverse fails and there is no
        # fallback, the action will not show up in the actions drop
        # down and you will see no error or warning about it.
        if context.restrictedTraverse('getObjPositionInParent', False):
            self.can_use_position_script = True
        else:
            self.can_use_position_script = False
        self.simple_reversing = SIMPLE_REVERSING
        self.request.set('disable_border', True)

    def __call__(self, *args, **kw):
        return self.template()
