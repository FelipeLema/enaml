#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .wpf_layout_component import WPFLayoutComponent

from ...components.control import AbstractTkControl


class WPFControl(WPFLayoutComponent, AbstractTkControl):
    pass

