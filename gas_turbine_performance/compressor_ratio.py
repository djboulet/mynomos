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

T1_params={
        'u_min':-40.0,
        'u_max':120.0,
        'function':lambda u:(u)+460,
        'scale_type':'linear smart',
        'title':r'Inlet\ Temperature',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'left',
                }
Nc_params={
        'u_min':0.5,
        'u_max':1.0,
        'function':lambda u:u,
        'title':r'Compressor eff',
        'scale_type':'linear smart',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'right',
                }
DeltaT_params={
        'u_min':300.0,
        'u_max':700.0,
        'function':lambda u:u,
        'title':r'Temp change',
        'scale_type':'linear smart',
        'tick_levels':3,
        'tick_text_levels':1,
        'tick_side':'right',
        'title_draw_center':True,
        'title_opposite_tick':False,
                }
Compratio_params={
        'u_min':5.0,
        'u_max':10.0,
        'function':lambda u:(u**(2.0/7.0))-1.0,
        'title':r'Compression ratio',
        'tick_levels':3,
        'scale_type':'linear smart',
        'tick_text_levels':1,
        'tick_side':'left',
        'title_draw_center':True,
        'title_opposite_tick':False,
                }

block_1_params={
                'block_type':'type_4',
                'f3_params':T1_params,
                'f4_params':Nc_params,
                'f1_params':DeltaT_params,
                'f2_params':Compratio_params,
                # 'isopleth_values':[[70,.82,'x',8.468]]
                             }

main_params={
              'filename':'compressor_ratio.pdf',
              'paper_height':20,
              'paper_width':20,
              'block_params':[block_1_params],
              'transformations':[('rotate',0.01),('scale paper',)],
            #   'title_str':r'$u_1/u_2=u_3/u_4$',
            #   'title_y':8.0,
              }
Nomographer(main_params)
