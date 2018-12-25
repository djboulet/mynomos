"""
    ex_compound_nomo_2.py

    Compound nomograph: q = u**v+w

    Copyright (C) 2007-2009  Leif Roschier

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

# N
c_params = {
    #height
    # scale minimum and maximum values
    'u_min': 5,
    'u_max': 30,
    # function to convert scale to "real world" value
    'function': lambda u: u*u,
    # cosmetic stuff
    'title': r'$c$',
    'tick_levels': 1,
    'tick_text_levels': 1,
    'tick_side': 'right',
    'scale_type': 'linear',
}

b_params = {
    # scale minimum and maximum values
    'u_min': 4,
    'u_max': 20,
    # function to convert scale to "real world" value
    'function': lambda u: -u*u,
    # cosmetic stuff
    'title': r'$b$',
    'tick_levels': 1,
    'tick_text_levels': 1,
    'tick_side': 'right',
    'scale_type': 'linear',
}

a_params = {
    # scale minimum and maximum values
    'u_min': 3.0,
    'u_max': 20.0,
    # function to convert scale to "real world" value
    'function': lambda u: -u*u,
    # cosmetic stuff
    'title': r'$a$',
    'tick_levels': 1,
    'tick_text_levels': 1,
    'tick_side': 'left',
    'scale_type': 'linear',
}

block_params_1 = {
    # block type
    'block_type': 'type_1',
    # block dimensions
    'width': 10.0,
    'height': 10.0,
    # block parameters
    'f1_params': a_params,
    'f2_params': b_params,
    'f3_params': c_params,
    # isopleth(s)
    # 'isopleth_values': [[2.5, 'x',0.35]]
}

main_params = {
    'filename': 'pythagorian.pdf',
    'paper_height': 15.0,
    'paper_width': 15.0,
    'block_params': [block_params_1],
    'transformations': [('rotate', 0.0), ('scale paper',)],
}
Nomographer(main_params)
