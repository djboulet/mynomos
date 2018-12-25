"""
    ex_type10_nomo_1.py

    Simple nomogram of type 7: F1(u)+F2(v)*F3(w)+F4(w)=0
    This example plots: u+v*w+w=0

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

gauge={
        'u_min':100.0,
        'u_max':120.0,
        'function':lambda u:-u,
        'title':r'$u$',
        'tick_levels':3,
        'tick_text_levels':2,
                }

ratio={
        'u_min':5.0,
        'u_max':10.0,
        'function':lambda u:u,
        'title':r'$v$',
        'tick_levels':3,
        'tick_text_levels':2,
        'tick_side':'left',
                }

atmos={
        'u_min':10,
        'u_max':20,
        'function_3':lambda u:u,
        'function_4':lambda u:u,
        'title':r'$w$',
        'tick_levels':4,
        'tick_text_levels':3,
        'scale_type':'linear smart',
        'title_draw_center':True,
                }

block_1_params={
             'block_type':'type_10',
             'width':10.0,
             'height':10.0,
             'f1_params':gauge,
             'f2_params':ratio,
             'f3_params':atmos,
             'isopleth_values':[[110,'x',14.73]],
             'mirror_x':True,
             }

main_params={
              'filename':'atmos_ratios.pdf',
              'paper_height':20.0,
              'paper_width':20.0,
              'block_params':[block_1_params],
              'transformations':[('rotate',0.01),('scale paper',)],
              'title_str':r'$u+vw+w=0$'
              }
Nomographer(main_params)
