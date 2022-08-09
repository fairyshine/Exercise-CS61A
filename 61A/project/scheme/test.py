
from scheme import *
env = create_global_frame()
lambda_line = "(lambda (a b c) (+ a b c))"
lambda_proc = do_lambda_form(lambda_line.rest, env)
lambda_proc.formals # use single quotes ' around strings in your answer