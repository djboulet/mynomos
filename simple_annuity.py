"""
    simple_annuity.py

    ---
    Nomogram to calculate how long a lump sum will last based on regular
    monthly withdrawals. 

    Copyright (C) 2018-2020  Daniel Boulet

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
import numpy as np

# allows use of latex commands in PyX such as \frac{a}{b} and \par
pyx.text.set(mode="latex")


def annuity(x, u):
    return np.log(
        np.log(-x/(u/1200.0-x))
        /
        np.log(u/1200.0+1)
    )


block_1_params = {
    'width': 10.0,
    'height': 5.0,
    'block_type': 'type_5',
    'u_func': lambda u: np.log(u*12.0),
    'v_func': annuity,
    'u_values': [10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 20.0, 25.0, 30.0, 40.0, 50.0, 60.0],
    'v_values': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0],
    'wd_tag': 'A',
    'u_title': r'\large Years',
    'v_title': r'\large Yield = ',
    'u_text_format': r"$%3.0f$ ",
    'v_text_format': r"$%3.0f$ \%% ",
    'vertical_guide_nr': 10,
    'horizontal_guides': False,
    'v_title_draw_center': True,
    'isopleth_values': [['x', 6, 'x'],['x',8.5,'x']], #['years','yield','ratio']
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
    # 'title_draw_center': True
}
N_params_2 = {
    'u_min': 100.0,
    'u_max': 1000.0,
    'function': lambda u: u,
    'title': r'\large Lump sum (in thousands)',
    'tag': 'none',
    'tick_side': 'left',
    'tick_levels': 4,
    'tick_text_levels': 2,
    'title_draw_center': True,
    'grid_length_1': 0.5,
    'grid_length_2': 0.35,
    'grid_length_3': 0.25,
    'text_distance_1': 0.55,
    'text_format': r"$\$%3.0f$ ",
    'scale_type': 'linear smart',
}
N_params_1 = {
    'u_min': 1000.0,
    'u_max': 5000.0,
    'function': lambda u: u/1000.0,
    'title': r'\large Monthly withdrawal',
    'tag': 'none',
    'scale_type': 'linear smart',
    'tick_side': 'right',
    'tick_levels': 4,
    'tick_text_levels': 2,
    'title_draw_center': True,
    'grid_length_1': 0.5,
    'grid_length_2': 0.35,
    'grid_length_3': 0.25,
    'text_distance_1': 0.55,
    'text_format': r"$\$%3.0f$ ",

}

block_2_params = {
    'block_type': 'type_2',
    'width': 10.0,
    'height': 20.0,
    'f1_params': N_params_1,    # withdrawal
    'f2_params': N_params_2,    # lump sum (in thousands)
    'f3_params': N_params_3,    # curve
    'isopleth_values': [[3000, 500, 'x'], [3198.25, 400, 'x']]
}

main_params = {
    'filename': 'simple_annuity.pdf',
    'paper_height': 2.54*11,
    'paper_width': 2.54*8.5,
    # 'make_grid': True,
    'block_params': [block_1_params, block_2_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r'\textbf{\huge Annuity Calculator}',
    'title_x': 17,
    'title_y': 29,
    'title_box_width': 8,
    'extra_texts': [
        {
            'text': r'\copyright Daniel Boulet (2018-2020)',
            'x': 16.5,
            'y': -2.5,
        },
        {
            'text': r'\noindent \textbf{How long will your money last?} \
                You can withdraw \$3000 per month from your \$500,000 \
                    initial investment for 30 years if your investments earn 6\% interest.',
            'x': 1,
            'y': 4,
            'width': 8,
        },
        {
            'text': r'\noindent \textbf{How much savings do I need?} \
                You will need an initial investment of \$400,000 earning 8.5\% \
                    if you want to withdraw \$3200 per month for 25 years.',
            'x': 13,
            'y': 10,
            'width': 8,
        },
    ],

}
Nomographer(main_params)
