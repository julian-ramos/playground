import traceback

def someFunction(*args):
    for i in args:
        print i
        
        
def func(*args,**kwargs):
    stack = traceback.extract_stack()
    filename, lineno, function_name, code = stack[-2]
    print filename
    print lineno
    print function_name
    print code
        
        
        
        
if __name__=="__main__":
    a=1
    b=2
    c=3
    d=5
    someFunction(a,b,c,d)
    
    func(a=1,b=2,c=3)