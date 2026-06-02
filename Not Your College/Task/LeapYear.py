# question : check year is a leap year or not 

year = int(input("enter year to check :"))


if( (year%100==0 and year%400 ==0) or (year%100!=0 and year%4==0 )):  # (not valid)
      print("leap year")
else :
      print("not a leap year")

      # year%400 ==0 or year%4 ==0  (not valid)
      #(year%400==0 and yar%100==0) and (year%4==0) (not valid)