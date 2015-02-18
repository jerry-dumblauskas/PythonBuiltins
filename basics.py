__author__ = 'jerrydumblauskas'
mn_list = [1,4,5,3,2,6,8,9,0]
mx_list = [0,7,3,1,6,5,3,8,5]
p = zip(mn_list,mx_list)
print "zip output -- a list of tuples"
print p

print "wrap syntax -- if you call a function with a *x, it is an iterable that will be uppacked into the function"
print "if it is in the func arg list, the values will be wrapped into a tuple"
lst = [1,2]

def wrap_in_a_tuple(*g):
    '''
    fan in
    '''
    print "wrapped"
    print type(g)
    print g

def unpack_vars(t, h):
    '''
    fan out
    '''
    print t
    print h

# fan out
unpack_vars(*lst)
# fan in
wrap_in_a_tuple(lst, 3)

print "dean's test"
print zip(*p)


print "DECORATOR TESTS"

print "OK 1========================"
def p_decorate(func):
   def func_wrapper(*x):
       return "<p>{0}</p>".format(func(*x))
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text("Johnny")


print "OK============================="

def p_decorate1(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate1
def get_text1(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text1("John")
