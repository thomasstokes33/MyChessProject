def function():
    print()
    print()
    variable=1
    print(locals())
    print(vars())
    print(globals())
    print()
    print()
globalwcastle=True
globalbcastle=True
colour='black'
name="global"+colour[0]+'castle'
print(globals())
print(vars())
function()
vars()[name]=False
print(globalbcastle)
