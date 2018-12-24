from pynomo.nomographer import *


fuelflow_para={
    'u_min':10000,
    'u_max':30000,
    'tick_levels':3,
    'text_format':r'$%4.0f$',
    'scale_type':'linear smart',
    'tick_text_levels':1,
    'function':lambda  u:log(u),
    'title':r'Fuel\ flow (lb/hr)',
}

pout_para={
    'u_min':20000,
    'tick_levels':3,
    'text_format':r'$%4.0f$',
    'scale_type':'linear smart',
    'tick_text_levels':1,
    'u_max':40000,
    'function':lambda  u:-log(u),
    'title':r'Power Output (kW)',
}


sfc1_para={
    'tag':'sfc',
    'u_min':0.50,
    'u_max':2.0,
    'text_format':r'$%.3f$',
    'scale_type':'linear smart',
    'tick_levels':3,
    'tick_text_levels':1,
    'function':lambda  u:-log(u),
    'title':r'SFC (lb/kw-h)',
}

sfc2_para={
    'tag':'sfc',
    'u_min':0.50,
    'text_format':r'$%4.0f$',
    'scale_type':'linear smart',
    'u_max':2.0,
    'scale_type':'manual point',
    'function':lambda  u:-log(u),
    'title':r'SFC (lb/kw-h)',
}

heatvalue_para={
    'u_min':18000,
    'u_max':25000,
    'text_format':r'$%4.0f$',
    'tick_levels':3,
    'scale_type':'linear smart',
    'tick_text_levels':1,
    'function':lambda  u:-log(u),
    'title':r'Heat value (BTU/lb)',
}

heatrate_para={
    'u_min':10000,
    'u_max':20000,
    'tick_levels':3,
    'text_format':r'$%4.0f$',
    'scale_type':'linear smart',
    'tick_text_levels':1,
    'function':lambda  u:log(u),
    'title':r'BTU/kW-h',
}


sfc_block={
    'block_type':'type_1',
    'f1_params':fuelflow_para,
    'f2_params':pout_para,
    'f3_params':sfc1_para,
}

hr_block={
    'block_type':'type_1',
    'f1_params':sfc2_para,
    'f2_params':heatvalue_para,
    'f3_params':heatrate_para,
}


# }
# main dictionary to build complete nomogram
main_params={
        # identify the blocks to include in the nomogram (order matters!)
        'block_params':[sfc_block,hr_block], 

        # specify filename and paper size
        'filename':'gasturbine.pdf',
        'paper_height':11.0*2.54,
        'paper_width':8.5*2.54,

        'transformations':[('rotate',0.001),('scale paper',),],
}

# run the script
Nomographer(main_params)
