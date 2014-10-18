from functools import partial, update_wrapper
from random import random

from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import RedirectView


def empty_view(request, *args, **kwargs):
    return HttpResponse('')


def kwargs_view(request, arg1=1, arg2=2):
    return HttpResponse('')


def absolute_kwargs_view(request, arg1=1, arg2=2):
    return HttpResponse('')


def defaults_view(request, arg1, arg2):
    pass


def nested_view(request):
    pass


def erroneous_view(request):
    import non_existent  # NOQA


def pass_resolver_match_view(request, *args, **kwargs):
    response = HttpResponse('')
    response.resolver_match = request.resolver_match
    return response

uncallable = "Can I be a view? Pleeeease?"


class ViewClass(object):
    def __call__(self, request, *args, **kwargs):
        return HttpResponse('')

view_class_instance = ViewClass()


class LazyRedirectView(RedirectView):
    url = reverse_lazy('named-lazy-url-redirected-to')


@user_passes_test(lambda u: u.is_authenticated(), login_url=reverse_lazy('some-login-page'))
def login_required_view(request):
    return HttpResponse('Hello you')


def bad_view(request, *args, **kwargs):
    raise ValueError("I don't think I'm getting good value for this view")


empty_view_partial = partial(empty_view, template_name="template.html")


empty_view_wrapped = update_wrapper(
    partial(empty_view, template_name="template.html"), empty_view,
)


@login_required
def login_required_view(request):
    return HttpResponse("Now, you're logged in, that's not funny!")


def redirect_to_nonexistant_view(request):
    return redirect('no.such.view')


def redirect_to_nonexistant_with_argument_view(request):
    return redirect('no.such.view?a=%s' % random())


def target_without_pattern_view(request):
    return HttpResponse("Just a fine view, but not linked in urls.py.")


def redirect_to_patternless_view(request):
    return redirect('urlpatterns_reverse.views.target_without_pattern_view')


def target_with_int_argument_view(request, number):
    return HttpResponse("Just a fine view that takes an integer argument.")


def redirect_with_wrong_argument_view(request):
    return redirect('urlpatterns_reverse.views.target_with_int_argument_view', number='a')
