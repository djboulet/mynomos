import sys
sys.path.insert(0, "..")
from pynomo.nomographer import *


resistors10to100={
    10:'10',    11:'11',    12:'12',    13:'13',    15:'15',    16:'16',    18:'18',
    20:'20',    22:'22',    24:'24',    27:'27',    30:'30',    33:'33',    36:'36',
    39:'39',    43:'43',    47:'47',    51:'51',    56:'56',    62:'62',    68:'68',
    75:'75',    82:'82',    91:'91',    100:'100',
}

resistors1to100={
    1.0:'1.0',    1.1:'1.1',    1.2:'1.2',    1.3:'1.3',    1.5:'1.5',    1.6:'1.6',    1.8:'1.8',    2.0:'2.0',
    2.2:'2.2',    2.4:'2.4',    2.7:'2.7',    3.0:'3.0',    3.3:'3.3',    3.6:'3.6',    3.9:'3.9',    4.3:'4.3',
    4.7:'4.7',    5.1:'5.1',    5.6:'5.6',    6.2:'6.2',    6.8:'6.8',    7.5:'7.5',    8.2:'8.2',    9.1:'9.1',
    10:'10',    11:'11',    12:'12',    13:'13',    15:'15',    16:'16',    18:'18',    20:'20',    22:'22',
    24:'24',    27:'27',    30:'30',    33:'33',    36:'36',    39:'39',    43:'43',    47:'47',    51:'51',
    56:'56',    62:'62',    68:'68',    75:'75',    82:'82',    91:'91',    100:'100',
}


"""
resistance divider
"""

u1_params = {
    'u_min': 10.0,
    'u_max': 100.0,
    'g': lambda u: 1,
    'f': lambda u: u,
    'h': lambda u: 1,
    'scale_type':'manual line',
    'manual_axis_data':resistors10to100,
    'grid': False,
    'tick_side': 'left',
    'title': r'$R_a$',
    'title_draw_center':True,
}


u2_params = {
    'tag': 'ratio',
    'u_min': 0.2,
    'u_max': 0.65,
    'g': lambda u: u,
    'f': lambda u: 0,
    'h': lambda u: 1.0,
    'scale_type':'manual point',
    'grid': False,

}


u3_params = {
    'u_min': 10.0,
    'u_max': 100.0,
    'scale_type': 'linear smart',
    'g': lambda u: 0,
    'f': lambda u: -u,
    'h': lambda u: 1,
    'scale_type':'manual line',
    'manual_axis_data':resistors10to100,
    'grid': False,
    'title_draw_center':True,
    'title': r'$R_b$',
}

"""
voltage ratios
"""

v1_params = {
    'function': lambda u: (u),
    'u_min': 3.0,
    'u_max': 5.5,
    'tick_text_levels': 1,
    'scale_type': 'linear smart',
    'tick_side': 'left',
    'title': r'$V_{out}$',

    'extra_params': [
        {
            'scale_type': 'manual arrow',
            'tick_side':'right',
            'manual_axis_data': {3.3: r'$3.3V$',
                                 5.0: r'$5.0V$'},
            'arrow_color': color.cmyk.Sepia,
            'arrow_length': 2.0,
            'text_color': color.cmyk.Sepia,
        }
    ]
}


v2_params = {
    'u_min': 8.0,
    'u_max': 15.0,
    'function': lambda u: (u),
    'scale_type': 'linear smart',
    'title': r'$V_{in}$',
    'tick_side':'left',

}

v3_params = {
    'tag': 'ratio',
    'u_min': 0.2,
    'u_max': 0.65,
    'function': lambda u: (u),
    'reference':True,
    'title':r'$ratio$',

}



block1_params = {
    'block_type': 'type_9',
    'f1_params': u1_params,
    'f2_params': u2_params,
    'f3_params': u3_params,
    
    'transform_ini': False,
    'isopleth_values':[[47,'x','y'],[47,'x','y']]
}


block2_params = {
    'block_type': 'type_2',
    'f1_params': v1_params,
    'f2_params': v2_params,
    'f3_params': v3_params,
    'mirror_y': True,
    'isopleth_values':[[3.3,15,'x'],[5.0,8.0,'x']]
}

"""
main parameters
"""

main_params = {
    'paper_height':30,
    'paper_width':30,
    'filename': 'newvoltdiv.pdf',
    'block_params': [block1_params, block2_params],
    'transformations': [('rotate', 0.01), ('scale paper',)],
}

Nomographer(main_params)
