"""
    air_core_coil.py

	Nomograph to calculate inductance of single layer air coil.  Design
	adapted from Electronics World magazine, August 1962 (page 55).
    Copyright (C) 2022 Daniel Boulet

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


def radius2diameter(r):
    return r * 2.0


def diameter2radius(d):
    return d / 2.0


length_over_diameter = {
    "u_min": 0.1,
    "u_max": 10.0,
    "function": lambda u: np.log(18.0 + 40.0 * u),
    "title": r"$\frac{L}{D}$",
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "log smart",
}

number_of_turns = {
    "u_min": 2.0,
    "u_max": 100.0,
    "function": lambda u: -2.0 * np.log(u),
    "title": r"$N$",
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "log smart",
}

inductance = {
    "u_min": 0.1,
    "u_max": 100.0,
    "function": lambda u: np.log(u),
    "title": r"$\mu H$",
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "log smart",
}


diameter = {
    "u_min": 0.5,
    "u_max": 2.5,
    "function": lambda u: -np.log(u),
    "title": r"$D$",
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "log smart",
}


block_1_params = {
    "block_type": "type_3",
    "width": 20.0,
    "height": 20.0,
    "f_params": [
        length_over_diameter,
        number_of_turns,
        inductance,
        diameter,
    ],
    "reference_padding": 0.1,
    "reference_titles": ["\Huge$\chi$"],
    "isopleth_values": [['x',40,30.0,2.0]],
}

main_params = {
    "filename": "air_core_coil.pdf",
    "paper_width": 8.5 * 2.54,
    "paper_height": 11.0 * 2.54,
    "block_params": [block_1_params],
    "transformations": [("rotate", 0.01), ("scale paper",)],
    "title_str": r"\Huge Single-layer air coil calculator",
    # "make_grid": True,
    "title_y": 27.0,
    "title_x": 2.0,
    "extra_texts": [
        {
            "x": -2.0,
            "y": 4.0,
            "text": r"\noindent Example: \par \noindent A 30 $\mu$H coil wound on a 2 inch form requires 40 turns of wire over a length of 4.4 inches (2.2 $\times$ 2).",
            "width": 7.0,
        },
        {
            "x": 12.0,
            "y": 28.0,
            "text": r"\noindent This nomograph implements the following formula: \par \medskip \noindent $\mu H = \frac{r^2 \times N^2}{9r + 10l}$ \medskip \par \noindent where $r$ is the radius of the coil (in inches), $N$ is the number of turns, $l$ is the length of the coil (in inches).",
            "width": 12.0,
        },
        {
            "x": 12.0,
            "y": 3.0,
            "text": r"\noindent Nomograph to calculate inductance of single layer air coil.  Design adapted from Electronics World magazine, August 1962 (page 55). \par \medskip   \noindent \copyright    Daniel Boulet  2022",
            "width": 12.0,
        },
    ],
}
Nomographer(main_params)
