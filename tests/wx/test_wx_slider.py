#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import wx

from .. import slider
from . import send_wx_event, process_wx_events, send_wx_mouse_event
from enaml.toolkit import wx_toolkit
from enaml.enums import TickPosition, Orientation
from enaml.widgets.wx.wx_slider import SLIDER_MAX

# A map from wxSlider constants to Enaml TickPosition values.
TICK_POS_MAP = {wx.SL_BOTTOM: TickPosition.DEFAULT,
                wx.SL_LEFT: TickPosition.LEFT ,
                wx.SL_RIGHT: TickPosition.RIGHT,
                wx.SL_TOP: TickPosition.TOP,
                wx.SL_BOTTOM: TickPosition.BOTTOM,
                wx.SL_BOTH: TickPosition.BOTH,
                wx.SL_TICKS: 'Ticks'}

# A map from Wx constants to Enaml enums for horizontal or vertical orientation.
ORIENTATION_MAP = {wx.SL_HORIZONTAL: Orientation.HORIZONTAL,
                   wx.SL_VERTICAL: Orientation.VERTICAL}

# Map event actions to WX constants
EVENT_MAP = {slider.TestEvents.PRESSED: wx.EVT_LEFT_DOWN,
             slider.TestEvents.RELEASED: wx.EVT_LEFT_UP,
             slider.TestEvents.HOME: wx.EVT_SCROLL_BOTTOM,
             slider.TestEvents.END: wx.EVT_SCROLL_TOP,
             slider.TestEvents.STEP_UP: wx.EVT_SCROLL_LINEUP,
             slider.TestEvents.STEP_DOWN: wx.EVT_SCROLL_LINEDOWN,
             slider.TestEvents.PAGE_UP: wx.EVT_SCROLL_PAGEUP,
             slider.TestEvents.PAGE_DOWN: wx.EVT_SCROLL_PAGEDOWN}

class TestWXSlider(slider.TestSlider):
    """ QtLabel tests. """

    toolkit = wx_toolkit()

    def setUp(self):
        super(TestWXSlider, self).setUp()
        self.widget.SetSize(wx.Size(200,20))

    def get_value(self, widget):
        """ Get a slider's position.

        """
        value = float(widget.GetValue())
        return self.component.from_slider(value / SLIDER_MAX)

    def get_tick_interval(self, widget):
        """ Get the Slider's tick_interval value.

        """
        value = float(widget.GetTickFreq())
        return value / SLIDER_MAX

    def get_tick_position(self, widget):
        """ Get the Slider's tick position style.

        Assertion errors are raised when it is not posible to estimate the
        tick positiosn.

        """
        style = widget.GetWindowStyle()
        flags = []
        for flag in TICK_POS_MAP.keys():
            if flag & style:
                flags.append(TICK_POS_MAP[flag])

        number_of_flags = len(flags)
        if number_of_flags == 0:
            return TickPosition.NO_TICKS
        elif number_of_flags == 1:
            self.fail('The tick position style is expected to have a least'
                      ' two style bits set when the ticks are visible')
        elif number_of_flags == 2:
            self.assertIn('Ticks', flags, 'When the ticks are visible'
                      ' the position style is expected to have the wx.SL_TICKS'
                      ' bits set')
            flags.pop(flags.index('Ticks'))
        else:
            self.fail('More than two tick position style flags are set')

        return flags[0]

    def get_orientation(self, widget):
        """ Get the Slider's orientation.

        """
        style = widget.GetWindowStyle()
        flags = []
        for flag in ORIENTATION_MAP.keys():
            if flag & style:
                flags.append(ORIENTATION_MAP[flag])

        number_of_flags = len(flags)

        if number_of_flags == 0:
            self.fail('Orientation should be always set in the widget')
        elif number_of_flags > 1:
            self.fail('More than one orientation style flags are set')

        return flags[0]

    def get_single_step(self, widget):
        """ Get the Slider's single step value.

        """
        value = widget.GetLineSize() / widget.GetTickFreq()
        return value

    def get_page_step(self, widget):
        """ Get the Slider's page step value.

        """
        value = widget.GetPageSize() / widget.GetTickFreq()
        return value

    def get_tracking(self, widget):
        """ Get the Slider's tracking status.

        """
        self.skipTest('Getting the tracking status from the wxSlider is'
                      'not implemented yet')

    def send_event(self, widget, event):
        """ Send an event to the Slider programmatically.

        Arguments
        ---------
        widget :
            The widget to sent the event to.

        event :
            The desired event to be proccessed.

        """
        event_type = EVENT_MAP[event]
        if  event_type in (wx.EVT_LEFT_DOWN, wx.EVT_LEFT_UP):
            position = wx.Point(100,10)
            send_wx_mouse_event(widget, event_type, position=position)
        else:
            value = widget.GetValue()
            tick_interval = widget.GetTickFreq()
            if event_type == wx.EVT_SCROLL_BOTTOM:
                value = widget.GetMin()
            elif event_type == wx.EVT_SCROLL_TOP:
                value = widget.GetMax()
            elif event_type == wx.EVT_SCROLL_LINEUP:
                value += widget.GetLineSize()
            elif event_type == wx.EVT_SCROLL_LINEDOWN:
                value -= widget.GetLineSize()
            elif event_type == wx.EVT_SCROLL_PAGEUP:
                value += widget.GetPageSize()
            elif event_type == wx.EVT_SCROLL_PAGEDOWN:
                value -= widget.GetPageSize()

            widget.SetValue(value)
            event = wx.ScrollEvent(event_type.typeId, widget.GetId())
            widget.GetEventHandler().ProcessEvent(event)

        #process_wx_events(self.view.toolkit.app)

