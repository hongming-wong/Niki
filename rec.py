import time


# destination = name money

# def budget(destinations, minbudget, maxbudget, overall):
#     minbudget = []
#     maxbudget = []
#     while (budget[0] != 'END'):
#         name = budget[0]

#         for i in budget[1:2]:
#             minbudget.append(int(i))

#         for j in budget[2:3]:
#             maxbudget.append(int(j))
           
#         budget = input().split()
    
#     minbudget.sort()
#     maxbudget.sort()
#     overall = []
#     overall.append(minbudget[0])
#     overall.append(maxbudget[0])
    

#     def criteria(destinations, A, B, overall):
        
#         for i in range(len(destinations[A])):
#             integer = int(destinations[A][i])
#             if integer in range(overall[0], overall[1]):
#                 return False
#         for i in range(len(destinations[A])):
#             if integer not in range(overall[0], overall[1]):
#                 return True
#         return False

#     def finaldestination(destinations, overall):
#         result = []
#         for i in destinations:
#             appendI = True
#             for j in destinations:
#                 if i == j:
#                     continue
#                 if (i!=j and criteria(destinations, i, j, overall)):
#                     appendI = False
#                     break
#             if appendI == True:
#                 result.append(i)
        
#         return result

#     return finaldestination(destinations, overall)



class place:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def getTuple(self):
        return self.name, self.budget

# destinations = [place("Tokyo", 10000), place("Hong Kong", 200000), place(Malaysia), 20000]
    

def getRec(budgetList, minbudget):
    time.sleep(2)
    # min = minbudget

    # for i in budgetList:
    #     if i[1] > min:
    #         min = i[1]

    # rec = []
    # for d in destinations:
    #     if d.budget <= min:
    #         rec.appned(d.getTuple())
    
    return """1. Tokyo, Japan\nReason: Tokyo fits the budget for everyone!\nTo start booking: https://book.cathaypacific.com/CathayPacificV3/dyn/air/booking/owdAvail#/!?destination=Tokyo-Japan\n\n2. Seoul, South Korea\nReason: Seoul fits the budget for most people.\nStart booking here: https://book.cathaypacific.com/CathayPacificV3/dyn/air/booking/owdAvail#/!?destination=Seoul-Korea"""
    
