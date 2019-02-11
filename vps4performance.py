"""
    vps4performance.py

    Gas turbine performance nomograph based on Vericor VPS4 genset.

    Copyright (C) 2019 Daniel Boulet

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

# allows use of latex commands in PyX such as \frac{a}{b} and \par
text.set(mode="latex")


def watts2btu_hr(watts):
    return watts*3.412141633


def btu_hr2watts(btu_hr):
    return btu_hr/3.412141633


def btu2joule(btu):
    return btu*1055.06


def joule2btu(joule):
    return joule/1055.06


'''
this part is the left handside of the total graph
'''

leftside_u1_left = {
    'tag': 'left_1',

    # range of values (nominal 3451000.0 W )
    'u_min': 3.0,
    'u_max': 4.0,

    # functions
    'function': lambda u: u*1000000.0,

    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',

    # tick and title locations
    'title': r'\Large $MW$',
    'title_x_shift': -1.0,
    'title_y_shift': 0.5,
    'tick_side': 'left',

    # extra parameters
    'extra_params': [
        {
            'scale_type': 'manual arrow',
            'manual_axis_data':
            {
                3.451: r'VPS4',
            },
            'arrow_length': 1.5,
        },
    ],


    # additional title information
    'extra_titles': [
        {
            'dx': -1.5,
            'dy': 2.0,
            'text': '\Large Power \par Output',
            # 'width': 5.0
        },
    ],


}

leftside_u1_right = {
    'tag': 'left_1',

    # range of values (nominal 11778263.0 BTU/hr )
    'u_min': 3.0*watts2btu_hr(1000000.0)/1000000.0,
    'u_max': 4.0*watts2btu_hr(1000000.0)/1000000.0,

    # functions
    'function': lambda u: u*1000000.0,
    'align_func': lambda u: u/watts2btu_hr(1000000.0)*1000000.0,

    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',

    # tick and title locations
    'title': r'\Large $\frac{MBTU}{hr}$',
    'title_x_shift': 1.0,
    'title_y_shift': 0.5,
    'tick_side': 'right',

}

leftside_u2_left = {
    # range of values (nominal 28%)
    'u_min': 0.25*100.0,
    'u_max': 0.35*100.0,

    # functions
    'function': lambda u: u/100.0,

    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',

    # tick and title locations
    'title': r'\Large $\%$',
    'title_x_shift': -1.0,
    'title_y_shift': 0.5,
    'tick_side': 'left',

    # additional title information
    'extra_titles': [
        {
            'dx': -1.5,
            'dy': 2.0,
            'text': '\Large Efficiency / \par Heat Rate',
            # 'width': 5.0
        },
    ],

    # extra parameters
    'extra_params': [
        {
            'scale_type': 'manual arrow',
            'manual_axis_data':
            {
                28.4: r'VPS4',
            },
            'arrow_length': 1.5,
        },
    ],


}

leftside_u2_right = {
    # range of values (nomninal 12025 BTU/kWh )
    'u_min': watts2btu_hr(100000.0)/35.0,
    'u_max': watts2btu_hr(100000.0)/25.0,

    # functions
    'function': lambda u: watts2btu_hr(1000.0)/(u),
    'text_format': r"$%4.0f$",
    # 'align_func': lambda u:341300.0/u,

    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',

    # tick and title locations
    'title': r'\Large $\frac{BTU}{kw \cdot hr}$',
    'title_x_shift': 1.0,
    'title_y_shift': 0.5,
    'tick_side': 'right',
}

leftside_u3_left = {
    'tag': 'mid',

    # range of values (nominal 12325000.0 W )
    'u_min': 10.0,
    'u_max': 14.0,

    # functions
    'function': lambda u: u*1000000.0,

    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',

    # tick and title locations
    'title': r'\Large $MW$',
    'title_x_shift': -1.0,
    'title_y_shift': 0.5,
    'tick_side': 'left',

    # additional title information
    'extra_titles': [
        {
            'dx': -1.5,
            'dy': 2.0,
            'text': '\Large Power \par Input',
            # 'width': 5.0
        },
    ],


}

leftside_u3_right = {
    # range of values (nominal 42065225.0 BTU/hr )
    'u_min': 10.0*watts2btu_hr(1000000.0)/1000000.0,
    'u_max': 14.0*watts2btu_hr(1000000.0)/1000000.0,

    # functions
    'function': lambda u: u*1000000.0,
    'align_func': lambda u: u/watts2btu_hr(1000000.0)*1000000.0,

    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',

    # tick and title locations
    'title': r'\Large $\frac{MBTU}{hr}$',
    'title_x_shift': 1.0,
    'title_y_shift': 0.5,
    'tick_side': 'right',
}

'''

this part is the right hand side of the total graph

'''

rightside_u3_left = {
    'tag': 'mid',

    # range of values (nominal 12325000.0 W )
    'u_min': 10.0,
    'u_max': 14.0,

    # functions
    'function': lambda u: u*1000000.0,

    # # scale type and detail
    'scale_type': 'manual point',

    # 'tick_levels': 4,
    # 'tick_text_levels': 3,
    # 'scale_type': 'linear smart',

    # # tick and title locations
    # 'title': r'MW',
    # 'title_x_shift': -1.0,
    # 'title_y_shift':0.5,
    # 'tick_side': 'left',

    # additional title information
    # 'extra_titles': [
    #     {
    #         'dx': -1.5,
    #         'dy': 2.0,
    #         'text': 'extra title',
    #         # 'width': 5.0
    #     },
    # ],


}

rightside_u3_right = {
    # range of values (nominal 42065225.0 BTU/hr )
    'u_min': 10.0*watts2btu_hr(1000000.0)/1000000.0,
    'u_max': 14.0*watts2btu_hr(1000000.0)/1000000.0,

    # functions
    'function': lambda u: u*1000000.0,
    'align_func': lambda u: u/watts2btu_hr(1000000.0)*1000000.0,


    # scale type and detail
    'scale_type': 'manual point',

    # 'tick_levels': 4,
    # 'tick_text_levels': 3,
    # 'scale_type': 'linear smart',

    # # tick and title locations
    # 'title': r'mill. BTU/hr',
    # 'title_y_shift':0.5,
    # 'title_x_shift': 1.0,
}


rightside_u2_left = {
    # range of values (nominal 45000000 MJ / kg )
    'u_min': 40.0,
    'u_max': 50.0,

    # functions
    'function': lambda u: 1.0/(u*1000000.0),

    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',

    # tick and title locations
    'title': r'\Large $\frac{MJ}{kg}$',
    'title_x_shift': -1.0,
    'title_y_shift': 0.5,
    'tick_side': 'left',

    # extra parameters
    'extra_params': [
        {
        },
    ],


    # additional title information
    'extra_titles': [
        {
            'dx': -1.5,
            'dy': 2.0,
            'text': '\Large \\ \par Fuel LHV',
            # 'width': 5.0
        },
    ],


}

rightside_u2_right = {
    # range of values (nominal 20000 BTU/lb)
    'u_min': 40000000.0/2321.13,
    'u_max': 50000000.0/2321.13,

    # functions
    'function': lambda u: 1.0/(u),
    # 'align_func':lambda u: u*2326.0/1000000.0,

    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',
    'text_format': r"$%4.0f$",

    # tick and title locations
    'title': r'\Large $\frac{BTU}{lb}$',
    'title_x_shift': 1.0,
    'title_y_shift': 0.5,
    'tick_side': 'right',

    # extra parameters
    'extra_params': [
        {
            'scale_type': 'manual arrow',
            'manual_axis_data':
            {
                20548.0: r'VPS4',
            },
            'arrow_length': 2.0,
        },
    ],


}


rightside_u1_left = {
    'tag': 'right_1',

    # range of values (nominal 1000 kg/hr )
    'u_min': 800.0,
    'u_max': 1200.0,

    # functions
    'function': lambda u: u/3600.0,

    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',

    # tick and title locations
    'title': r'\Large $\frac{kg}{hr}$',
    'title_x_shift': -1.0,
    'title_y_shift': 0.5,
    'tick_side': 'left',

    # additional title information
    'extra_titles': [
        {
            'dx': -1.5,
            'dy': 2.0,
            'text': '\Large Fuel Cons. \par Rate',
            # 'width': 5.0
        },
    ],


}

rightside_u1_right = {
    'tag': 'right_1',

    # range of values (nominal 2020 lb/hr )
    'u_min': 800*2.2,
    'u_max': 1200.0*2.2,

    # functions
    'function': lambda u: u,
    'align_func': lambda u: u/2.2,
    # scale type and detail
    'tick_levels': 4,
    'tick_text_levels': 3,
    'scale_type': 'linear smart',

    # tick and title locations
    'title': r'\Large $\frac{lbs}{hr}$',
    'title_x_shift': 1.0,
    'title_y_shift': 0.5,
    'tick_side': 'right',

    # extra parameters
    'extra_params': [
        {
            'scale_type': 'manual arrow',
            'manual_axis_data':
            {
                2020.0: r'VPS4',
            },
            'arrow_length': 1.5,
        },
    ],


}


leftside_SI_block = {
    'block_type': 'type_2',
    'f1_params': leftside_u1_left,
    'f2_params': leftside_u2_left,
    'f3_params': leftside_u3_left,
    'isopleth_values': [[3.451, 28.4, 'x']],
}

leftside_IMP_block = {
    'block_type': 'type_2',
    'f1_params': leftside_u1_right,
    'f2_params': leftside_u2_right,
    'f3_params': leftside_u3_right,
    'isopleth_values': [[watts2btu_hr(3.451), 'x', watts2btu_hr(3.451)/.284]],

}

rightside_SI_block = {
    'block_type': 'type_2',
    'f1_params': rightside_u1_left,
    'f2_params': rightside_u2_left,
    'f3_params': rightside_u3_left,
    'isopleth_values': [[2020.0/2.2, 'x', 'x']],
    'mirror_x': True,
}

rightside_IMP_block = {
    'block_type': 'type_2',
    'f1_params': rightside_u1_right,
    'f2_params': rightside_u2_right,
    'f3_params': rightside_u3_right,
    'isopleth_values': [[2020.0, 'x', watts2btu_hr(3.451)/.284]],
    'mirror_x': True,
}

main_params = {
    'filename': 'vps4performance.pdf',
    'paper_height': 8.0*2.54,
    'paper_width': 10.5*2.54,
    'block_params': [leftside_SI_block, rightside_SI_block, leftside_IMP_block, rightside_IMP_block],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_str': r"\Huge G.T. Performance \par Nomograph",
    'title_x': 5.5,
    'title_y': 21.0,
    'extra_texts': [
        {
            'text': r'\Large \% eff = $\frac{341214.1633}{HR}$',
                'x': 4.0,
                'y': 2.0,
            # 'width': 5.0
        },
        {
            'text': r'\Large HR = $\frac{3412.141533 \times P_{in}}{P_{out}}$',
            'x': 4.0,
            'y': 1.0,
        },
        {
            'text': r'\Large Power = LHV $\times$ Consumption',
            'x': 16.0,
            'y': 2.0,
            'width': 10.0
        },
        {
            'text': r'\copyright Daniel Boulet  2019',
            'x': 25.0,
            'y': -2.0,
        },
        {
            'x':16.0,
            'y':20.0,
            'text': r'\noindent Example: \par \medskip \noindent Working from left to right, 3.451\,MW output at at 28.4\% efficiency requires 12.151\,MW input to turbine. From right to left, fuel flow rate of 2020 lbs per hour of fuel with heat value of 47.5\,MJ per kg will produce 12.151\,MW input to turbine. \par \medskip \noindent (Note: different system of units may be combined in a single calculation.)',
            'width':7.0,
        }
    ],
    # 'make_grid': True,
}
Nomographer(main_params)
