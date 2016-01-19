__author__ = 'jerrydumblauskas'
mn_list = [1,4,5,3,2,6,8,9,0]
mx_list = [0,7,3,1,6,5,3,8,5]
p = zip(mn_list,mx_list)
print ("zip output -- a list of tuples")
print (list(p))

print ("wrap syntax -- if you call a function with a *x, it is an iterable that will be unpacked, into the function")
print ("if it is in the func arg list, the values will be wrapped into a tuple")
lst = [1,2]

def wrap_in_a_tuple(*g):
    '''
    fan in
    '''
    print ("wrapped")
    print (type(g))
    print (g)

def splat_vars(t, h):
    '''
    fan out or show how we "SPLAT"
    '''
    print (t)
    print (h)

# fan out
splat_vars(*lst)
# fan in
wrap_in_a_tuple(lst, 3)

print ("dean's test")
p = zip(mn_list,mx_list)
print (list(zip(*p)))


print ("DECORATOR TESTS")

print ("OK 1========================(better, as it has the var args list)")
def p_decorate(func):
   def func_wrapper(*x):
       return "<p>{0}</p>".format(func(*x))
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print (get_text("Johnny"))


print ("OK=============================")

def p_decorate1(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate1
def get_text1(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print (get_text1("John"))


print ("ITERTOOLS!")

from itertools import chain

q=[1,2,3,4,5,6,7,8,9]
p=[3,4,5,3,2,4,5,6,7]
y = chain(q,p)

for t in y:
    print (t)

print ("Braden's idiom")
s = ('x1','y1','z1','x2','y2','z2','x3','y3','z3')
print ("so this is a list of 'x1','y1','z1','x2','y2','z2','x3','y3','z3'")
print ("when we splat the iter -- we get 3 refs to the same iter object")
print ("so each pointer to the same iter objects pulls from the same list i.e. s")
print ("the intermediate form is (x1,x2,x3), (y1,y2,y3), (z1,z2,z3)")
print ("the above, zipped, is below")
print (list(zip(*[iter(s)]*3)))