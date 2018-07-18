# -*- coding: utf-8 -*-

"""
ipywidgets_widget_list

https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html
"""

import ipywidgets as widgets

widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
