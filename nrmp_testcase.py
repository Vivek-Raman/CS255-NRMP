
def nrmp_testcase (): 
    
    input_5m5w_0 = [
    "man",
    "woman",
    {
        "V": "A B C D E",
        "W": "B C D A E",
        "X": "C D A B E",
        "Y": "D A B C E",
        "Z": "A B C D E",
    }, {
        "A": "W X Y Z V",
        "B": "X Y Z V W",
        "C": "Y Z V W X",
        "D": "Z V W X Y",
        "E": "V W X Y Z",
    }
    ]
    input_5m5w_1 = [
    "man",
    "woman",
    {
        "V": "A B C D E",
        "W": "B A D C E",
        "X": "A B C D E",
        "Y": "B A E C D",
        "Z": "A B C D E",
    }, {
        "A": "W V Y Z X",
        "B": "V W Z X Y",
        "C": "V W Y Z X",
        "D": "W V Z X Y",
        "E": "V W X Y Z",
    }
    ]
    input_5m5w_1 = [
    "man",
    "woman",
    {
        "V": "A B C D E",
        "W": "A C D E B",
        "X": "A D E B C",
        "Y": "A E B C D",
        "Z": "A C D B E",
    }, {
        "A": "V W Y Z X",
        "B": "V W Z X Y",
        "C": "V W Y Z X",
        "D": "V W Z X Y",
        "E": "V W X Y Z",
    }
    ]
    input_5m5w_2 = [
    "man",
    "woman",
    {
        "V": "A B C D E",
        "W": "B A D C E",
        "X": "A B C D E",
        "Y": "B A E C D",
        "Z": "A B C D E",
    }, {
        "A": "W V Y Z X",
        "B": "V W Z X Y",
        "C": "V W Y Z X",
        "D": "W V Z X Y",
        "E": "V W X Y Z",
    }
    ]
    input_5m5w_3 = [
    "man",
    "woman",
    {
        "V": "A B C D E",
        "W": "B A C D E",
        "X": "A B C E D",
        "Y": "B A C E D",
        "Z": "C B A D E",
    }, {
        "A": "X Y Z W V ",
        "B": "Y Z X V W ",
        "C": "Z Y X W V ",
        "D": "Y Z X V W ",
        "E": "Z X Y W V ",
    }
    ]
    input_5m5w = [
    "man",
    "woman",
    {
        "V": "B A D E C",
        "W": "D B A C E",
        "X": "B E C D A",
        "Y": "A D C B E",
        "Z": "B D A E C",
    }, {
        "A": "Z V W Y X",
        "B": "X W Y V Z",
        "C": "W X Y Z V",
        "D": "V Z Y X W",
        "E": "Y W Z X V",
    }
    ]
    spec = [
    "hospital",                        # names of the group that recruit or propose to
    "students",                        # names of the group that was recruited or proposed to 
    {
    "A":"1 2  3 4 5   6  7  8  9  10 ",      # Hospital's preference list of its applicants
    "B":"4 5  7 6 2 9 10 3 8  1",
    "C":"1 10 4 8 6 2  9 3 5  7",
    "D":"1 2  3 4 5   6  7  8  9  10 ",
    "E":"5 1  3 6 9 8 10 4 2  7",
    }
    ,
    {                               # Student's preference list of the hospitals
    "1":  "A B  C D E",
    "2":  "C B E A D",
    "3":  "A E D B C",
    "4":  "E A D C B",
    "5":  "A B E D C",
    "6":  "A B  C D E",
    "7":  "E A D C B",
    "8":  "A D E C B",
    "9":  "C D E A B",
    "10": "C E A B D"
    }
    ]

    input_nrmp = [
    "hospital",     # names of the group that recruit or propose to
    "students",     # names of the group that was recruited or proposed to 
    { 				# Hospital's preference list of its applicants
    "A":"3 1  9 8 7 4  6 2 5 10",      
    "B":"4 5  7 6 2 9 10 3 8  1",
    "C":"1 10 4 8 6 2  9 3 5  7",
    "D":"3 1  9 8 7 4  6 2 5 10",
    "E":"5 1  3 6 9 8 10 4 2  7",
    } , {                               
    # Student's preference list of the hospitals
    "1":  "A D E B C",
    "2":  "C B E A D",
    "3":  "A E D B C",
    "4":  "E A D C B",
    "5":  "A B E D C",
    "6":  "A D C E B",
    "7":  "E A D C B",
    "8":  "A D E C B",
    "9":  "C D E A B",
    "10": "C E A B D"
    }
    ]
    input_nrmp2 = [
    "hospital",     # names of the group that recruit or propose to
    "students",     # names of the group that was recruited or proposed to 
    { 				# Hospital's preference list of its applicants
    "A":"3 1  9 8 7 4  6 2 5 10",      
    "B":"4 5  7 6 2 9 10 3 8  1",
    "C":"1 10 4 8 6 2  9 3 5  7",
    "D":"8 1  9 5 7 4  6 2 3 10",
    "E":"5 1  3 6 9 8 10 4 2  7",
    } , {                               
    # Student's preference list of the hospitals
    "1":  "A D E B C",
    "2":  "C B E A D",
    "3":  "A E D B C",
    "4":  "E A D C B",
    "5":  "A B E D C",
    "6":  "A D C E B",
    "7":  "E A D C B",
    "8":  "A D E C B",
    "9":  "C D E A B",
    "10": "C E A B D"
    }
    ] 

    input_4m4w = [
    "man",
    "woman",
    {
    "m1": "w3  w1   w2 w4",
    "m2": "w1  w3   w4 w2",
    "m3": "w3  w1   w2 w4",
    "m4": "w3  w1   w4 w2",
    }, {
    "w1": "m1  m2  m3  m4",
    "w2": "m1  m2  m3  m4",
    "w3": "m2  m1  m3  m4",           
    "w4": "m2  m1  m3  m4",          
    }
    ]

    input_3m3w = [
    "man",
    "woman",
    {
    "m1": "w3  w1   w2",
    "m2": "w1  w3   w2",
    "m3": "w3  w1   w2",
    }, {
    "w1": "m1 m2 m3",
    "w2": "m1 m2 m3",
    "w3": "m2 m1 m3",           # "w3": "m2 m3 m1"
    }    
    ]
    inputs = (spec, input_nrmp, input_3m3w, input_4m4w, input_5m5w, input_5m5w_0, input_5m5w_1,input_5m5w_2,input_5m5w_3,input_nrmp2) 
    return inputs
