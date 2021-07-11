"""
    vf_calculator.py

    Stub matching nomogram for 80 to 260 MHz range.

    Copyright (C) 2020	Daniel Boulet

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
from pyx import *
pyx.text.set(text.LatexEngine)
sys.path.insert(0, "..")

pyx.text.preamble(r"\usepackage{array}")

scalingFactor = 2
shortest_wavelength = 0.19250
longest_wavelength = 0.77001

stub_length_1 = {
    'u_min': shortest_wavelength,
    'u_max': longest_wavelength,
    'function': lambda u: u**scalingFactor,
    'title': r'Cable 1',
    'tick_levels': 5,
    'tick_text_levels': 4,
    'text_format': r'$%2.2g$m',
    'scale_type': 'linear smart',
    'tick_side': 'left',
}
vel_factor_1 = {
    'u_min': 60,
    'u_max': 90,
    'function': lambda u: (u/100)**scalingFactor,
    'title': r'Cable 1 VF (\%)',
    'tick_levels': 3,
    'text_format': r'$%2.2g$',
    'tick_text_levels': 1,
    'scale_type': 'linear smart',
    'tick_side': 'right',
    'extra_params': [
        {
            'scale_type': 'manual arrow',
            'arrow_length': 0.75,
            'manual_axis_data': {
                66: r'A',
                73: r'B',
                78: r'C',
                80: r'D',
                81: r'E',
                82: r'F',
                84: r'G',
                85: r'H',
            },
            'tick_side': 'left'
        }
    ]
}

stub_length_2 = {
    'u_min': shortest_wavelength,
    'u_max': longest_wavelength,
    'function': lambda u: u**scalingFactor,
    'title': r'Cable 2 length',
    'tick_levels': 5,
    'tick_text_levels': 4,
    'text_format': r'$%2.2g$m',
    'scale_type': 'linear smart',
    'tick_side': 'right',
    'title_x_shift': 0.5,
    'title_rotate_text': True,
}
vel_factor_2 = {
    'u_min': 60,
    'u_max': 90,
    'function': lambda u: (u/100)**scalingFactor,
    'title': r'Cable 2 VF (\%)',
    'tick_levels': 5,
    'tick_text_levels': 4,
    'scale_type': 'linear smart',
    'tick_side': 'left',
    'title_rotate_text':True,
    'title_x_shift': 0.5,
    'extra_params': [
        {
            'scale_type': 'manual arrow',
            'arrow_length': 0.75,
            'manual_axis_data': {
                66: r'A',
                73: r'B',
                78: r'C',
                80: r'D',
                81: r'E',
                82: r'F',
                84: r'G',
                85: r'H',
            },
            'tick_side': 'right'
        }
    ]

}

block_1_params = {
    'block_type': 'type_4',
    'f1_params': stub_length_1,
    'f2_params': vel_factor_1,
    'f3_params': stub_length_2,
    'f4_params': vel_factor_2,
    'isopleth_values': [[0.5, 66, 'x', 85]],
    'reference_color': pyx.color.cmyk.Gray
}

main_params = {
    'filename': 'vf_calculator.pdf',
    'paper_height': 20.0,
    'paper_width': 20.0,
    'block_params': [block_1_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
    'title_box_width':7.0,
    'title_str': r'\LARGE 80--260MHz $\frac{1}{4}\lambda$ Stub Matching Chart \par $\frac{L_1}{VF_1}=\frac{L_2}{VF_2}$',
    'title_x':15.0,
    'title_y': 8.0,
    # 'make_grid': True,
    'extra_texts': [
        {
            'x': 1,
            'y': 19,
            'text': r'\begin{center} \begin{tabular}{| m{6cm} | c | } \hline \bf{Cable Type} & \bf{Label} \\                 \hline RG-6/U PE (Belden 8215) \newline RG-8/U PE (Belden 8237) \newline RG-58/U PE (Belden 9201) \newline RG-59A/U PE (Belden 8241) \newline RG-174 PE (Belden 8216) \newline RG-213/U (Belden 8267) & A (66\%)  \\                  \hline RG-58A/U Foam (Belden 8219) \newline RG-174 Foam (Belden 7805R) & B (73\%) \\            	\hline RG-8/U Foam (Belden 8214) \newline RG-59A/U Foam (Belden 8241F) & C (78\%) \\                 \hline LMR-240UF & D (80\%) \\                 \hline RG-6/U Foam (Belden 9290) & E  (81\%) \\                 \hline RG-8X (Belden 9258) \newline Davis BuryFlex & F (82\%)  \\                 \hline RG-8/U (Belden 9913) \newline RG-11/U Foam HDPE (Beldin 9292) \newline LMR-240 & G (84\%) \\ \hline LMR-400 \newline LMR-400UF & H (85\%) \\ \hline \end{tabular} \end{center}',
            'width': 10.0,
        },
        {
            'x': 11.0,
            'y': 18,
            'text': r'\noindent This chart will calculate the cable length required to substitute the same wavelength stub with another having a different velocity factor. \newline \newline Example: to substitute a 0.5m section of RG-213 requires a 0.644m section of LMR-400. \newline \newline \copyright Daniel Boulet (2020)',
            'width': 9.0,
        },
    ],


}
Nomographer(main_params)
