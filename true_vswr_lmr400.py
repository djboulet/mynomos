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


# various conversion functions
def vswr2rl(vswr):
    # vswr to return loss in db
    return -20 * np.log10((vswr - 1) / (vswr + 1))


def rl2vswr(rl):
    # return loss to vswr
    return (1 + 10 ** (-rl / 20)) / (1 - 10 ** (-rl / 20))


def watts2dbw(watts):
    # watts to dbW
    return 10 * np.log10(watts)


def dbw2watts(dbw):
    # dbW to watts
    return 10 ** (dbw / 10.0)


def cableloss(freq):
    # cable loss in db per meter at freq
    # source formula is db per 100 feet
    return (np.sqrt(freq) * 0.122290 + freq * 0.000260) / 100.0 / 0.3048


# measured return loss axes and block section
axis1_forward_power_meas_watts = {
    "tag": "axis14",
    "u_min": 10.0,
    "u_max": 150.0,
    "title": r"$P_{fwd}$",
    "tick_levels": 5,
    "tick_text_levels": 4,
    "function": lambda u: watts2dbw(u),
    "align_func": lambda u: watts2dbw(u),
    "scale_type": "linear smart",
    "tick_side": "left",
}

block_forward_watts = {
    "block_type": "type_8",
    "f_params": axis1_forward_power_meas_watts,
    "isopleth_values": [["x"]],
}

axis2_reflected_power_meas_watts = {
    "tag": "axis25",
    "title": r"$P_{ref}$",
    "u_min": 0.1,
    "u_max": 10.0,
    "function": lambda u: watts2dbw(u),
    "align_func": lambda u: watts2dbw(u),
    "tick_levels": 5,
    "tick_text_levels": 4,
    "tick_side": "left",
    "scale_type": "linear smart",
}

block_reflected_watts = {
    "block_type": "type_8",
    "f_params": axis2_reflected_power_meas_watts,
    "isopleth_values": [["x"]],
}

axis3_return_loss_meas_vswr = {
    "tag": "axis36",
    "u_min": 1.2,
    "u_max": 3.0,
    "title": r"VSWR (Measured)",
    "function": lambda u: vswr2rl(u),
    "align_func": lambda u: vswr2rl(u),
    "tick_levels": 5,
    "tick_text_levels": 4,
    "tick_side": "left",
    "scale_type": "linear smart",
}

block_return_loss_meas_vswr = {
    "block_type": "type_8",
    "f_params": axis3_return_loss_meas_vswr,
    "isopleth_values": [["x"]],
}

axis4_forward_power_meas_dbw = {
    "tag": "axis14",
    "u_min": watts2dbw(10.0),
    "u_max": watts2dbw(100.0),
    "function": lambda u: -u,
    "title_draw_center": True,
    "tick_side": "left",
    "tick_levels": 5,
    "title_distance_center": 1.7,
    "tick_text_levels": 4,
    "scale_type": "manual",
}

axis5_reflected_power_meas_dbw = {
    "tag": "axis25",
    "u_min": watts2dbw(0.1),
    "u_max": watts2dbw(7.0),
    "function": lambda u: u,
    "title_distance_center": -1.7,
    "title_draw_center": True,
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "manual",
}

axis6_return_loss_meas_dbw1 = {
    "tag": "axis36",
    "u_min": 7.0,
    "u_max": 30.0,
    "function": lambda u: u,
    "title_distance_center": 1.5,
    "title_draw_center": True,
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "manual",
}


block_measured_rl_dbw = {
    "block_type": "type_1",
    "f1_params": axis4_forward_power_meas_dbw,
    "f2_params": axis5_reflected_power_meas_dbw,
    "f3_params": axis6_return_loss_meas_dbw1,
    "height": 20.0,
    "width": 20.0,
    "isopleth_values": [[watts2dbw(60), watts2dbw(5), "x"]],
}


axis8_return_loss_true_dbw = {
    "tag": "axis8-10",
    "u_min": 1.0,
    "u_max": 30.0,
    "function": lambda u: -u,
    "title_draw_center": True,
    "tick_levels": 5,
    "title_distance_center": 1.5,
    "tick_text_levels": 4,
    "scale_type": "manual",
}

axis10_return_loss_true_vswr = {
    "tag": "axis8-10",
    "u_min": 1.2,
    "u_max": 20.0,
    "title": r"VSWR (True)",
    "function": lambda u: vswr2rl(u),
    "align_func": lambda u: vswr2rl(u),
    "tick_side": "left",
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
}

block_return_loss_true_vswr = {
    "block_type": "type_8",
    "f_params": axis10_return_loss_true_vswr,
    "isopleth_values": [["x"]],
}


axis9_cable_loss = {
    "tag": "axis9",
    "u_min": 0.0,
    "u_max": 10.0,
    "function": lambda u: -2.0 * u,
    "title_distance_center": -1.5,
    "title_draw_center": True,
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "manual",
}

block_true_rl_dbw = {
    "block_type": "type_1",
    "f1_params": axis6_return_loss_meas_dbw1,
    "f2_params": axis8_return_loss_true_dbw,
    "f3_params": axis9_cable_loss,
    "isopleth_values": [["x", "x", "x"]],
}

# cable loss block using type 5
block_cable_loss = {
    "block_type": "type_5",
    "u_func": lambda u: u,
    "u_values": list(np.linspace(25.0, 125.0, 21)),
    "u_scale_type": "manual point",
    "u_title_distance_center": 1.0,
    "u_title": "Cable length (m)",
    "v_func": lambda x, v: x / cableloss(v),
    "v_values": [1.75, 3.5, 7.0, 14.0, 28.0, 50.0, 144.0, 440.0],
    "v_title": "Freq (MHz)",
    "wd_tick_levels": 4,
    "wd_tick_text_levels": 1,
    "wd_tick_side": "left",
    "wd_title": r"LMR400\textsuperscript{\textregistered} Cable Loss (db)",
    "wd_title_opposite_tick": True,
    "wd_tag": "axis9",
    "isopleth_values": [[75, 144, "x"]],
}

main_params = {
    "filename": outputfile,
    "paper_height": 8.0 * 2.54,
    "paper_width": 10.5 * 2.54,
    "block_params": [
        block_measured_rl_dbw,
        block_true_rl_dbw,
        block_reflected_watts,
        block_forward_watts,
        block_return_loss_meas_vswr,
        block_return_loss_true_vswr,
        block_cable_loss,
    ],
    "transformations": [("rotate", 0.01), ("scale paper",)],
    "title_str": r"\huge \textbf{True VSWR as a result of cable attenuation for LMR400\textsuperscript{\textregistered}} \
		\par\medskip \normalsize \copyright Daniel Boulet (2021)",
    "title_x": 7.0,
    "title_y": 19.0,
    "title_box_width": 12.0,
    "extra_texts": [
        {
            "x": 1.0,
            "y": 16.5,
            "text": r"\noindent Calculate true VSWR by drawing \
				a straight line from forward power axis through the reflected \
				power axis to the measured VSWR axis. \
				To compensate for cable loss draw straight line from \
				measured VSWR to cable loss value.  True VSWR can be read at \
				the intersection of true VWSR axis.",
            "width": 12.0,
        },
        {
            "x": 0.0,
            "y": 3.0,
            "text": r"\noindent \textbf{Example:} \
				\par \noindent Measured forward and reflected power are \
				60W and 5W respectively thus measured VSWR is 1.81:1. \
				However 75m of LMR400\textsuperscript{\textregistered} will attenuate \
				a 144MHz signal by 3.70 dB therefore true VSWR is 5.20:1.",
            "width": 9.0,
        },
    ],
    # "make_grid": True,
}
Nomographer(main_params)
