"""
    manning2.py

    Manning formula for open channel flow

	Copyright (C) 2023 Daniel Boulet

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

hydraulic_flux = {
    "u_min": 0.01,
    "u_max": 1.0,
    "function": lambda u: u,
    "title": r"\Large Q ($\frac{m^3}{s}$)",
    "tick_levels": 3,
    "tick_text_levels": 1,
    "tick_side": "left",
}

hydraulic_area = {
    "u_min": 0.01,
    "u_max": 1.0,
    "function": lambda u: u,
    "title": r"\Large A ($m^2$)",
    "tick_levels": 3,
    "tick_text_levels": 2,
    "scale_type": "linear smart",
    "tick_side": "left",
    "title_draw_center": True,
}

cross_sectional_velocity2 = {
    "tag": "v",
    "u_min": 0.5,
    "u_max": 10.0,
    "function": lambda u: u,
    # "title": r"V ($\frac{m}{s}$)",
    "tick_levels": 3,
    "tick_text_levels": 1,
    "scale_type": "manual data",
}

flow_block = {
    "block_type": "type_2",
    "f1_params": hydraulic_flux,
    "f2_params": hydraulic_area,
    "f3_params": cross_sectional_velocity2,
    # "mirror_x": True,
    "isopleth_values": [[0.15, 0.03, "x"]],
}

cross_sectional_velocity1 = {
    "tag": "v",
    "u_min": 0.5,
    "u_max": 10.0,
    "function": lambda u: u,
    "title": r"\Large V ($\frac{m}{s}$)",
    "tick_levels": 3,
    "tick_text_levels": 1,
    "tick_side": "left",
    "title_draw_center": True,
    "title_distance_center": -0.5,
    # "scale_type": "manual_data",
}
stream_slope = {
    "u_min": 1.0,
    "u_max": 150.0,
    "function": lambda u: pow(u / 100.0, 0.5),
    "title": r"\Large S ($\%$)",
    "tick_levels": 3,
    "tick_text_levels": 1,
    "tick_side": "left",
    "title_draw_center": True,
    "title_distance_center": 0.75,
}
hydraulic_radius = {
    "u_min": 1.0,
    "u_max": 10.0,
    "function": lambda u: pow(u, 2.0 / 3.0),
    "title": r"\Large Rh ($m$)",
    "tick_levels": 3,
    "tick_text_levels": 1,
    "tick_side": "right",
    # "title_opposite_tick": False,
    "title_draw_center": True,
    "title_distance_center": -0.75,
}
manning_coeff = {
    "u_min": 0.01,
    "u_max": 1.0,
    "function": lambda u: u,
    "title": r"\Large n",
    "tick_levels": 3,
    "tick_text_levels": 1,
    "tick_side": "right",
    "title_draw_center": True,
    "title_distance_center": 0.75,
    # "title_opposite_tick": False,
}

manning_block = {
    "block_type": "type_4",
    "f1_params": cross_sectional_velocity1,
    "f2_params": hydraulic_radius,
    "f3_params": stream_slope,
    "f4_params": manning_coeff,
    "padding": 0.8,
    "mirror_x": True,
    "isopleth_values": [["x", 5.0, "x", 0.5]],
}


main_params = {
    "filename": outputfile,
    "paper_height": 5.5 * 2.54,
    "paper_width": 11 * 2.54,
    # "make_grid": True,
    "block_params": [flow_block, manning_block],
    "transformations": [("rotate", 0.01), ("scale paper",)],
    "title_str": r"\huge \textbf{Manning formula} for estimating the average velocity of a liquid flowing in an open channel.",
    "title_x": 5.0,
	'title_y':1.5,
    "extra_texts": [
        {
            "x": 22.0,
            "y": 12.0,
            "text": r"\Large $Q = A \cdot V =  \frac{1}{n} \cdot Rh^\frac{2}{3} \cdot \sqrt{S} $ \normalsize \medskip \
			\par Q = Hydraulic flux  \
			\par A = Flow cross-sectional area \
			\par V = Flow velocity \
			\par n = Manning roughness coefficient \
			\par Rh = Hydraulic radius \
			\par S = Channel slope \
			\par \medskip \normalsize \copyright Daniel Boulet (2023)",
            "width": 12.0,
        },
    ],
}
Nomographer(main_params)
