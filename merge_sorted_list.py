# -*- coding:utf-8 -*-

def merge_sorted_list(heada, headb):
    if not heada and not headb:
        return None
    if not heada:
        return headb
    elif not headb:
        return heada

    ha, hb = heada, headb
    result = []
    while ha and hb:
        if ha.value < hb.value:
            result.append(ha.value)
            ha = ha.next
        else:
            result.append(hb.value)
            hb = hb.next

    while ha:
        result.append(ha.value)
        ha = ha.next
    while hb:
        result.append(hb.value)
        hb = hb.next

    return result
