#!/bin/bash
# Display all HTTP methods the server of a given URL will accept.
curl -si "$1" | grep 'Allow:' | cut -d ':' -f2 | cut -b2-
