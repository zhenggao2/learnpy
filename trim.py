# -*- encoding: utf-8 -*-
def trim(s):
    ns_front = 0
    while ns_front < len(s):
        if s[ns_front] == ' ':
            ns_front += 1
        else:
            break
    if ns_front == len(s)-1:
        return ''

    ns_tail = len(s)-1
    while ns_tail >= 0:
        if s[ns_tail] == ' ':
            ns_tail -= 1
        else:
            break

    return s[ns_front:ns_tail+1]

