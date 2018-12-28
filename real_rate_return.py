"""
    real_rate_return.py

    Simple nomogram to calculate real rate of return based
    on interest rate and rate of inflation.  Real rate of return
    (rrr) = (1+interest)/(1+inflation)
    
    Copyright (C) 2018      Daniel Boulet

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

interest = {
    'u_min': 0.0,
    'u_max': 10.0,
    'function': lambda u: u/100.0+1.0,
    'title_draw_center':True,
    'title': r'Return on investment ($r\%$)',
    'scale_type': 'linear smart',
    'tick_side': 'left',
    'tick_levels': 3,
    'tick_text_levels': 1,
}

rrr = {
    'u_min': -5.0,
    'u_max': 10.0,
    'function': lambda u: u/100.0+1.0,
    'title_draw_center':True,
    'title': r'Real rate of return ($q\%$)',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'scale_type': 'linear smart',
}

inflation = {
    'u_min': 0.0,
    'u_max': 5.0,
    'title_y_shift':0.5,
    'function': lambda u: u/100.0+1.0,
    'title': r'Rate of inflation ($i\%$)',
    'scale_type': 'linear smart',
    'tick_levels': 3,
    'tick_text_levels': 1,
}


block_1_params = {
    'block_type': 'type_2',
    #  'width':10.0,
    #  'height':10.0,
    'f1_params': interest,
    'f3_params': rrr,
    'f2_params': inflation,
    'isopleth_values': [[5, 5, 'x'], [7.5, 2.5, 'x']],
}

main_params = {
    'filename': 'real_rate_return.pdf',
    #   'paper_height':10.0,
    #   'paper_width':10.0,
    'block_params': [block_1_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    # 'title_x': 17,
    'title_y': 21,
    'title_box_width': 5,
    'title_str': r'\Large Real rate of return calculator:   $(1+r)/(1+i)=(1+q)$'
}
Nomographer(main_params)
