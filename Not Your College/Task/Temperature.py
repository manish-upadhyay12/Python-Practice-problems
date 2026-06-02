  # Qusetion : check temperature and print 
    #   -5 to 5 = very cold
    #   6 to 18 - cold
    #   19 to 40 = hot
    #   >=41  = very hot
#        <-5 = very cold


tem = int(input("enter temperature ="))

if tem>=-5 and tem<=5 :
    print("Temperature is very cold")
    
elif tem>=6 and tem<=18 :
    print("Temperature is  cold")
    
elif tem>=19 and tem<40 :
    print("Temperature is hot")
    
elif  tem>=41  :
    print("Temperature is very hot ")
elif tem<-5 :
    print("Temperature is very cold")

    # task completed
