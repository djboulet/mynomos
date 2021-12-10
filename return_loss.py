"""
    return_loss.py

    Nomogram to calculate VSWR at antenna given measured VSWR and feedline antenuation.

    Copyright(C) 2021 Daniel Boulet

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
import numpy as np
from pyx import *

outputfile = sys.argv[0].split('.')[0]+'.pdf'
sys.path.insert(0, "..")
text.set(text.LatexEngine)

from pynomo.nomographer import Nomographer

minimum_return_loss = 6.0
maximum_return_loss = 40.0


# functions to convert return loss to VSWR and vice-versa


def vswr2rl(vswr):
    return -20 * np.log10((vswr - 1) / (vswr + 1))


def rl2vswr(rl):
    return (1 + 10 ** (-rl / 20)) / (1 - 10 ** (-rl / 20))


# main block items

measured_rl = {
    "tag": "measured",
    "u_min": minimum_return_loss,
    "u_max": maximum_return_loss,
    "function": lambda u: u,
    "scale_type": "linear smart",
    "title": r"Return loss (dB)",
    "title_relative_offset": (0, 1.5),
    "title_draw_center": True,
    "tick_side": "left",
    "tick_levels": 4,
    "tick_text_levels": 3,
    "extra_titles": [
        {
            "dx": -1.2,
            "dy": 0.5,
            "text": r"\Large \textbf{Feedpoint}",
            # 'width':5.0,
        }
    ],
}


antenna_rl = {
    "tag": "antenna",
    "u_min": 6,
    "u_max": 30,
    "scale_type": "linear smart",
    "function": lambda u: -u,
    "title": r"Return loss (dB)",
    "title_draw_center": True,
    "extra_titles": [
        {
            "dx": -1.2,
            "dy": 0.5,
            "text": r"\Large \textbf{Antenna}",
            # 'width':5.0,
        }
    ],
    "title_relative_offset": (0, 1.5),
    "tick_levels": 2,
    "tick_text_levels": 1,
    "tick_side": "left",
}

cable_loss = {
    "tag": "cable_loss",
    "u_min": 0,
    "u_max": 10.0,
    "scale_type": "linear smart",
    "function": lambda u: -2 * u,
    "title": r"\Large \textbf{Attenuation (dB)}",
    "title_relative_offset": (0, -2.5),
    # "title_draw_center": True,
    "tick_side": "left",
    "tick_levels": 4,
    "tick_text_levels": 3,
    # "extra_params": [
    #     {
    #         "scale_type": "manual arrow",
    # 		'tick_side':'right',
    #         "manual_axis_data": {
    #             8.5: "100ft LMR195 70cm band",
    #         },
    #     }
    # ],
}

main_block = {
    "block_type": "type_1",
    "f1_params": measured_rl,
    "f3_params": cable_loss,
    "f2_params": antenna_rl,
    "isopleth_values": [["x", "x", 'x']],
    "mirror_y": True,
}

# measured vswr items
measured_vswr = {
    "tag": "measured",
    "u_min": rl2vswr(maximum_return_loss),
    "u_max": rl2vswr(minimum_return_loss),
    "function": lambda u: vswr2rl(u),
    "align_func": lambda u: vswr2rl(u),
    "title": r"VSWR",
    "title_draw_center": True,
    "title_relative_offset": (0, 1),
    "tick_levels": 6,
    "tick_text_levels": 3,
    "scale_type": "linear smart",
    "tick_side": "right",
}

measured_vswr_block = {
    "block_type": "type_8",
    "f_params": measured_vswr,
    "isopleth_values": [[1.3]],
}

# antenna vswr items

antenna_vswr = {
    "tag": "antenna",
    "u_min": rl2vswr(30),
    "u_max": rl2vswr(6),
    "function": lambda u: vswr2rl(u),
    "align_func": lambda u: vswr2rl(u),
    "title": r"VSWR",
    "title_relative_offset": (0, 1.5),
    "title_draw_center": True,
    "tick_levels": 6,
    "tick_text_levels": 3,
    "scale_type": "linear smart",
    "tick_side": "right",
}

antenna_vswr_block = {
    "block_type": "type_8",
    "f_params": antenna_vswr,
    "isopleth_values": [["x"]],
}

# cable loss items (type 2 block)
cable_loss_arrows = {
    "tag": "cable_loss",
    "u_min": 0.0,
    "u_max": 10.0,
    "function": lambda u: u,
    # "title": r"cable loss",
    "tick_levels": 3,
    "tick_text_levels": 1,
    "scale_type": "manual",
}

loss_per_unit_length_lmr195 = {
    "tag": "cable_type",
    "u_min": 1.0,
    "u_max": 30.0,
    "function": lambda u: u,
    "align_function": lambda u: u,
    "title": r"LMR195",
    "title_rotate_text": True,
    "title_x_shift": -0.1,
    "title_y_shift": 1.1,
    # "title_draw_center": True,
    "tick_levels": 3,
    "tick_text_levels": 2,
    "tick_side": "left",
    "scale_type": "manual arrow",
    "manual_axis_data": {
        3.2: r"40m",
        4.5: r"20m",
        5.5: r"15m",
        6.4: r"10m",
        8.7: r"6m",
        14.5: r"2m",
        25.2: r"70cm",
    },
    # "title_relative_offset": (0, 0),
}

loss_per_unit_length_lmr400 = {
    "tag": "cable_type",
    "u_min": 1.0,
    "u_max": 30.0,
    "function": lambda u: u,
    "align_function": lambda u: u,
    "title": r"LMR400",
    "title_rotate_text": True,
    "title_x_shift": 0.3,
    "title_y_shift": -0.8,
    # "title_draw_center": True,
    "tick_levels": 3,
    "tick_text_levels": 2,
    "tick_side": "right",
    "scale_type": "manual arrow",
    "manual_axis_data": {
        1.1: r"40m",
        # 1.5: r"20m",
        # 1.9: r"15m",
        2.2: r"10m",
        3.0: r"6m",
        5.0: r"2m",
        8.9: r"70cm",
    },
    # "title_relative_offset": (0, -2.5),
}

length_meters = {
    "tag": "clength",
    "u_min": 10.0,
    "u_max": 100.0,
    "function": lambda u: u / 100.0,
    "title": r"Meters",
    "tick_levels": 3,
    "tick_text_levels": 1,
    "title_draw_center": True,
    "tick_side": "left",
    "title_relative_offset": (0, 1.5),
    "extra_titles": [
        {
            "dx": -2.0,
            "dy": 0.4,
            "text": r"\Large \textbf{Cable Length}",
        }
    ],
}

length_feet = {
    "tag": "clength",
    "u_min": 10.0 / 0.3048,
    "u_max": 100.0 / 0.3048,
    "function": lambda u: u,
    "align_func": lambda u: u * 0.3048,
    "title": r"Feet",
    "title_draw_center": True,
    "tick_levels": 3,
    "tick_text_levels": 1,
    "title_relative_offset": (0, -2.5),
}
cable_parameters = {
    "block_type": "type_2",
    # "width": 10.0,
    # "height": 10.0,
    "f1_params": cable_loss_arrows,
    "f2_params": loss_per_unit_length_lmr195,
    "f3_params": length_meters,
    'isopleth_values': [['x', 6.4, 'x']],
}

cable_parameters2 = {
    "block_type": "type_8",
    "f_params": loss_per_unit_length_lmr400,
	'isopleth_values':[['x']],
}

cable_parameters3 = {
    "block_type": "type_8",
    "f_params": length_feet,
	'isopleth_values':[[150]],
}


main_params = {
    "filename": outputfile,
    "paper_height": 8.0 * 2.54,
    "paper_width": 10.5 * 2.54,
    # "block_params": [main_block],
    "block_params": [
        main_block,
        measured_vswr_block,
        antenna_vswr_block,
        cable_parameters,
        cable_parameters2,
        cable_parameters3,
    ],
    # "block_params": [main_block,measured_vswr_block],
    "transformations": [("rotate", 0.01), ("scale paper",)],
    "title_str": r"\huge \textbf{VSWR reduction due to cable attenuation}",
    "title_x": 18.0,
    "title_y": 20.5,
    "extra_texts": [
        {
            "x": 3.0,
            "y": 19.0,
            "text":r"\noindent \textbf{How to use:} \
				\par \medskip \noindent Draw a straight line from the \textit{Cable Length} axis through the appropriate cable and frequency band  to the \textit{Attenuation} axis. Draw a second line from the measured VSWR or return loss value on the \textit{Feedpoint} axis to the intersection of the first line and the \textit{Attenuation} axis.  Read the actual antenna VSWR or return loss on the \textit{Antenna} axis. \
				\par \medskip \noindent  \copyright Daniel Boulet (2021)",
            "width": 9.0,
        },
    ],
    "debug": False,
    # "make_grid": True,
}

Nomographer(main_params)
