import os
fd = os.open("testdata.txt", os.O_RDWR)
os.write(fd, b'Hello I am loving reading, and I will become automation tester soon')
os.close(fd)