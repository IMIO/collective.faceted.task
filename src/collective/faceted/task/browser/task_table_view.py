# -*- coding: utf-8 -*-

from collective.eeafaceted.z3ctable.browser.views import FacetedTableView

from collective.faceted.task.interfaces import IFacetedTasksTable

from zope.interface import implements


class FacetedTaskTableView(FacetedTableView):
    """
    """

    implements(IFacetedTasksTable)

    def _getViewFields(self):
        """Returns fields we want to show in the table."""
        col_names = [
            u'TitleColumn',
            u'assigned_user_column',
            u'status',
            u'due_date',
        ]
        return col_names
