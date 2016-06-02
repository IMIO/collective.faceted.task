# -*- coding: utf-8 -*-

from collective.task.adapters import TaskMethodsAdapter
from collective.task.browser.table import TasksTable
from collective.task.browser.table import TitleColumn as TaskTitleColumn


class FacetedTasksTable(TasksTable):

    """Table that displays tasks info."""


class TitleColumn(TaskTitleColumn):

    """Column that displays title."""

    def renderCell(self, item):
        adaptedTask = TaskMethodsAdapter(item)
        return adaptedTask.get_full_tree_title()
