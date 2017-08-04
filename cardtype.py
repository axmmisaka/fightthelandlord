def cardtype(cards):
        if len(cards) == 1:
                return "dan"
        if len(cards) == 2:
                if cards[0] == 16 and cards[1] == 17:
                        return "wangzha"
                elif cards[0] != cards[1]:
                        return "buxing"
                elif cards[0] == cards[1]:
                        return "duizi",cards[0]
        if len(cards) == 3:
                if cards[0] == cards[1] == cards[2]:
                        return "san",cards[0]
                else:
                        return "buxing"
        if len(cards) == 4:
                if cards[0] == cards[1] == cards[2] == cards[3]:
                        return "zhadan",cards[0]
                elif cards[0] == cards[1] == cards[2]:
                        return "sandai1",cards[0],cards[1]
                else:
                        return "buxing"
        if len(cards) == 5:
                if cards[0] == cards[1] == cards[2] and cards[3] == cards[4]:
                        return "sandai2",cards[0],cards[3]
                elif cards[0] == cards[1] - 1 == cards[2] - 2 == cards[3] - 3 == cards[4] - 4:
                        return "shunzi",(cards[0],5)
                else:
                        return "buxing"
        if len(cards) == 6:
            if cards[0] == cards[1] == cards[2] == cards[3]:
                if cards[4] != cards[5]:
                    return "sidai2",cards[0],cards[4]
                else:
                        return "buxing"
            elif cards[0] == cards[1] == cards[2] and cards[3] == cards[4] == cards[5]:
                        return "feiji",(cards[0],2)
            elif cards[0] == cards[1] - 1 == cards[2] - 2 == cards[3] - 3 == cards[4] - 4 == cards[5] - 5:
                        return "shunzi",(cards[0],6)
            elif cards[0] == cards[1] and cards[2] == cards[3] and cards[4] == cards[5]:
                        return "liandui",(cards[0],3)
            else:
                        return "buxing"
        if len(cards) >= 7:
                i = 0
                while i <= len(cards) - 2:
                        if cards[0] != cards[i + 1] - (i + 1):
                                break
                        i += 1
                if i == len(cards) - 1:         
                        return "shunzi" ,cards[0], len(cards)
                
                
                i = 0
                while i <= len(cards) - 2:
                        if cards[i] != cards[i + 1]:
                                break
                        i += 2
                if i == len(cards):
                    i = 1
                    while i <= len(cards) - 2:
                        if cards[i + 1] != cards[i] + 1:
                            break
                        i += 2
                    if i+1 == len(cards):
                        return "liandui" ,cards[0], int(len(cards) / 2)
                lst = cards[:]
                r = 0
                
                
                for i in range(0,int(len(cards)/3)):
                        if lst[0] == lst[1] == lst[2] and lst[0] == cards[0]+r:
                                lst = lst[3:]
                                r += 1
                        else:
                                break
                if r == 1 or r == 0:
                        return "buxing"
                else:
                        if len(lst) ==0:
                                return r ,"fei"
                        if len(lst) == r:
                                for i in range(0,len(lst)):
                                        if lst[i] != lst[1 + i]:
                                                return r,"fei dai",lst
                                        else:
                                                return "buxing"
                        if len(lst) == 2 * r:
                                lstt = lst[:]
                                p = 0
                                for i in range(0,r):
                                        if lstt[0] == lstt[1]:
                                                lstt = lstt[2:]
                                                p += 1
                                        else:
                                                break
                                if p == r:
                                        return r ,"fei dai",lst
                return "buxing"
