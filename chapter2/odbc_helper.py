#!/usr/bin/env python

def build_connection_string(params):
    """ Build a connection string from a dictionary of parameters."""

    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    params = {
            "server": "mpilgrim",
            "database": "master",
            "uid": "sa",
            "pwd": "secret"
            }

    print build_connection_string(params)
