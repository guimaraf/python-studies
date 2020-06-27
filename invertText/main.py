infoText = 'type here the text you want to invert'
firstList = list(infoText)
firstList.reverse()

reversetext = ""

for i in firstList:
  reversetext+= i
  
print(reversetext)