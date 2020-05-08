"""
    romer.py

    Nomogram to layout a custom romer for map reading. Scale values
    according to 'actual_grid_size' (the size of the grid represented on
    the map e.g. 1km) and 'printed_grid_size' (size of the grid
    printed on the map e.g. 8.7cm).  The pynomo script will generate a
    romer to scale the map grid and actual grid.

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

from pynomo.nomographer import Nomographer
import sys
import os
import numpy as np
import pyx

pyx.text.set(mode="latex")


def deg2rad(deg):
    return np.pi * deg / 180.0


# actual grid size in meters
# actual_grid_size = float(os.environ['ACTUAL_GRID_SIZE'])
actual_grid_size = 1000.0

# printed grid size in centimeters
# printed_grid_size = float(os.environ['PRINTED_GRID_SIZE'])
printed_grid_size = 7.5

map_scale = actual_grid_size / (printed_grid_size / 100.0)
romer_title = "Map Romer \par Scale: " + \
    "{0:.4f}".format(round(map_scale, 2)) + " to 1"

n_params = {
    'u_min': 0.0,
    'u_max': actual_grid_size,
    'function_x': lambda u: u * np.cos(deg2rad(45.0)),
    'function_y': lambda u: u * np.sin(deg2rad(45.0)),
    'tick_levels': 3,
    'tick_text_levels': 0,
    'tick_side': 'left',
    'title': r'Northings',
    'title_draw_center': True,
    'title_distance_center': -1.5,
    'extra_params': [{
        'u_min': actual_grid_size/10.0 * 1.5,
        'u_max': actual_grid_size,
        'tick_text_levels': 2,
    }],
    'text_distance_0': 0.65,
    'text_distance_1': 0.4,
    'text_size_0': pyx.text.size.scriptsize,
    'text_size_1': pyx.text.size.tiny,
    'grid_length_0': 0.5,

}

e_params = {
    'u_min': 0.0,
    'u_max': actual_grid_size,
    'function_x': lambda u: u * np.cos(deg2rad(135.0)),
    'function_y': lambda u: u * np.sin(deg2rad(135.0)),
    'tick_levels': 3,
    'tick_text_levels': 0,
    'title': r'Eastings',
    'title_draw_center': True,
    'title_distance_center': 1.5,
    'extra_params': [{
        'u_min': actual_grid_size/10.0 * 1.5,
        'u_max': actual_grid_size,
        'tick_text_levels': 2,
    }],
    'text_distance_0': 0.65,
    'text_distance_1': 0.4,
    'grid_length_0': 0.5,
    'text_size_0': pyx.text.size.scriptsize,
    'text_size_1': pyx.text.size.tiny,
}

block_params_n = {
    'block_type': 'type_8',
    'f_params': n_params,
    # 'width': printed_grid_size * 100.0 * np.sqrt(2.0),
    # 'height': printed_grid_size * 100.0 * np.sqrt(2.0),
    'width': 5.0,
    'height': printed_grid_size / np.sqrt(2.0),
}

block_params_e = {
    'block_type': 'type_8',
    'f_params': e_params,
    'width': 5.0,
    'height': printed_grid_size / np.sqrt(2.0),
}

main_params = {
    'filename': 'romer.pdf',
    # 'paper_height': printed_grid_size / np.sqrt(2.0),
    # 'paper_width': printed_grid_size * 2.0 / np.sqrt(2.0),
    'paper_height': printed_grid_size,
    'paper_width': printed_grid_size,
    'block_params': [block_params_n, block_params_e],
    'title_str': romer_title,
    'title_x': 3.0,
    'title_y': 6.5,
    'transformations': [('rotate', 44.9), ('scale paper',)],
    # 'make_grid': True,
    'draw_lines': True,
    'line_params': [
        {
            'coords': [
                [0, 1.5, 0, printed_grid_size + 0.5], [-0.5, printed_grid_size,
                                                       printed_grid_size - 1.5, printed_grid_size],
            ],
            'line_style': [pyx.color.cmyk.Black, pyx.style.linewidth.thin, pyx.style.linestyle.dashed],
        },
    ],
    'extra_texts': [
        {
            'x': 0.0,
            'y': -1.0,
            'text': r'\copyright Daniel Boulet  2020',
            'width': 10.0,
        },
    ],

}

Nomographer(main_params)
