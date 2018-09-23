import itertools
No_Q=int(input("Please enter the number of Queens : "))
board=list(range(No_Q))
avail_posn=itertools.permutations(board)
sol_list=[]
for i in avail_posn:
        set1=set()
        set2=set()
        for j in range(No_Q):
                set1.add(i[j]+j)
                set2.add(i[j]-j)
        if len(set1) == len(set2) == No_Q :
                sol_list.append(i)
                 
print("Number of solutions : " ,len(sol_list))
#print(sol_list)

import numpy as np
board_array=np.array(np.arange(No_Q*No_Q), dtype=str).reshape(No_Q,No_Q)
#print(board_array)
for k in sol_list:
        board_array[:]="|_|"
        for p in range(No_Q):
                board_array[(k[p],p)]="|Q|"
        print(f"\nSolution Number {sol_list.index(k)+1}")# = {k}")
        for l in range(No_Q):
                print(''.join(board_array[l,:]))
        if  sol_list.index(k) + 1 == len(sol_list) :
                print("\nAll solutions shown.")
                break
        next=input("\nDo you want to see the next Solution? (Y/N) : ")
        if next != "Y":
                print("Exiting the process.")
                break
