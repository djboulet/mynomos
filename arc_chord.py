"""
    arc_chord.py

    Nomogram to demonstrate relationship between circle arc lengths and chords

    Copyright (C) 2018-2019  Daniel Boulet

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *
from math import *


chord = {
    'u_min': 6.0,
    'u_max': 12.0,
    'function': lambda u: (u**2)/4.0,
    'title': r'chord ($u$)',
    'tick_levels': 3,
    'tick_text_levels': 2,
}

radius = {
    'u_min': 7.0,
    'u_max': 15.0,
    'function': lambda u: -2*u,
    'title': r'radius ($v$)',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'tick_side': 'left',
}

drop = {
    'u_min': 0.5,
    'u_max': 2.0,
    'function_3': lambda u: u,
    'function_4': lambda u: u**2,
    'title': r'drop ($w$)',
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',
    'tick_side': 'left',
    'title_draw_center': True,
}


block_1_params = {
    'block_type': 'type_10',
    'width': 10.0,
    'height': 10.0,
    'f1_params': chord,
    'f2_params': radius,
    'f3_params': drop,
     'isopleth_values':[[10.5,'x',1.25]]
}


main_params = {
    'filename': 'arc_chord.pdf',
    # 'paper_height': 10.0,
    # 'paper_width': 10.0,
    'block_params': [block_1_params,],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'$u_1=u_2\times u_3$'
}
Nomographer(main_params)
