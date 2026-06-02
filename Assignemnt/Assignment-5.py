# smart bill calculator : calculate bill and take number of friend and 
#  find how many money pay by each person

total_amount = float(input("enter your total amoun of bil :"))
no_of_friends = int(input("enter no of friends who pay bill :"))

each_will_pay  = total_amount/no_of_friends
print("Each friends will pay : " , each_will_pay)
