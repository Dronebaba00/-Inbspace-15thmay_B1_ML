## String
S=input('Enter String :- ')
Cal={i:S.count(i) for i in set(S)}
print('All Alphabtes',Cal)
D=str(dict(Cal))
Len=len(Cal)
Val=list(Cal.values())
Max=max(Val)
New = [Max-Val[i] for i in range (Len)]

if (New.count(0)==Len or New.count(0)==1):
    print("My string")
else:
    print("Not my string")
