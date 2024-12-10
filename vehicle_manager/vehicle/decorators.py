from django.shortcuts import redirect

def authenication(fn):

    def wrapper(request,*args,**kwargs):

        if not request.user.is_authenticated:

            return redirect('signin')
        
        else:

            return fn(request,*args,**kwargs)
        
    return wrapper


