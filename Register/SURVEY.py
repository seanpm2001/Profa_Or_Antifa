# Start of script
# Profa or Antifa survey
print ("Profa or Antifa survey - Register")
reg = str(input("Do you support dictatorships? (such as Nazi Germany, Fascist Italy, Soviet Russia, Communist China, etc.)"))
reg == reg.upper()
if (reg == "Y" or "YES"):
  regA = int(0)
  regB = int(1)
  print ("You have successfully registered to be part of Profa")
else:
  regA = int(1)
  regB = int(0)
  print ("You have successfully registered to be part of Antifa")
break
noMore = input("Press [ENTER] key to quit")
print ("Exiting survey...")
""" File info
File type: Python 3 source file (*.py)
File version: 1 (Sunday, April 11th 2021 at 4:46 pm)
Line count (including blank lines and compiler line): 23
"""
# End of script
