x = 10
def function():
    global x #if  you want to access a global variable just write befour golbal.
    x =  20
function()
print(x)