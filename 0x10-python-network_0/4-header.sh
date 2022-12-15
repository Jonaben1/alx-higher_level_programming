#!/bin/bash
# Send a GET request to a given URL with a header variable.
curl -LsX Get -H "X-School-User-Id: 98" "$1"

