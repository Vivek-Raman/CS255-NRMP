import nrmp 

def answerKey(): 
    spec_0 =  {} 
    spec_1 =  {'A': ['1'], 'B': ['4'], 'C': ['10'], 'D': ['2'], 'E': ['5']} 
    spec_2 =  {'A': ['1', '2'], 'B': ['5', '7'], 'C': ['10', '8'], 'D': ['4', '6'], 'E': ['3', '9'] } 
    spec_3 =  {'A': ['1', '3', '5'], 'B': ['6'], 'C': ['10', '2', '9'], 'D': ['8'], 'E': ['4', '7']} 
    spec_4 =  {'A': ['1', '3', '5', '6'], 'B': [], 'C': ['10', '2', '9'], 'D': ['8'], 'E': ['4', '7']} 
    output_spec = [ spec_0, spec_1, spec_2, spec_3,  spec_4, ]


    output_nrmp_0 = {}
    output_nrmp_1 = {'A': ['3'], 'B': ['4'], 'C': ['10'], 'D': ['1'], 'E': ['5']} # quota = 1
    output_nrmp_2 = {'A': ['3', '1'], 'B': ['5', '7'], 'C': ['10', '6'], 'D': ['9', '8'], 'E': ['4', '2'] } 
    output_nrmp_3 = {'A': ['3', '1', '8'], 'B': ['5'], 'C': ['10', '2', '9'], 'D': ['6'], 'E': ['4', '7']}
    output_nrmp_4 = {'A': ['3', '1', '8', '6'], 'B': ['5'], 'C': ['10', '2', '9'], 'D': [], 'E': ['4', '7']} 

    output_nrmp = [ 
            output_nrmp_0,
            output_nrmp_1,           
            output_nrmp_2,      
            output_nrmp_3,      
            output_nrmp_4,
        ]

    output_3m3w = [ 
    {}, 
    {'m1': ['w3'], 'm2': ['w1'], 'm3': ['w2']},
    {'m1': ['w1', 'w2'], 'm2': ['w3'], 'm3': []}
    ]

    output_4m4w = [ 
    {}, 
    {'m1': ['w3'], 'm2': ['w1'], 'm3': ['w2'], 'm4': ['w4']},
    {'m1': ['w1', 'w2'], 'm2': ['w3', 'w4'], 'm3': [], 'm4': []}
    ]


    output_5m5w = [ 
    {}, 
    {'V': ['A'], 'W': ['C'], 'X': ['B'], 'Y': ['E'], 'Z': ['D']},
    {'V': ['D'], 'W': ['C'], 'X': ['B'], 'Y': ['E'], 'Z': ['A']},
    {'V': ['D'], 'W': ['C'], 'X': ['B'], 'Y': ['E'], 'Z': ['A']},
    {'V': ['D'], 'W': ['C'], 'X': ['B'], 'Y': ['E'], 'Z': ['A']},
    ]

    output_5m5w_0 = [ 
    {}, 
    {'V': ['E'], 'W': ['A'], 'X': ['B'], 'Y': ['C'], 'Z': ['D']},
    {'V': ['E'], 'W': ['A'], 'X': ['B'], 'Y': ['C'], 'Z': ['D']},
    {'V': ['E'], 'W': ['A'], 'X': ['B'], 'Y': ['C'], 'Z': ['D']},
    {'V': ['E'], 'W': ['A'], 'X': ['B'], 'Y': ['C'], 'Z': ['D']},
    ]

    output_5m5w_1 = [ 
    {}, 
    {'V': ['A'], 'W': ['C'], 'X': ['E'], 'Y': ['B'], 'Z': ['D']},
    {'V': ['A', 'B'], 'W': ['C', 'D'], 'X': ['E'], 'Y': [], 'Z': []},
    {'V': ['A', 'B', 'C'], 'W': ['D', 'E'], 'X': [], 'Y': [], 'Z': []},
    {'V': ['A', 'B', 'C', 'D'], 'W': ['E'], 'X': [], 'Y': [], 'Z': []}
    ]

    output_5m5w_2 = [ 
    {}, 
    {'V': ['A'], 'W': ['B'], 'X': ['D'], 'Y': ['E'], 'Z': ['C']},
    {'V': ['B', 'C'], 'W': ['A', 'D'], 'X': ['E'], 'Y': [], 'Z': []},
    {'V': ['B', 'C', 'E'], 'W': ['A', 'D'], 'X': [], 'Y': [], 'Z': []},
    {'V': ['B', 'C', 'E'], 'W': ['A', 'D'], 'X': [], 'Y': [], 'Z': []},
    ]

    output_5m5w_3 = [ 
    {}, 
    {'V': ['D'], 'W': ['E'], 'X': ['A'], 'Y': ['B'], 'Z': ['C']},
    {'V': [], 'W': [], 'X': ['A'], 'Y': ['B', 'D'], 'Z': ['C', 'E']},
    {'V': [], 'W': [], 'X': ['A'], 'Y': ['B', 'D'], 'Z': ['C', 'E']},
    {'V': [], 'W': [], 'X': ['A'], 'Y': ['B', 'D'], 'Z': ['C', 'E']},
    ]

    output_nrmp_2 = [ 
    {},
    {'A': ['3'], 'B': ['4'], 'C': ['1'], 'D': ['8'], 'E': ['5']},
    {'A': ['3', '1'], 'B': ['5', '7'], 'C': ['10', '6'], 'D': ['8', '9'], 'E': ['4', '2']},
    {'A': ['3', '1', '8'], 'B': ['5'], 'C': ['10', '2', '9'], 'D': ['6'], 'E': ['4', '7']},
    {'A': ['3', '1', '8', '6'], 'B': ['5'], 'C': ['10', '2', '9'], 'D': [], 'E': ['4', '7']},
    ]

    outputs = ( output_spec, output_nrmp, output_3m3w, output_4m4w, output_5m5w, output_5m5w_0,output_5m5w_1, output_5m5w_2, output_5m5w_3, output_nrmp_2)
    return outputs
