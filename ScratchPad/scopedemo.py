count = 0

def show_count():
    print("Count = ", count)

def set_count(c):
    global count #if  this line is not here, calling set_count will not change results of show_count
    count = c
