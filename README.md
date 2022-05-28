# python 
### this is python demo 


## Decorators:- 

```python
def f1(func):
    def wrapper(*args,**kwargs):
        print("started")
        func(*args,**kwargs)
        print("ended")
@f1
def f(a):
    print("hello")
# f= f1(f)
f("hi")
```
