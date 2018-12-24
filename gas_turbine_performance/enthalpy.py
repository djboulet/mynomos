"""
    ex_type2_nomo_1.py

    Simple nomogram of type 2: F1=F2*F3

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

deltaH={
        'u_min':200,
        'u_max':300,
        'function':lambda u:u,
        'scale_type':'linear smart',
        'title':r'$dH$',
        'tick_levels':3,
        'tick_text_levels':1,
                }

spHeat={
        'u_min':0.2,
        'u_max':0.3,
        'function':lambda u:u,
        'title':r'$c_p$',
        'scale_type':'linear smart',
        'tick_levels':3,
        'tick_text_levels':2,
        'scale_type':'linear smart',
                }

deltaT={
        'u_min':500,
        'u_max':1500,
        'scale_type':'linear smart',
        'function':lambda u:u,
        'title':r'$dT$',
        'tick_levels':3,
        'tick_text_levels':1,
                }


block_1_params={
             'block_type':'type_2',
             'width':10.0,
             'height':10.0,
             'f1_params':deltaH,
             'f2_params':spHeat,
             'f3_params':deltaT,
             'isopleth_values':[[240,0.24,'x']],
             }

main_params={
              'filename':'enthalpy.pdf',
              'paper_height':10.0,
              'paper_width':10.0,
              'block_params':[block_1_params],
              'transformations':[('rotate',0.01),('scale paper',)],
              'title_str':r'$u_1=u_2\times u_3$'
              }
Nomographer(main_params)
