from pynomo.nomographer import *

# sets start and end of "pounds" scale
lbStart = 2.0
lbEnd = 8.0

# specifies parameters for pounds scale
lb_para={
        # this tag ensures that the lb scale and kg scale are horizontally aligned
        'tag':'A',

        # minimum and maximum values to be plotted
        'u_min':lbStart,
        'u_max':lbEnd,
        
        # specify a 1 to 1 relationship between the values and where they are plotted
        'function':lambda u:u,
        
        # three levels of ticks but only one level are labelled
        'tick_levels':3,        
        'tick_text_levels':1,
        
        # set title and shift it uyp byb 1cm
        'title':r'$Weight$',    
        'title_y_shift':1.0,
        
        # add extra title information
        'extra_titles':[        
                {
                        'text':r'\small $lbs$',
                        'dy':0.5,
                        'dx':-0.5,
                }
        ]
}

# sepcifies parameters for a kilogram scale
kg_para={
        # this tag ensures that the lb scale and kg scale are horizontally aligned
        'tag':'A',
        
        # minimum and maximum values are converted to kilograms
        'u_min':lbStart/2.2,
        'u_max':lbEnd/2.2,
        
        # specify a 1 to 1 relationship between the values and how they are plotted
        'function':lambda u:u,
        
        # however, we need to align the length and position with the pounds scale (1 kg plotted next to 2.2lb linearly)
        'align_func':lambda u:u*2.2,
        
        # two levels of ticks but only one level is labelled
        'tick_levels':2,
        'tick_text_levels':1,
        
        # force the ticks to be plotted on the left
        'tick_side':'left',     
        
        # set the title and shift it up and left by 0.5 cm
        'title':r'\small $kgs$',         
        'title_x_shift':-0.5,
        'title_y_shift':0.5
}

# specifies parameters for the cooking rate scale
rate_para = {
        # minimum and maximum cooking rates
        'u_min':15,
        'u_max':30,
        
        # specify a one-to-one relationship between the value and the scale length
        'function':lambda u:u,
        
        # manually assign points to the scale (don't draw a line)
        'scale_type':'manual point',
        
        # include the dictionary inside the parameter settings
        'manual_axis_data': {
            15.0: r'15 \small $min/lb$',
            20.0: r'20 \small $min/lb$',
            25.0: r'25 \small $min/lb$',
            30.0: r'30 \small $min/lb$'
        },
        
        # add a few extra parameters to the tick marks
        'extra_params': [{
                # include the dictionary inside the parameter settings
                'manual_axis_data': {
                        0.37:''
                },
                # move the ticks to the left side
                'tick_side':'left',
        }]
}

# create an empty dictionary to store hh:mm tick values
timedict = {}

# set possible values of time from 30 upto and including 240 minutes in 10 minute steps
timevalue = range(30,241,10)    

# calculate hours and minutes and insert those values in the dictonary
# the number of minutes is the "key" and the hh:mm formatted value is the label
for n in timevalue:
        h = int(n/60.0)         
        m = n%60                
        timedict[n] = "%02d:%02d"%(h,m)

# specify parameters for cooking time
time_para = {
        # minimum and maximum cook times
        'u_min':30,             
        'u_max':240,

        # specify a one-to-one relationship between the value and the scale length
        'function':lambda u:u,

        # create a manually defined scale specified by the contents of the timedict dictionary
        'scale_type':'manual line', 

        # manual axis parameters and a new title
        'manual_axis_data':timedict,

        # include title information and position it correctly
        'title':r'$Cook\ time$',        
        'title_y_shift':1.0,
        'extra_titles':[
                {
                        'dx':-1.0,
                        'text':r'\small $hh:mm$',
                        'dy':0.5,
                }
        ]

}

# create a type 8 block to plot kg alongside the lbs scale
kg_block={                      
         'block_type':'type_8',
            'f_params':kg_para,
            'isopleth_values':[['x']],
         }

# create a type 2 block to tie together weight, cook time and cooking rate
cooktime_block={
        # type 2 (u1 = u2 x u3)
        'block_type':'type_2', 
        'f1_params':time_para,  
        'f2_params':rate_para,
        'f3_params':lb_para,
        
        # flip nomogram so that weight is on the right hand side
        # and flip vertically so greater weights are at the top
        'mirror_x':True,        
        'mirror_y':True,
        
        # draw an isopleth
        'isopleth_values':[[110,20,'x']],
}

# main dictionary to build complete nomogram
main_params={
        # identify the blocks to include in the nomogram (order matters!)
        'block_params':[cooktime_block,kg_block], 

        # specify filename and paper size
        'filename':'cook.pdf',
        'paper_height':11.0*2.54,
        'paper_width':8.5*2.54,

        # add a title and transform slightly
        'title_str':r'\Huge $Roasting\ Chart$',
        'transformations':[('rotate',0.001),('scale paper',)],
}

# run the script
Nomographer(main_params)
