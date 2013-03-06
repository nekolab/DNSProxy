__DEBUG__ = True

DEBUG_FILTER=''.join([chr(x) if len(repr(chr(x))) == 3 else '.' for x in xrange(256)])

def debug_hexdump(src, width=16):
    result=[]
    if src is None: return result
    for i in xrange(0, len(src), width):
        s = src[i:i+width]
        hexa = ' '.join(["%02X"%ord(x) for x in s])
        printable = s.translate(DEBUG_FILTER)
        hexa += (47 - len(hexa)) * " "
        result.append("%04Xh  %s  %s\n" % (i, hexa, printable))
    return ''.join(result)
