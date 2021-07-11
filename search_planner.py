"""
search_effort.py

Nomogram to calculate search effort for ground search activities.

Copyright(C) 2018-2020 Daniel Boulet

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY
without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see < http: // www.gnu.org/licenses/>.
"""
from pynomo.nomographer import Nomographer
import sys
from pyx import *
pyx.text.set(text.LatexEngine)

searchers = {
    'ID': 'searchers',
    'u_min': 3.0,
    'u_max': 8.0,
    'function': lambda u: 1.0 / u,
    'scale_type': 'linear',
    'title': r'Number of searchers',
    'title_distance_center': -1.25,
    'tick_levels': 1,
    'tick_text_levels': 1,
    'tick_side': 'left',
    'grid_length_0': 0.5,
    'text_distance_0': 0.75,
    'title_draw_center': True,
    # 'title_opposite_tick': False,
    # 'text_horizontal_align': True,
    'extra_angle': 90.0

}


hectares = {
    'ID': 'hectares',
    'u_min': 1.0,
    'u_max': 20.0,
    'function': lambda u: u*10000.0,
    # 'title': r'Search area ($Ha$)',
    'extra_titles': [
        {
            'text': r'Search \par area ($Ha$)',
            'dx': -1.5,
            'dy': 0.7
        }
    ],

    'tick_levels': 3,
    'tick_text_levels': 1,
    'tick_side': 'left',
    'grid_length_0': 0.5,
    'grid_length_1': 0.3,
    'text_distance_0': 0.8,
    'scale_type': 'linear smart'
}

distance1 = {
    'ID': 'distance1',
    'tag': 'distance',
    'scale_type': 'linear smart',
    'u_min': 0.5,
    'u_max': 5.0,
    'function': lambda u: u*1000,
    'align_function': lambda u: u * 1000,
    'extra_titles': [
        {
            'text': r'Distance \par ($km$)',
            'dx': -0.5,
            'dy': 0.65
        }
    ],
    'grid_length_0': 0.5,
    'grid_length_1': 0.3,
    'text_distance_0': 0.65,
    'tick_levels': 3,
    'tick_text_levels': 1,
    'tick_side': 'right',
}

spacing = {
    'ID': 'spacing',
    'u_min': 2.0,
    'u_max': 15.0,
    'function': lambda u: u,
    # 'scale_type': 'manual point',
    # 'manual_axis_data': {2.5: '2.5', 5.0: '5.0', 10: '10', 15: '15'},
    'title': r'Searcher spacing ($m$)',
    'title_draw_center': True,
    'title_opposite_tick': False,
    'tick_text_levels': 1,
    'tick_levels': 2,
    'grid_length_0': 0.5,
    'grid_length_1': 0.2,
    'text_distance_0': .8,
    'title_distance_center': -1.5,
    'text_horizontal_align': True,
    'extra_angle': 90.0,
    'turn_relative': True,

    # 'extra_params': [
    #     {
    #         'u_min': 2.5,
    #         'u_max': 15.0,
    #         'scale_type': 'linear',
    #         'tick_levels': 3,
    #         'tick_text_levels': 1,
    #         'tick_side': 'right',
    #     }
    # ]
}

area_block = {
    'ID': 'area_block',
    'block_type': 'type_4',
    'height': 8,
    'width':8,
    'f1_params': hectares,
    'f2_params': distance1,
    'f3_params': spacing,
    'f4_params': searchers,
    'reference_color': pyx.color.cmyk.Gray,
    'padding': .9,
    'isopleth_values': [['x', 3.0, 7.5, 6]],
}

distance2 = {
    # distance in meters (u3)
    'ID': 'distance2',
    'tag': 'distance',
    'u_min': 0.5,
    'u_max': 5.0,
    'scale_type': 'manual_point',
    'function': lambda u: u*1000,
    'tick_levels': 0,
    'tick_text_levels': 0,
    # 'title_x_shift': 1.0,
}

speed_km_h = {
    # speed in km/hr
    'ID': 'speed_in_km_per_hr',
    'tag': 'speed',
    'u_min': 1.0,
    'u_max': 5.0,
    'function': lambda u: u*1000/3600,
    'title': r'Speed ($\frac{km}{hr}$)',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'title_x_shift': 0.0,
    'title_draw_center': True,
    'title_distance_center': -1.4,
    'grid_length_0': 0.5,
    'grid_length_1': 0.3,
    'text_distance_0': 0.8,
    'text_distance_1':0.35

}


time_required = {
    # time in minutes
    'ID': 'time_required',
    'u_min': 15.0,
    'u_max': 120.0,
    'function': lambda u: u*60,
    # 'title': r'Time required ($min$)',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'title_x_shift': 1.0,
    'extra_titles': [
        {
            'text': r'Time \par required \par ($min$)',
            'dx': -0.5,
            'dy': 1.2
        }
    ],

}

distance_speed_time_block = {
    'block_type': 'type_2',
    'f1_params': distance2,
    'f2_params': speed_km_h,
    'f3_params': time_required,
    'isopleth_values': [[3.0, 'x', 90]],
    'mirror_x': True
}

speed_min_100meter = {
    # speed in minutes / 100 meters
    'ID': 'speed_sec_meter',
    'u_min': 0.72*100/60,
    'u_max': 3.6*100/60,
    'function': lambda u: u/100*60,
    'title': r'Pace ($\frac{min}{100\cdot m}$)',
    'tick_levels': 3,
    'tick_text_levels': 2,
    'title_draw_center': True,
    'scale_type': 'linear smart',
    'tick_side': 'left',
    'title_distance_center': -1.6,
    'grid_length_0': 0.5,
    'grid_length_1': 0.3,
    'text_distance_0': 0.8,
    'text_distance_1': 0.35

}


distance_speed_time_block2 = {
    'ID': 'distance_speed_time_block2',
    'block_type': 'type_2',
    'f1_params': time_required,
    'f2_params': speed_min_100meter,
    'f3_params': distance2,
    'isopleth_values': [[90, 'x', 3.0]],
    'width':10,
    'mirror_x': True,

}

main_params = {
    'filename': 'search_planner.pdf',
    'paper_height': 8,
    'paper_width': 16,
    'block_params': [area_block, distance_speed_time_block, distance_speed_time_block2],
    'transformations': [('rotate', 0.01), ('scale paper',),  ],
    'title_str': r'\Large \textbf{Grid search time and resource calculator}',
    'title_y': 10.0,
    'title_x':10,
    # 'make_grid': True,
    # 'debug': True,
    'isopleth_params': [
        # {'color': 'black',
        #  'linewidth': 'thin',
        #  'linestyle': 'solid',
        #  'circle_size': 0.08,
        #  'transparency': 0.0,
        #  },
        {'color': 'black',
         'linewidth': 'thin',
         'linestyle': 'dashed',
         'circle_size': 0.05,
         'transparency': 0.25,
         },
    ],
    'extra_texts': [
        {
            'x': 9.0,
            'y': 0.0,
            'text': r'\small \noindent Example shown: \par \noindent Six searchers spaced 7.5 meters apart \
                need to walk 3 kilometers to search an area of 13.5 hectares. If the team travels at \
                2 kilometers per hour (or covers 100 meters every 3 minutes) they will need 90 minutes to \
                cover the assigned area.',
            'width': 8,
        },
        {
            'x': 14.2,
            'y': -2.0,
            'text': r'\tiny \copyright Daniel Boulet  2020',
            'width': 5.0,
        },
        {
            'x': 1,
            'y': 7.0,
            'text': r'$\frac{Area}{Distance}=Searchers \times Spacing$',
            'width': 10.0,

        },

    ],


}


Nomographer(main_params)
