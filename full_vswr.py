"""
    full_vswr.py

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

outputfile = sys.argv[0].split(".")[0] + ".pdf"
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


def watts2dbw(watts):
    return 10 * np.log10(watts)


def dbw2watts(dbw):
    return 10 ** (dbw / 10.0)


# measured return loss axes and block section
axis1_forward_power_meas_watts = {
    "tag": "forward_power_meas",
    "u_min": 5.0,
    "u_max": 100.0,
    "title_distance_center": -2.0,
    "title": "axis1",
    "title_draw_center": True,
    "function": lambda u: watts2dbw(u),
    "align_func": lambda u: watts2dbw(u),
	'scale_type':'linear smart',
}

block_forward_watts = {
    "block_type": "type_8",
    "f_params": axis1_forward_power_meas_watts,
}

axis2_reflected_power_meas_watts = {
    "tag": "reflected_power_meas",
    "title": r"axis2",
    "u_min": 0.1,
    "title_draw_center": True,
    "u_max": 7.0,
    "title_distance_center": 2.0,
    "function": lambda u: watts2dbw(u),
    "align_func": lambda u: watts2dbw(u),
    "tick_side": "left",
	'scale_type':'linear smart',
}

block_reflected_watts = {
    "block_type": "type_8",
    "f_params": axis2_reflected_power_meas_watts,
}

axis3_return_loss_meas_vswr = {
    "tag": "return_loss_meas_dbw",
    "u_min": rl2vswr(30),
    "u_max": rl2vswr(7),
    "title_draw_center": True,
    "title": r"axis3",
    "title_distance_center": 2.0,
    "function": lambda u: vswr2rl(u),
    "align_func": lambda u: vswr2rl(u),
    "tick_side": "left",
	'scale_type':'linear smart',
}

block_return_loss_meas_vswr = {
    "block_type": "type_8",
    "f_params": axis3_return_loss_meas_vswr,
}

axis4_forward_power_meas_dbw = {
    "tag": "forward_power_meas",
    "u_min": watts2dbw(5.0),
    "u_max": watts2dbw(100.0),
    "function": lambda u: -u,
    "title": r"axis4",
    "title_draw_center": True,
    "tick_side": "left",
    "tick_levels": 5,
    "title_distance_center": 2.0,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
}

axis5_reflected_power_meas_dbw = {
    "tag": "reflected_power_meas",
    "u_min": watts2dbw(0.1),
    "u_max": 7.0,
    "function": lambda u: u,
    # 'align_func': lambda u: dbw2watts(u),
    "title": r"axis5",
    "title_distance_center": -2.0,
    "title_draw_center": True,
    "tick_levels": 5,
    # "title_draw_center": True,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
}

axis6_return_loss_meas_dbw1 = {
    "tag": "return_loss_meas_dbw",
    "u_min": 7.0,
    "u_max": 30.0,
    "function": lambda u: u,
    "title_distance_center": 2.0,
    "title": r"axis6",
    "title_draw_center": True,
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
}


block_measured_rl_dbw = {
    "block_type": "type_1",
    "f1_params": axis4_forward_power_meas_dbw,
    "f2_params": axis5_reflected_power_meas_dbw,
    "f3_params": axis6_return_loss_meas_dbw1,
    "width": 5.0,
    # "height": 5.0,
    #     # "isopleth_values": [[60.0,'x',1.0],[30.0,'x',2.0]],
}


# actual return loss axes and block section
# axis7_return_loss_meas_dbw2 = {
#     "tag": "return_loss_meas_dbw",
#     "u_min": 7.0,
#     "u_max": 30.0,
#     "function": lambda u: u,
#     "title_distance_center": 2.0,
#     "title_draw_center": True,
#     "title": r"axis7",
#     "tick_levels": 5,
#     "tick_text_levels": 4,
#     "scale_type": "linear smart",
# }

axis10_return_loss_meas_vswr = {
    "tag": "a",
    "u_min": rl2vswr(30),
    "u_max": rl2vswr(7),
    "title_draw_center": True,
    "title": r"axis10",
    "title_distance_center": 2.0,
    "function": lambda u: vswr2rl(u),
    "align_func": lambda u: vswr2rl(u),
    "tick_side": "left",
	'scale_type':'linear smart',
}

block_return_loss_true_vswr = {
    "block_type": "type_8",
    "f_params": axis10_return_loss_meas_vswr,
}


axis8_return_loss_true_dbw = {
	'tag':'a',
    "u_min": 5.0,
    "u_max": 30.0,
    "function": lambda u: -u,
    "title_draw_center": True,
    "title": r"axis8",
    "tick_levels": 5,
    "title_distance_center": 2.0,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
}

axis9_cable_loss = {
    "tag": "attenuation",
    "u_min": 0.0,
    "u_max": 10.0,
    "function": lambda u: -2.0 * u,
    "title_distance_center": -2.0,
    "title": r"axis9",
    "title_draw_center": True,
    # "tick_levels": 5,
    # "tick_text_levels": 4,
	'scale_type':'linear smart',
}

block_true_rl_dbw = {
    "block_type": "type_1",
    "f1_params": axis6_return_loss_meas_dbw1,
    "f2_params": axis8_return_loss_true_dbw,
    "f3_params": axis9_cable_loss,
    # 'mirror_x':True,
    #     # "isopleth_values": [[60.0,'x',1.0],[30.0,'x',2.0]],
}

# cable loss block using type 5
block_cable_loss = {
    "block_type": "type_5",
    # 'wd_tag': 'ratio',
    # 'mirror_y':True,
    "u_func": lambda u: u,
    "v_func": lambda x, v: x / (np.sqrt(v) * 0.424232 + v * 0.000563),
    # lengths
    "u_values": list(np.linspace(0.1, 1.0, 10)),
    "u_scale_type": "manual point",
    # 'u_manual_axis_data': {12.0: '7', 14.0: '6', 16.0: '5', 18.0: '4', 21.0: '3', 24.0: '2', 28.0: '1'},
    "u_title": "length",
    # teeth on front derailer
    "v_values": [1.75, 3.5, 7.0, 14.0, 28.0, 50.0, 144.0, 440.0],
    # 'v_scale_type': 'manual point',
    # 'v_manual_axis_data': {28.0: 'Small', 38.0: 'Medium', 48.0: 'Large'},
    "v_title": "freq",
    "wd_tick_levels": 4,
    "wd_tick_text_levels": 1,
    "wd_tick_side": "left",
    "wd_title": "loss",
    "wd_title_opposite_tick": True,
    "wd_tag": "attenuation",
    # 'wd_scale_type':'manual',
    # 'isopleth_values': [[14.0, 38.0, 'x']],
}


# # cable loss axes and block section
# attenuation2 = {
# 	'tag':'attenuation',
#     "u_min": 0.1,
#     "u_max": 10.0,
#     "function": lambda u:u,
# 	# 'align_func': lambda u:u,
#     "title": r"Cable Loss",
#     "tick_levels": 5,
#     "tick_text_levels": 4,
#     "scale_type": "linear smart",
# }

# loss_per_unit_length_lmr195 = {
#     # "tag": "cable_type",
#     "u_min": 4.0,
#     "u_max": 30.0,
#     "function": lambda u: u,
#     # "align_function": lambda u: u,
#     "title": r"LMR195",
#     # "title_rotate_text": True,
#     # "title_x_shift": -0.1,
#     # "title_y_shift": 1.1,
#     # "title_draw_center": True,
#     "tick_levels": 3,
#     "tick_text_levels": 2,
#     "tick_side": "left",
#     "scale_type": "manual arrow",
#     "manual_axis_data": {
#         # 3.2: r"40m",
#         4.5: r"20m",
#         5.5: r"15m",
#         6.4: r"10m",
#         8.7: r"6m",
#         14.5: r"2m",
#         25.2: r"70cm",
#     },
#     # "title_relative_offset": (0, 0),
# }

# length_meters = {
#     # "tag": "clength",
#     "u_min": 10.0,
#     "u_max": 50.0,
#     "function": lambda u: u/100.0,
#     "title": r"Meters",
#     "tick_levels": 3,
#     "tick_text_levels": 1,
#     # "title_draw_center": True,
#     # "tick_side": "left",
#     # "title_relative_offset": (0, 1.5),
#     # "extra_titles": [
#     #     {
#     #         "dx": -2.0,
#     #         "dy": 0.4,
#     #         "text": r"\Large \textbf{Cable Length}",
#     #     }
#     # ],
# }

# cable_loss_block = {
# 	'block_type':'type_2',
#     "f1_params": attenuation2,
#     "f2_params": length_meters,
#     "f3_params": loss_per_unit_length_lmr195,
# 	# 'mirror_x':True,
# 	'mirror_y':True,
# }

main_params = {
    "filename": "full_vswr.pdf",
    "paper_height": 8.0 * 2.54,
    "paper_width": 10.5 * 2.54,
    # "block_params": [main_block],
    "block_params": [
        block_measured_rl_dbw,
        block_true_rl_dbw,
        block_reflected_watts,
        block_forward_watts,
        block_return_loss_meas_vswr,
		block_return_loss_true_vswr,
		block_cable_loss,
        # cable_loss_block,
        # cable_loss_type5,
        #         main_block,
        #         measured_vswr_block,
        #         antenna_vswr_block,
        #         cable_parameters,
        #         cable_parameters2,
        #         cable_parameters3,
    ],
    "transformations": [("rotate", 0.01), ("scale paper",)],
    # "title_str": r"\huge \textbf{VSWR reduction due to cable attenuation}",
    #     "title_x": 18.0,
    #     "title_y": 20.5,
    #     "extra_texts": [
    #         {
    #             "x": 3.0,
    #             "y": 19.0,
    #             "text": r"\noindent \textbf{How to use:} \
    # 				\par \medskip \noindent Draw a straight line from the \textit{Cable Length} axis through the appropriate cable and frequency band  to the \textit{Attenuation} axis. Draw a second line from the measured VSWR or return loss value on the \textit{Feedpoint} axis to the intersection of the first line and the \textit{Attenuation} axis.  Read the actual antenna VSWR or return loss on the \textit{Antenna} axis. \
    # 				\par \medskip \noindent  \copyright Daniel Boulet (2021)",
    #             "width": 9.0,
    #         },
    #     ],
    #     "debug": False,
    # "make_grid": True,
}


Nomographer(main_params)


# main block items


# vswr = {
#     "u_min": 1.1,
#     "u_max": 5.0,
#     "function": lambda u: -math.log((u + 1) / (u - 1)),
#     "title": r"VSWR",
#     "tick_levels": 5,
#     "tick_text_levels": 4,
#     "scale_type": "linear smart",
# }


# # measured vswr items
# measured_vswr = {
#     "tag": "measured",
#     "u_min": rl2vswr(maximum_return_loss),
#     "u_max": rl2vswr(minimum_return_loss),
#     "function": lambda u: vswr2rl(u),
#     "align_func": lambda u: vswr2rl(u),
#     "title": r"VSWR",
#     "title_draw_center": True,
#     "title_relative_offset": (0, 1),
#     "tick_levels": 6,
#     "tick_text_levels": 3,
#     "scale_type": "linear smart",
#     "tick_side": "right",
# }


# measured_rl = {
#     "tag": "measured",
#     "u_min": minimum_return_loss,
#     "u_max": maximum_return_loss,
#     "function": lambda u: u,
#     "scale_type": "linear smart",
#     "title": r"Return loss (dB)",
#     "title_relative_offset": (0, 1.5),
#     "title_draw_center": True,
#     "tick_side": "left",
#     "tick_levels": 4,
#     "tick_text_levels": 3,
#     "extra_titles": [
#         {
#             "dx": -1.2,
#             "dy": 0.5,
#             "text": r"\Large \textbf{Feedpoint}",
#             # 'width':5.0,
#         }
#     ],
# }


# antenna_rl = {
#     "tag": "antenna",
#     "u_min": 6,
#     "u_max": 30,
#     "scale_type": "linear smart",
#     "function": lambda u: -u,
#     "title": r"Return loss (dB)",
#     "title_draw_center": True,
#     "extra_titles": [
#         {
#             "dx": -1.2,
#             "dy": 0.5,
#             "text": r"\Large \textbf{Antenna}",
#             # 'width':5.0,
#         }
#     ],
#     "title_relative_offset": (0, 1.5),
#     "tick_levels": 2,
#     "tick_text_levels": 1,
#     "tick_side": "left",
# }

# cable_loss = {
#     "tag": "cable_loss",
#     "u_min": 0,
#     "u_max": 10.0,
#     "scale_type": "linear smart",
#     "function": lambda u: -2 * u,
#     "title": r"\Large \textbf{Attenuation (dB)}",
#     "title_relative_offset": (0, -2.5),
#     # "title_draw_center": True,
#     "tick_side": "left",
#     "tick_levels": 4,
#     "tick_text_levels": 3,
#     # "extra_params": [
#     #     {
#     #         "scale_type": "manual arrow",
#     # 		'tick_side':'right',
#     #         "manual_axis_data": {
#     #             8.5: "100ft LMR195 70cm band",
#     #         },
#     #     }
#     # ],
# }

# main_block = {
#     "block_type": "type_1",
#     "f1_params": measured_rl,
#     "f3_params": cable_loss,
#     "f2_params": antenna_rl,
#     # "isopleth_values": [["x", "x", 'x']],
#     "mirror_y": True,
# }


# for_ref_vswr_block = {
#     "block_type": "type_1",
#     "f1_params": forward_power,
#     "f2_params": vswr,
#     "f3_params": reflected_power,
#     # "isopleth_values": [[60.0,'x',1.0],[30.0,'x',2.0]],
# }


# measured_vswr_block = {
#     "block_type": "type_8",
#     "f_params": measured_vswr,
#     "isopleth_values": [[1.3]],
# }

# # antenna vswr items

# antenna_vswr = {
#     "tag": "antenna",
#     "u_min": rl2vswr(30),
#     "u_max": rl2vswr(6),
#     "function": lambda u: vswr2rl(u),
#     "align_func": lambda u: vswr2rl(u),
#     "title": r"VSWR",
#     "title_relative_offset": (0, 1.5),
#     "title_draw_center": True,
#     "tick_levels": 6,
#     "tick_text_levels": 3,
#     "scale_type": "linear smart",
#     "tick_side": "right",
# }

# antenna_vswr_block = {
#     "block_type": "type_8",
#     "f_params": antenna_vswr,
#     # "isopleth_values": [["x"]],
# }

# # cable loss items (type 2 block)
# cable_loss_arrows = {
#     "tag": "cable_loss",
#     "u_min": 0.0,
#     "u_max": 10.0,
#     "function": lambda u: u,
#     # "title": r"cable loss",
#     "tick_levels": 3,
#     "tick_text_levels": 1,
#     "scale_type": "manual",
# }

# loss_per_unit_length_lmr195 = {
#     "tag": "cable_type",
#     "u_min": 1.0,
#     "u_max": 30.0,
#     "function": lambda u: u,
#     "align_function": lambda u: u,
#     "title": r"LMR195",
#     "title_rotate_text": True,
#     "title_x_shift": -0.1,
#     "title_y_shift": 1.1,
#     # "title_draw_center": True,
#     "tick_levels": 3,
#     "tick_text_levels": 2,
#     "tick_side": "left",
#     "scale_type": "manual arrow",
#     "manual_axis_data": {
#         3.2: r"40m",
#         4.5: r"20m",
#         5.5: r"15m",
#         6.4: r"10m",
#         8.7: r"6m",
#         14.5: r"2m",
#         25.2: r"70cm",
#     },
#     # "title_relative_offset": (0, 0),
# }

# loss_per_unit_length_lmr400 = {
#     "tag": "cable_type",
#     "u_min": 1.0,
#     "u_max": 30.0,
#     "function": lambda u: u,
#     "align_function": lambda u: u,
#     "title": r"LMR400",
#     "title_rotate_text": True,
#     "title_x_shift": 0.3,
#     "title_y_shift": -0.8,
#     # "title_draw_center": True,
#     "tick_levels": 3,
#     "tick_text_levels": 2,
#     "tick_side": "right",
#     "scale_type": "manual arrow",
#     "manual_axis_data": {
#         1.1: r"40m",
#         # 1.5: r"20m",
#         # 1.9: r"15m",
#         2.2: r"10m",
#         3.0: r"6m",
#         5.0: r"2m",
#         8.9: r"70cm",
#     },
#     # "title_relative_offset": (0, -2.5),
# }

# length_meters = {
#     "tag": "clength",
#     "u_min": 10.0,
#     "u_max": 100.0,
#     "function": lambda u: u / 100.0,
#     "title": r"Meters",
#     "tick_levels": 3,
#     "tick_text_levels": 1,
#     "title_draw_center": True,
#     "tick_side": "left",
#     "title_relative_offset": (0, 1.5),
#     "extra_titles": [
#         {
#             "dx": -2.0,
#             "dy": 0.4,
#             "text": r"\Large \textbf{Cable Length}",
#         }
#     ],
# }

# length_feet = {
#     "tag": "clength",
#     "u_min": 10.0 / 0.3048,
#     "u_max": 100.0 / 0.3048,
#     "function": lambda u: u,
#     "align_func": lambda u: u * 0.3048,
#     "title": r"Feet",
#     "title_draw_center": True,
#     "tick_levels": 3,
#     "tick_text_levels": 1,
#     "title_relative_offset": (0, -2.5),
# }
# cable_parameters = {
#     "block_type": "type_2",
#     # "width": 10.0,
#     # "height": 10.0,
#     "f1_params": cable_loss_arrows,
#     "f2_params": loss_per_unit_length_lmr195,
#     "f3_params": length_meters,
#     # 'isopleth_values': [['x', 6.4, 'x']],
# }

# cable_parameters2 = {
#     "block_type": "type_8",
#     "f_params": loss_per_unit_length_lmr400,
#     # 'isopleth_values':[['x']],
# }

# cable_parameters3 = {
#     "block_type": "type_8",
#     "f_params": length_feet,
#     # 'isopleth_values':[[150]],
# }
# jlfkljlsdfkjlsd
