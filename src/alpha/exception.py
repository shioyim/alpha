class BaseError(Exception):
    """custom error"""
    def __repr__(self):
        return self.mess

    def __init__(self):
        self.code = "custom-base-error"
        self.mess = "Custom a base error"

class DeliverError(BaseError):
    """deliver a foreign exception"""
    def __init__(self, err):
        if isinstance(err,Exception):
            self.code = err.__class__.__name__
            self.mess = err.args[0]
        else:
            self.code = "object-not-a-exception"
            self.mess = "Object delivered is not a exception instance"

class Debug(BaseError):
    """debug unknow error can use"""
    def __init__(self,err=None):
        self.err = err
        pdb.set_trace()

class UnknowError(BaseError):
    """raise a unknow error"""
    def __init__(self,mess="Raise a unknow error"):
        self.code = "unknow-error"
        self.mess = mess

#example
# #
# def f(x):
#     try:
#         return 1/x,None
#     except Exception  as e:
#         raise UnknowError("Raise a unknow error")

# def cst_f(x):
#     try:
#         val,error = f(x)
#         return val,None
#     except UnknowError as e:
#         return None,e

# cst_f(0)

#debug 
# def f(x):
#     try:
#         return 1/x,None
#     except Exception  as e:
#         raise Debug(e)
# def debug_f(x):
#     val,error = f(x)
#     return val,None
# debug_f(0)  

# DeliverError
# def f(x):
#     try:
#         return 1/x,None
#     except Exception  as e:
#         raise DeliverError(e)

# def del_f(x):
#     try:
#         val,error = f(x)
#         return val,None
#     except DeliverError as e:
#         return None,e
# del_f(0)   
