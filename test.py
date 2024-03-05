import random
import kps9566
import kps9566.kps9566map
import kps9566.compat_map

ascii = [chr(i) for i in range(0x20, 0x7f)]

kpscjks ={}
for k, v in kps9566.compat_map.CJK_COMPAT_MAP.items():
    if v in kps9566.kps9566map.KPS9566MAP:
        kpscjks[k]=v

for i in range(1000):
    randomstr=''.join([random.choice(kps9566.kps9566map.KPS9566MAP+ascii+list(kps9566.kps9566map.KPS9566ALTERNATIVES.keys())+list(kpscjks.values())) for _ in range(10)])
    #print(randomstr)
    data=randomstr.encode('kps9566')
    #print([hex(x) for x in data])
    decodedstr=data.decode('kps9566')
    #print(decodedstr)
    for k, v in list(kps9566.compat_map.CJK_COMPAT_MAP.items())+list(kps9566.kps9566map.KPS9566ALTERNATIVES.items()):
        randomstr=randomstr.replace(k, v)
    assert randomstr==decodedstr