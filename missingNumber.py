n = int(input())
nums=[]
input_string = input()
string_list = input_string.split()
nums = [int(x) for x in string_list]
i=1
nums.sort()
for j in nums:
    if(i==j):
        i += 1
        if(i==n):
            print(i)
        
    else:
        print(i)
        break
    
       
   
  



            
            

