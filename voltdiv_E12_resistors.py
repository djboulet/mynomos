"""
    voltdiv_E12_resistors.py

    Nomogram to calculate resistor values for simple voltage divider.  This
    nomogram uses grid rather than matrix.  

    Copyright (C) 2018-2020 Daniel Boulet

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

from pynomo.nomographer import *
import sys
sys.path.insert(0, "..")
outputfile = sys.argv[0].split('.')[0]+'.pdf'

from pyx import *
pyx.text.set(text.LatexEngine)

resistors = [
    1.0,	1.2,	1.5,
    1.8,	2.2,	2.7,
    3.3,	3.9,	4.7,
    5.6,	6.8,	8.2,
]

# Type 5 contour


def f1(x, u):
    return u*(1-x)/x


block_1_params = {
    'width': 12.0,
    'height': 20.0,
    'block_type': 'type_5',
    'u_func': lambda u: u,
    # 'v_func': lambda x, v: x + v,
    'v_func': f1,
    'u_values': resistors,
    'v_values': resistors,

    'v_axis_color': pyx.color.cmyk.Red,
    'u_axis_color': pyx.color.cmyk.Red,
    'wd_tag': 'A',
    'u_title': r'$R_a$',
    'v_title': r'$R_b$',
    'u_text_format': r"$%3.1f$ ",
    'v_text_format': r"$%3.1f$ ",
    # 'wd_tick_levels': 4,
    # 'wd_tick_text_levels': 2,
    'wd_tick_side': 'right',
    'wd_axis_color': pyx.color.cmyk.Gray,
    'isopleth_values': [
        [4.7, 'x', 'x'],
        [2.7, 'x', 'x'],
        [1.2, 'x', 'x'],
        [5.1, 'x', 'x'],
    ],
    'vertical_guide_nr':10
}

# this is non-obvious trick to find bottom edge coordinates of the grid in order
# to align it with N nomogram
block1_dummy = Nomo_Block_Type_5(mirror_x=False)
block1_dummy.define_block(block_1_params)
block1_dummy.set_block()

# Let's define the N-nomogram
N_params_3 = {
    'u_min': block1_dummy.grid_box.params_wd['u_min'],
    'u_max': block1_dummy.grid_box.params_wd['u_max'],
    'function': lambda u: u,
    'title': '',
    'tag': 'A',
    'tick_side': 'right',
    'tick_levels': 2,
    'tick_text_levels': 2,
    'reference': False,
    'tick_levels': 0,
    'tick_text_levels': 0,
    'title_draw_center': True
}
N_params_2 = {
    'u_min': 6.0,
    'u_max': 24.0,
    'function': lambda u: u,
    'title': r'$V_{in}$',
    'tag': 'none',
    'tick_side': 'left',
    'tick_levels': 4,
    'tick_text_levels': 3,
    'title_draw_center': True,
    # 'text_format':r"$%3.0f$ ",
    'scale_type': 'linear smart',
}
N_params_1 = {
    'u_min': 1.0,
    'u_max': 10.0,
    'function': lambda u: u,
    'title': r'$V_{out}$',
    'tag': 'none',
    'scale_type': 'linear smart',
    'tick_side': 'right',
    'tick_levels': 3,
    'tick_text_levels': 3,
    'title_draw_center': True
}

block_2_params = {
    'block_type': 'type_2',
    #  'width':10.0,
    #  'height':40.0,
    'f1_params': N_params_1,
    'f2_params': N_params_2,
    'f3_params': N_params_3,
    'isopleth_values': [
        # Vout, Vin, ratio
        [3.3, 9.0, 'x'],
        [3.3, 6.0, 'x'],
        [5.0, 9.0, 'x'],
        [5.0, 12.0, 'x'],
    ]
}

main_params = {
    'filename': outputfile,
    'paper_height': 8.5*2.54,
    'paper_width': 11.0*2.54,
    # 'block_params': [block_1_params],
    'block_params': [block_1_params, block_2_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'\Large Voltage Divider Nomograph \par \
        \normalsize (For E12 series values) \par \bigskip \
        \large $V_{out}=V_{in} \cdot \frac{R_b}{R_a+R_b}$ \
        \par \bigskip   \normalsize \copyright    Daniel Boulet  2018-2020',
    'title_x': 2.0,
    'title_y': 6.0,
    # 'make_grid':True,
    # 'title_box_width': 5,
    'isopleth_params': [
        {
            'color': 'blue',
            'linewidth': 'thick',
            'linestyle': 'dashed',
            'circle_size': 0.10,
            # 'transparency': 0.0,
        },
    ],
}

Nomographer(main_params)
