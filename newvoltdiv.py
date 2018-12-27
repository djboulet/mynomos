"""
    ex_type9_nomo_1.py

    Simple nomogram of type 9: determinant

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


def limit_u(u):
    u1 = u
    if not u1 > 0.0:
        u1 = 0.0001
    return u1


def limit_v(v):
    v1 = v
    if not v1 > 0.0:
        v1 = 0.0001
    return v1


"""
resistance divider
"""

u1_params = {
    'u_min': 1.0,
    'u_max': 10.0,
    'g': lambda u: 1,
    'f': lambda u: u,
    'h': lambda u: 1,
    'scale_type': 'linear smart',
    # 'u_start': 4.0,
    # 'u_stop': 6.0,
    # 'v_start': 4.0,
    # 'v_stop': 6.0,
    'grid': False,
    'tick_side': 'left',
    # 'text_prefix_u': r'$R_a$',
    # 'text_prefix_v': r'$R_b$',
    'title': r'$u_1$',
}


u2_params = {
    'tag': 'ratio',
    'u_min': 0.1,
    'u_max': 0.9,
    'g': lambda u: u,
    'f': lambda u: 0,
    'h': lambda u: 1.0,
    'title': r'$u_2$',
    'scale_type': 'linear smart',
    'tick_levels': 3,

    'tick_text_levels': 2,
    'grid': False,

}


u3_params = {
    'u_min': 1.0,  # for alignment
    'u_max': 10.0,  # for alignment
    'scale_type': 'linear smart',
    'g': lambda u: 0,
    'f': lambda u: -u,
    'h': lambda u: 1,
    'grid': False,
    'title': r'$u_3$',
}


block1_params = {
    # 'width': 20,
    'block_type': 'type_9',
    'f1_params': u1_params,
    'f2_params': u2_params,
    'f3_params': u3_params,
    'transform_ini': False,
    #  'isopleth_values':[[7,[0.75,0.5],'x']]
}

"""
voltage ratios
"""

v1_params = {
    'function': lambda u: (u),
    # 'function': lambda u: -log(u),
    'u_min': 1.0,  # for alignment
    'u_max': 10.0,  # for alignment
    'scale_type': 'linear smart',
    'title': r'$v_1$',
}

v3_params = {
    'tag': 'ratio',
    'u_min': 0.1,
    'u_max': 0.9,
    'function': lambda u: (u),
    # 'function': lambda u: -log(u),
    'title': r'$v_3$',
    'scale_type': 'linear smart',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'tick_side': 'left',

}

v2_params = {
    'u_min': 10.0,
    'u_max': 30.0,
    'function': lambda u: (u),
    # 'function': lambda u: log(u),
    'scale_type': 'linear smart',
    'title': r'$v_2$',

}


block2_params = {
    # 'width': 40,
    'block_type': 'type_2',
    'f1_params': v1_params,
    'f2_params': v2_params,
    'f3_params': v3_params,
    'mirror_y':True,
    #  'isopleth_values':[[7,[0.75,0.5],'x']]
}

"""
main parameters
"""

main_params = {
    'filename': 'newvoltdiv.pdf',
    'block_params': [block1_params, block2_params],
    # 'block_params': [ block2_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
}
Nomographer(main_params)
