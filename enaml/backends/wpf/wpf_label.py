#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import warnings

from wpyf.label import Label as _WPyFLabel
from .wpf_control import WPFControl

from ...components.label import AbstractTkLabel


class WPFLabel(WPFControl, AbstractTkLabel):
    """ A WPF implementation of Label.

    """
    #--------------------------------------------------------------------------
    # Setup methods
    #--------------------------------------------------------------------------
    def create(self, parent):
        """ Creates the underlying WPF Label control.

        """
        self.widget = _WPyFLabel()
        parent.Add(self.widget, 0, 0)

    def initialize(self):
        """ Initializes the attributes on the underlying control.

        """
        super(WPFLabel, self).initialize()
        shell = self.shell_obj
        self.set_label(shell.text)
        self.set_word_wrap(shell.word_wrap)

    #--------------------------------------------------------------------------
    # Implementation
    #--------------------------------------------------------------------------
    def shell_text_changed(self, text):
        """ The change handler for the 'text' attribute.

        """
        self.set_label(text)

    def shell_word_wrap_changed(self, word_wrap):
        """ The change handler for the 'word_wrap' attribute.

        """
        self.set_word_wrap(word_wrap)

    def set_label(self, label):
        """ Sets the label on the underlying control.

        """
        shell = self.shell_obj
        self.widget.Content = unicode(shell.text)

    def set_word_wrap(self, wrap):
        """ Sets the word wrapping on the underlying widget.

        """
        warnings.warn("Option is not yet supported in the wpf backend")

