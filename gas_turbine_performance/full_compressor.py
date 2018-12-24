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

T1_params = {
    'u_min': -40.0,
    'u_max': 120.0,
    'function': lambda u: (u)+460,
    'scale_type': 'linear smart',
    'title': r'Inlet\ Temperature',
    'tick_levels': 3,
    'tick_text_levels': 1,
    'tick_side': 'left',
}
Nc_params = {
    'u_min': 0.5,
    'u_max': 1.0,
    'function': lambda u: u,
    'title': r'Compressor eff',
    'scale_type': 'linear smart',
    'tick_levels': 3,
    'tick_text_levels': 1,
    'tick_side': 'right',
}
DeltaT_params = {
    'u_min': 300.0,
    'u_max': 700.0,
    'function': lambda u: u,
    'title': r'Temp change',
    'scale_type': 'linear smart',
    'tick_levels': 3,
    'tick_text_levels': 1,
    'tick_side': 'right',
    'title_draw_center': True,
    'title_opposite_tick': False,
}
Compratio_params = {
    'tag': 'compration',
    'u_min': 5.0,
    'u_max': 10.0,
    'function': lambda u: (u**(2.0/7.0))-1.0,
    'title': r'Compression ratio',
    'tick_levels': 3,
    'scale_type': 'linear smart',
    'tick_text_levels': 1,
    'tick_side': 'left',
    'title_draw_center': True,
    'title_opposite_tick': False,
    # 'align_func':lambda u:(u+1)**3.5,
    # 'align_func':lambda u:(u**(2.0/7.0))-1.0,


}


block_1_params = {
    'block_type': 'type_4',
    'f1_params': DeltaT_params,
    'f2_params': Compratio_params,
    'f3_params': T1_params,
    'f4_params': Nc_params,
    
    # 'isopleth_values':[[70,.82,'x',8.468]]
}


gauge = {
    'u_min': 100.0,
    'u_max': 120.0,
    'function': lambda u: u,
    'title': r'$u$',
    'tick_levels': 3,
    'scale_type':'linear smart',
    'tick_text_levels': 1,
}

ratio = {
    'tag': 'atmosration',
    'u_min': 5.0,
    'u_max': 10.0,
    'function': lambda u: -u,
    'title': r'$v$',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'tick_side': 'left',
}

atmos = {
    'u_min': 10,
    'u_max': 20,
    'function_3': lambda u: u,
    'function_4': lambda u: u,
    'title': r'$w$',
    'tick_levels': 3,
    'tick_text_levels': 1,
    'scale_type': 'linear smart',
    'title_draw_center': True,
}

block_2_params = {
    'block_type': 'type_10',
    # 'height':20,
    # 'width':20,
    'f1_params': gauge,
    'f2_params': ratio,
    'f3_params': atmos,
    #  'isopleth_values':[[110,'x',14.73]],
    'mirror_x': True,
}

leftLadder = {
    'tag': 'compration',
    'u_min': 5.0,
    'u_max': 10.0,
    'tick_levels': 3,
    'tick_text_levels': 1,
    'tick_side':'left',
    'line_type': 'linear smart',
    'function': lambda u: (u**(2.0/7.0))-1.0,
    # 'function': lambda u: u,

}

rightLadder = {
    'tag': 'atmosration',
    'line_type': 'linear smart',
    'tick_levels': 3,
    'tick_text_levels': 1,
    'u_min': 5.0,
    'grid_length_0':0.2,
    'u_max': 10.0,
    'function': lambda u: u,
}

ladder = {
    'block_type': 'type_6',
    # 'height':20,
    # 'width':40,
    'f1_params': leftLadder,
    'tick_levels':3,
    'tick_text_levels':1,
    'f2_params': rightLadder,
    'mirror_x':True,
}

main_params = {
    'filename': 'full_compressor.pdf',
    'paper_height': 8.5*2.54,
    'paper_width': 11.0*2.54,
    'block_params': [block_1_params,ladder,block_2_params],
    'transformations': [('rotate', 0.01), ('scale paper',),],
    #   'title_str':r'$u_1/u_2=u_3/u_4$',
    #   'title_y':8.0,
}
Nomographer(main_params)
