import sys

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()   # to track the error like file ,line_number

    file_name = exc_tb.tb_frame.f_code.co_filename # file information from which file the error has occured

    error_message = "Error occured python script name [{0}] line under [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message,error_detail = error_detail
        )
    
    def __str__(self):
        return self.error_message
    

# exc_type, exc_value, exc_tb = sys.exc_info()


# exc_type (first value):
# The type of the exception (e.g., ZeroDivisionError, ValueError, etc.)

# exc_value (second value):
# The actual error message or object (e.g., division by zero)

# exc_tb (third value):
# The traceback object, which holds info like:

# What file the error happened in

# What line number

# The call stack at the time of the error
