patient = {"Dean" : (105,130,140),
           "Siah" : (80,90,100),
           "Nino" : (110 , 145 , 150)
           }
normal = 120
for pn,bs in patient.items():
    print(f"\nPatient:{pn}" )
    for b in bs:
      if b > normal:
         print(b, "| Diabeitc")
      else:
          print(b, "| Normal")
    highest =max(bs)
    print("Highest Blood Sugar Count", highest, pn)
    lowest =min(bs)
    print("Lowest Blood Sugar Count", lowest, pn)
    difference = highest - lowest
    print("Difference:", difference, pn)
    average = sum(bs)/len(pn)
    print("Average" , average , pn)