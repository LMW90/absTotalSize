import os
totalSize = 0
for filename in os.listdir('C:\\Users\LMW\Desktop\CV'):
    totalSize += os.path.getsize(os.path.join('C:\\Users\\LMW\\Desktop\\CV', filename))
print(totalSize)
