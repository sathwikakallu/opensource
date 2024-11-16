n1,n2=input().split()
if ((n1=='S') and (n2=='P')) or ((n1=='P') and (n2=='R')) or ((n1=='R') and (n2=='S')):
    print("Vignesh")
elif ((n1=='P') and (n2=='S')) or ((n1=='R') and (n2=='P')) or ((n1=='S') and (n2=='R')):
    print("Charan")
elif ((n1=='S') and (n2=='R')) or ((n1=='P') and (n2=='S')) or ((n1=='R') and (n2=='P')):
    print("Charan")
elif ((n1=='R') and (n2=='S')) or ((n1=='S') and (n2=='P')) or ((n1=='P') and (n2=='R')):
    print("Vignesh")
else:
    print("NULL")
