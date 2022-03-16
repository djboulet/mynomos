"""
    vswr.py

    Low power VSWR calculator

    Copyright (C) 2021  Daniel Boulet

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
import sys,math
# created outputfile name based on script name
outputfile = sys.argv[0].split('.')[0]+'.pdf'

sys.path.insert(0, "..")
from pynomo.nomographer import Nomographer
from pyx import *
text.set(text.LatexEngine)


forward_power = {
    "u_min": 5.0,
    "u_max": 100.0,
    "function": lambda u: 0.5*math.log(u),
    "title": r"Forward power",
	'title_draw_center':True,
	'tick_side':'left',
	'extra_angle':180.0,
	'text_distance_0':1.4,
	'text_distance_1':1.0,
	'text_distance_2':0.8,
	'text_distance_3':0.6,
	'text_distance_4':0.6,
    "tick_levels": 5,
	'title_distance_center':-1.0,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
}

vswr = {
    "u_min": 1.25,
    "u_max": 5.0,
    "function": lambda u: -math.log((u+1)/(u-1)),
	'extra_angle':180.0,
	'text_distance_0':1.4,
	'text_distance_1':1.0,
	'text_distance_2':0.8,
	'text_distance_3':0.6,
	'text_distance_4':0.6,
    "title": r"VSWR",
    "tick_levels": 5,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
}

reflected_power = {
    "u_min": 0.5,
    "u_max": 10.0,
    "function": lambda u: -0.5*math.log(u),
    "title": r"Reflected power",
	'title_distance_center':-1.0,
    "tick_levels": 5,
	'title_draw_center':True,
	'extra_angle':180.0,
	'text_distance_0':1.4,
	'text_distance_1':1.0,
	'text_distance_2':0.8,
	'text_distance_3':0.6,
	'text_distance_4':0.6,
    "tick_text_levels": 4,
    "scale_type": "linear smart",
}

block_1_params = {
    "block_type": "type_1",
    "f1_params": forward_power,
    "f2_params": vswr,
    "f3_params": reflected_power,
    "isopleth_values": [[30.0,2.0,'x'],[20.0,2.0,'x'],[10.0,2.0,'x']],
}

main_params = {
	# 'make_grid':True,
    "filename": outputfile,
    "paper_height": 10.0,
    "paper_width": 25.0,
    "block_params": [block_1_params],
    "transformations": [("rotate", 90.01), ("scale paper",)],
    "title_str": r"\huge VSWR Calculator \medskip \par \small \copyright Daniel Boulet (2021-2022)",
	'title_box_width':10.0,
	'title_y':7.0,
	'title_x':3.0,
	'extra_texts': [
		{

			'text': r'\Large $VSWR = \frac{1+\sqrt{\frac{P_{reflected}}{P_{forward}}}}{1-\sqrt{\frac{P_{reflected}}{P_{forward}}}}$',
			'x': 18.0,
			'y': 7.0,
			'width': 10.0,
		},
	]
}
Nomographer(main_params)
