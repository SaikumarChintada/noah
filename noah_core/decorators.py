from functools import wraps
from django.utils.decorators import available_attrs
from django.http import JsonResponse


def social_login_required(view_func):
    @wraps(view_func, assigned=available_attrs(view_func))
    def inner(request, *args, **kwargs):
        print (request.user)
        if request.user.is_authenticated:
            try:
                return view_func(request, *args, **kwargs)
            except Exception as e:
                return JsonResponse({'success': False})
        else:
            return JsonResponse({'success': False })
    return inner
