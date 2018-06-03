
import matplotlib.pyplot as plt


example_tux_orderbook = {"asks":[["0.00000049","776.22230000"],["0.00000050","1643.96964836"],["0.00000051","16802.44436690"],["0.00000052","16028.00000000"],["0.00000053","16026.86792452"],["0.00000054","16028.00000000"],["0.00000055","16028.00000000"],["0.00000056","16278.00000000"],["0.00000057","17529.67274219"],["0.00000058","11278.00000000"],["0.00000059","11278.00000000"],["0.00000060","10501.00000000"],["0.00000061","11802.66900000"],["0.00000062","10434.85698920"],["0.00000063","11345.46031746"],["0.00000064","10251.00000000"],["0.00000065","11278.00000000"],["0.00000066","20251.00000000"],["0.00000067","51028.00000000"],["0.00000068","50438.93650790"],["0.00000069","51855.61594649"],["0.00000070","50251.00000000"],["0.00000071","50398.35294117"],["0.00000072","101025.66900000"],["0.00000073","1248.00000000"],["0.00000074","100251.00000000"],["0.00000075","1251.00000000"],["0.00000076","100251.00000000"],["0.00000077","6028.00000000"],["0.00000078","100251.00000000"],["0.00000079","1251.00000000"],["0.00000080","100502.00000000"],["0.00000081","251.00000000"],["0.00000082","101502.00000000"],["0.00000083","251.00000000"],["0.00000084","1251.00000000"],["0.00000085","100502.00000000"],["0.00000086","502.00000000"],["0.00000087","251.00000000"],["0.00000088","1251.00000000"],["0.00000089","100502.00000000"],["0.00000090","502.00000000"],["0.00000091","251.00000000"],["0.00000092","1502.00000000"],["0.00000093","502.00000000"],["0.00000094","502.00000000"],["0.00000095","502.00000000"],["0.00000096","251.00000000"],["0.00000097","1502.00000000"],["0.00000098","251.00000000"]],
            "bids":[["0.00000046","4372.00000000"],["0.00000045","16278.00000000"],["0.00000044","15501.00000000"],["0.00000043","16278.00000000"],["0.00000042","15977.19047619"],["0.00000041","15501.00000000"],["0.00000040","15000.00000000"],["0.00000039","15777.00000000"],["0.00000038","20777.00000000"],["0.00000037","21000.00000000"],["0.00000036","22000.00000000"],["0.00000035","20000.00000000"],["0.00000034","20000.00000000"],["0.00000033","32971.64455522"],["0.00000032","30000.00000000"],["0.00000031","30000.00000000"],["0.00000030","30000.00000000"],["0.00000029","42000.00000000"],["0.00000028","40000.00000000"],["0.00000027","102000.00000000"],["0.00000026","60000.00000000"],["0.00000025","80437.48000000"],["0.00000024","80000.00000000"],["0.00000023","80000.00000000"],["0.00000022","100000.00000000"],["0.00000021","126190.47619040"],["0.00000020","220500.07777777"],["0.00000019","202631.72777777"],["0.00000018","170000.00000000"],["0.00000017","210000.00000000"],["0.00000016","308413.00000000"],["0.00000015","380400.07777770"],["0.00000014","301000.00000000"],["0.00000013","301000.00000000"],["0.00000012","301000.00000000"],["0.00000011","301000.00000000"],["0.00000010","102238.75555554"],["0.00000009","2000.00000000"],["0.00000008","2000.00000000"],["0.00000007","2000.00000000"],["0.00000006","2000.00000000"],["0.00000005","4187.40000000"],["0.00000004","4000.00000000"],["0.00000003","4000.00000000"],["0.00000002","8000.00000000"],["0.00000001","49372.00000000"]]}


def draw_depth(bidasks, bps=999):
    # bps is how far from market price you want to view,
    # to view 25% in both directions, set bps=.25
    best_bid = max([float(price) for price, amount in bidasks["bids"]])
    best_ask = min([float(price) for price, amount in bidasks["asks"]])
    worst_bid = best_bid * (1 - bps)
    worst_ask = best_ask * (1 + bps)
    filtered_bids = sorted([(float(bid[0]),float(bid[1])) for bid in bidasks["bids"] if float(bid[0]) >= worst_bid], key=lambda x:-x[0])
    filtered_asks = sorted([(float(ask[0]),float(ask[1])) for ask in bidasks["asks"] if float(ask[0]) <= worst_ask], key=lambda x:+x[0])

    bsizeacc = 0
    bhys = []    # bid - horizontal - ys
    bhxmins = [] # bid - horizontal - xmins
    bhxmaxs = [] # ...
    bvxs = []
    bvymins = []
    bvymaxs = []
    asizeacc = 0
    ahys = []
    ahxmins = []
    ahxmaxs = []
    avxs = []
    avymins = []
    avymaxs = []
    
    for (p1, s1), (p2, s2) in zip(filtered_bids, filtered_bids[1:]):
        bvymins.append(bsizeacc)
        if bsizeacc == 0:
            bsizeacc += s1
        bhys.append(bsizeacc)
        bhxmins.append(p2)
        bhxmaxs.append(p1)
        bvxs.append(p2)
        bsizeacc += s2
        bvymaxs.append(bsizeacc)
    
    for (p1, s1), (p2, s2) in zip(filtered_asks, filtered_asks[1:]):
        avymins.append(asizeacc)
        if asizeacc == 0:
            asizeacc += s1
        ahys.append(asizeacc)
        ahxmins.append(p1)
        ahxmaxs.append(p2)
        avxs.append(p2)
        asizeacc += s2
        avymaxs.append(asizeacc)
        
    plt.vlines(bhys[1:], bhxmins[1:], bhxmaxs[1:], color="green")
    plt.hlines(bvxs, bvymins, bvymaxs, color="green")
    plt.vlines(ahys[1:], ahxmins[1:], ahxmaxs[1:], color="red")
    plt.hlines(avxs, avymins, avymaxs, color="red")
        

def visualize_orderbook(orderbook, bps=999):
    plt.figure(figsize=(10,4))
    draw_depth(orderbook, bps=bps)
    plt.grid()
    plt.show()
    
if __name__ == "__main__":
    visualize_orderbook(example_tux_orderbook)
        
