n=[3, 0, 6, 5, 0, 8, 4, 0, 0,5, 2, 0, 0, 0, 0, 0, 0, 0,0, 8, 7, 0, 0, 0, 0, 3, 1,0, 0, 3, 0, 1, 0, 0, 8, 0,9, 0, 0, 8, 6, 3, 0, 0, 5,0, 5, 0, 0, 9, 0, 6, 0, 0,1, 3, 0, 0, 0, 0, 2, 5, 0,0, 0, 0, 0, 0, 0, 0, 7, 4,0, 0, 5, 2, 0, 6, 3, 0, 0 ]
# n=[0,1,0,0,0,0,0,0,0,5,2,0,0,8,0,0,0,4,3,0,0,0,4,0,1,2,0,0,0,2,0,1,0,0,0,0,0,9,0,0,0,0,0,4,0,0,0,0,5,9,3,8,7,0,0,8,0,0,6,0,0,0,9,2,0,9,0,0,0,0,6,0,1,0,0,9,0,0,0,0,7]
import numpy as np
# for i in range(len(n)):
#     print(n[i],end=" ")

z=[]
# y=[]
a=np.array([n[0:9],n[9:18],n[18:27],n[27:36],n[36:45],n[45:54],n[54:63],n[63:72],n[72:81]])
# j=0
# k=0

for i in range(len(a)):
    result = np.where(a[i] == 0)[0]
    for j in range(len(result)):
        z.append([i,result[j]])
# i=0
# j=0
# for i in range(len(n)):
    
#     if(k<=8):
#         # a[j].append(n[i])
#         if(n[i]==0):
#             z.append([j,k])
#         k=k+1
#     else:
#         k=0
#         j=j+1
#         # a[j].append(n[i])
#         if(n[i]==0):
#             z.append([j,k])
#         k=k+1

# print("y")
# print(y)
# print("z")
# print(z)

# for i in range(9):
#     for j in range(9):
#         print(str(a[i][j]),end=" ")
#     print("")
print("=====================")


def isValid(n,i,j):
    # temp_row=[]
    # temp_col=[]
    # temp_sq=[]

    # valid=0

    for cnt in range(9):
        # print(cnt)
        # print(str(i)+" , "+str(cnt))
        # print(a[i][cnt])
        # temp_row.append(a[i][cnt])
        if(a[i][cnt]==n):
            return 0

    # try:
    #     if(temp_row.index(n)>=0):
    #         return 0
    # except ValueError:
    #     pass

    for cnt in range(9):
        # print(str(cnt)+" , "+str(j))
        # print(a[cnt][j])
        # temp_col.append(a[cnt][j])
        if(a[cnt][j]==n):
            return 0
    
    # try:
    #     if(temp_col.index(n)>=0):
    #         return 0
    # except ValueError:
    #     pass

    temp_i_start=(0) if (i<=2 and i>=0) else ( (3) if (i<=5 and i>=3) else (6) )
    temp_i_end=temp_i_start+3
    temp_j_start= (0) if (j<=2 and j>=0) else ( (3) if (j<=5 and j>=3) else (6) )
    temp_j_end=temp_j_start+3 

    for cnt_i in range(temp_i_start,temp_i_end):
        for cnt_j in range(temp_j_start,temp_j_end):
            # print(str(cnt_i)+" , "+str(cnt_j))
            # temp_sq.append(a[cnt_i][cnt_j])
            if(a[cnt_i][cnt_j]==n):
                return 0
            

    # try:
    #     if(temp_sq.index(n)>=0):
    #         return 0
    # except ValueError:
    #     pass

    # print("num="+str(n)+" @ "+str(i)+" , "+str(j))
    # print("temp row"+str(temp_row))
    # print("temp col"+str(temp_col))
    # print("temp sq"+str(temp_sq))
    return 1

i=0
while(i<9):
    j=0
    while(j<9):
        
        if(a[i][j]==0):
            check=0

            for num in range(1,10):
                if(isValid(num,i,j)==1):
                    a[i][j]=num
                    check=1
                    break
            
            if(check==0):
                check2=0
                # print("==========")
                # print("backtracing")
                # print("==========")

                while(check2==0):
                    # print("original i,j = "+str(i)+" , "+str(j))
                    temp_index=z.index([i,j])
                    a[i][j]=0
                    i=z[temp_index-1][0]
                    j=z[temp_index-1][1]
                    # print("new i,j = "+str(i)+" , "+str(j))
                    
                    for num in range(a[i][j]+1,10):
                        # print("************")
                        # print("checking for num="+str(num)+" @ i,j="+str(i)+","+str(j))
                        if(isValid(num,i,j)==1):
                            a[i][j]=num
                            check2=1
                            # check=1
                            # print("check2="+str(check2)+" @ i,j "+str(i)+","+str(j)+" num="+str(a[i][j])+" accepted")
                            break
                    

            # print("check="+str(check)+" @ i,j "+str(i)+","+str(j)+" num="+str(a[i][j])+" accepted")
            # print()

        j+=1
    i+=1


for i in range(9):
    for j in range(9):
        print(str(a[i][j]),end=" ")
    print("")

s=""
for i in range(9):
    for j in range(9):
        s+=str(a[i][j])+" "
    s+="\n"

from tkinter import *  
  
from tkinter import messagebox  
  
top = Tk()  
  
# top.geometry("800x1800")      
  
messagebox.showinfo("Sudoku Solved !",s)  
  
# top.mainloop()
