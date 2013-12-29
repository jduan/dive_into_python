#!/usr/bin/env python

def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.

    Take module, class, list, dictionary, or string."""

    method_list = [method for method in dir(object) if callable(getattr(object,
        method)) and not '__' in method]
    processFunc = collapse and (lambda s: ' '.join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
        (method.ljust(spacing),
            processFunc(str(getattr(object, method).__doc__)))
        for method in method_list])

if __name__ == '__main__':
    li = []
    info(object=li, spacing=20, collapse=False)
