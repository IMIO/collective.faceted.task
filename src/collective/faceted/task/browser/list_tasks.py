# -*- coding: utf-8 -*-

from plone import api

from collective.faceted.task import _
from collective.faceted.task.browser.table import FacetedTasksTable

from collective.task.behaviors import ITask

from Products.Five.browser import BrowserView

from zope.interface import implements
from zope.viewlet.interfaces import IViewlet


class TasksListBase(BrowserView):
    """
    Base class for both the view and viewlet
    rendering the task listing.
    """
    noresult_message = _(u"There is no task for this content.")
    __table__ = FacetedTasksTable

    def update(self):
        self.table = self.__table__(self.context, self.request)
        catalog = api.portal.get_tool('portal_catalog')
        container_path = '/'.join(self.context.getPhysicalPath())
        brains = catalog.searchResults(
            object_provides=ITask.__identifier__,
            path={'query': container_path},
            sort_on='getObjPositionInParent'
        )
        self.table.results = [b.getObject() for b in brains]
        self.table.update()


class TasksListViewlet(TasksListBase):
    """
    Viewlet displaying tasks list for current task container object.
    """
    implements(IViewlet)

    label = _(u"Tasks list")

    def __init__(self, context, request, view, manager=None):
        super(TasksListBase, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager


class TasksListView(TasksListBase):
    """
    View displaying tasks list for current task container object.
    """
