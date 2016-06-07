# -*- coding: utf-8 -*-

from collective.eeafaceted.z3ctable.columns import BaseColumn

from collective.task.adapters import TaskAdapter
from collective.task.browser.table import TasksTable


class FacetedTasksTable(TasksTable):

    """Table that displays tasks info."""


class TitleColumn(BaseColumn):

    """Column that displays title."""

    def renderCell(self, item):
        adaptedTask = TaskAdapter(item.getObject())
        title = adaptedTask.get_full_tree_title().decode('utf-8')
        cell = u'<a href="{0}">{1}</a>'.format(item.getURL(), title)
        return cell
