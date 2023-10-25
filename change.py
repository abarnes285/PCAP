changeAmt = input("What is the customer's change amount?")
changeAmt = int(changeAmt)

numQtrs = changeAmt // 25 
changeAmt =   changeAmt - (numQtrs*25)

numDimes = changeAmt // 10 
changeAmt = changeAmt -(numDimes*10)

numNickeles = changeAmt // 5
changeAmt = changeAmt - (numNickeles*5)

numPennies = changeAmt // 1
changeAmt = changeAmt - (numPennies*1)

print ("Quarters:",  numQtrs)
print ("Dimes: %s" % numDimes)
print ("Nickles: {}" .format(numNickeles))
print (f"Pennies: {numPennies}")
print(f"Final Change Amount: {changeAmt}")

