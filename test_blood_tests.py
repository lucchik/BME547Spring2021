def test_analyze_HDL():
    #The following code works but is not optimal coz once an assertion fails
    #the code won't execute the remaining code
    '''
    from blood_tests import analyze_HDL
    normal = analyze_HDL(90)
    assert(normal=="Normal")
    bLow = analyze_HDL(55)
    assert(bLow=="Borderline Low")
    low = analyze_HDL(25)
    assert(low=="Low")
    '''

def test_analyze_HDL_Normal():
    from blood_tests import analyze_HDL
    normal = analyze_HDL(90)
    assert(normal=="Normal")

def test_analyze_HDL_bLow():
    from blood_tests import analyze_HDL
    bLow = analyze_HDL(55)
    assert(bLow=="Borderline Low")

def test_analyze_HDL_Low():
    from blood_tests import analyze_HDL
    low = analyze_HDL(25)
    assert(low=="Low")
