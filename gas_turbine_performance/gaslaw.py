"""
    ex_type4_nomo_1.py

    Simple nomogram of type 4: F1/F2=F3/F4

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

pressure={
        'u_min':100,
        'u_max':500,
        'function':lambda u:u,
        'title':r'$P$',
        'scale_type':'linear smart',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'left',
                }
density={
        'u_min':0.1,
        'u_max':0.5,
        'function':lambda u:u,
        'scale_type':'linear smart',
        'title':r'$density$',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'right',
                }
temp={
        'u_min':500,
        'u_max':2500,
        'function':lambda u:u+460,
        'scale_type':'linear smart',
        'title':r'$temp$',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'right',
        'title_draw_center':True,
        'title_opposite_tick':False,
                }
gasconstant={
        'u_min':0.36,
        'u_max':0.38,
        'function':lambda u:1.0/u,
        'title':r'$R$',
        'scale_type':'manual point',
        'manual_axis_data':{
            0.37:''
        },
        'tick_levels':3,
        'tick_text_levels':1,
        # 'tick_side':'left',
        'title_draw_center':True,
        'title_opposite_tick':False,
                }

block_1_params={
                'block_type':'type_4',
                'f1_params':pressure,
                'f2_params':density,
                'f3_params':temp,
                'f4_params':gasconstant,
                # 'isopleth_values':[[7,6,2,'x']],
                             }

main_params={
              'filename':'gaslaw.pdf',
              'paper_height':10.0,
              'paper_width':10.0,
              'block_params':[block_1_params],
              'transformations':[('rotate',0.01),('scale paper',)],
              'title_str':r'$u_1/u_2=u_3/u_4$',
              'title_y':8.0,
              }
Nomographer(main_params)
