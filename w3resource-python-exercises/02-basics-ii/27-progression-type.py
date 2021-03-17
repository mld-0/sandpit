import itertools
def ap_gp_sequence(values):
    is_gp = True
    is_ap = True
    ratio_previous = None
    delta_previous = None
    delta = None
    ratio = None
    if len(values) <= 1:
        is_gp = False
        is_ap = False
    for n in range(0, len(values)-1):
        delta_previous = delta
        delta = values[n+1] - values[n]
        ratio_previous = ratio
        try:
            ratio = values[n+1] / values[n]
        except ZeroDivisionError:
            ratio = None
        if (delta == 0):
            is_ap = False
        if (ratio == 0) or (values[n+1] == 0 and values[n] == 0):
            is_gp = False
        if (delta != delta_previous) and ((not delta is None) and (not delta_previous is None)):
            is_ap = False
        if (ratio != ratio_previous) and ((not ratio is None) and (not ratio_previous is None)):
            is_gp = False
        if (not ratio_previous is None) and (ratio is None):
            is_gp = False
    next_num = None
    if (is_ap):
        print("AP Sequence, ", end='')
        next_num = values[-1] + delta
    elif (is_gp):
        print("GP Sequence, ", end='')
        next_num = values[-1] * ratio
    else:
        print("Invalid Sequence, ", end='')
    print("Next num: %s" % next_num)

ap_gp_sequence([1,2,3])
ap_gp_sequence([2,6,18])
ap_gp_sequence([0,0,0])
