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



u_para={
    'u_min':10,
    'u_max':100,
    'function':lambda  u:u,
    'scale_type':'manual line',
    'manual_axis_data':resistors10to100,
    'tick_side':'left',
    'title':r'$R_a$',
}

v_para={
    'tag':'ratio',
    'u_min':1/11.0,
    'u_max':10.0/11.0,
    'scale_type':'linear smart',
    'function':lambda  u:-1.0/u,
    'title':r'$ratio$',
}

w_para={
    'u_min':1,
    'u_max':100,
    'scale_type':'manual line',
    'manual_axis_data':resistors1to100,
    'function_3':lambda  u:u,
    'function_4':lambda  u:u,
    'title':r'$R_b$',
}



va_para={
    'u_min':3,
    'u_max':6,
    'scale_type':'manual point',
    'manual_axis_data':{
        3.3:r'$V_{out} = 3.3V$',
        5.0:r'$V_{out} = 5.0V$',
    },
    'function':lambda  u:-u,
    # add a few extra parameters to the tick marks
    'extra_params': [{
            # include the dictionary inside the parameter settings
            'manual_axis_data': {
                5*1.02:r'2\%',
                5*1.05:r'5\%',
                5/1.02:r'2\%',
                5/1.05:r'5\%',
                3.3*1.02:r'2\%',
                3.3*1.05:r'5\%',
                3.3/1.02:r'2\%',
                3.3/1.05:r'5\%',
            },
            # move the ticks to the left side
            'tick_side':'left',
    }],

}

vb_para={
    'u_min':8,
    'u_max':24,
    'scale_type':'linear smart',
    'function':lambda  u:u,
    'title':r'$V_{in}$',
}


vr_para={
    'tag':'ratio',
    'scale_type':'manual point',

    # 'scale_type':'linear smart',
    'u_min':1/11.0,
    'u_max':10.0/11.0,
    'function':lambda  u:-1.0/u,
    'align_func':lambda u:u,
}

type10_block={
    'block_type':'type_10',
    'f1_params':u_para,
    'f2_params':v_para,
    'f3_params':w_para,
    'isopleth_values':[[68,5.0/15.0,'x']],
    
}


type2_block={
    'block_type':'type_2',
    'f1_params':vb_para,
    'f2_params':va_para,
    'f3_params':vr_para,
    'isopleth_values':[[15,5,'x']]
}

type8_block={
         'block_type':'type_8',
            'f_params':vr_para,
}
# }
# main dictionary to build complete nomogram
main_params={
        # identify the blocks to include in the nomogram (order matters!)
        'block_params':[type10_block,type2_block], 

        # specify filename and paper size
        'filename':'voltage_divider.pdf',
        'paper_height':11.0*2.54,
        'paper_width':8.5*2.54,

        # add a title and transform slightly
        'title_str':r'\Large $V_{out} = V_{in} \times R_a \div (R_a + R_b)$',
        'title_x':17.0,
        'title_y':5.0,
        # 'title_box_width':15,
        'transformations':[('rotate',0.001),('scale paper',),],
}

# run the script
Nomographer(main_params)
