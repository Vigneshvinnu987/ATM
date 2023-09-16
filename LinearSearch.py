pos = -1
def search(list,n):
    i = 0
    while i<len(list):
        if list[i] == n:
            globals() ['pos'] = i
            return True
        i = i+1
    return False
list = [19,20,99,100,44,33]
n = 99
if search(list,n):
    print("Fount at the value",pos+1)
else:
    print("Not found")