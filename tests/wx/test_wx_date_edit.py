#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import wx

from enaml.widgets.wx.wx_date_edit import to_wx_date, from_wx_date
from enaml.toolkit import wx_toolkit

from .. import date_edit


class TestWXDateEdit(date_edit.TestDateEdit):
    """ WXDateEdit tests. """

    toolkit = wx_toolkit()

    def test_set_format(self):
        """ Test setting the output format

        """
        self.skipTest('Seetting the display format is not supported in'
                      ' native wxWidgets')

    def get_date(self, widget):
        """  Get the toolkits widget's active date.

        """
        date = widget.GetValue()
        return from_wx_date(date)

    def get_minimum_date(self, widget):
        """  Get the toolkits widget's maximum date attribute.

        """
        date = widget.GetLowerLimit()
        return from_wx_date(date)

    def get_maximum_date(self, widget):
        """ Get the toolkits widget's minimum date attribute.

        """
        date = widget.GetUpperLimit()
        return from_wx_date(date)

    def change_date(self, widget, date):
        """ Simulate a change date action at the toolkit widget.

        """
        wx_date = to_wx_date(date)
        widget.SetValue(wx_date)
        event_type = wx.EVT_DATE_CHANGED
        event = wx.DateEvent(widget, wx_date, event_type.typeId)
        widget.GetEventHandler().ProcessEvent(event)

    def get_date_as_string(self, widget):
        """  Get the toolkits widget's active date as a string.

        """
        self.skipTest("The retrival of the date as string is not"
                      "implemented yet for the wx_toolkit")
