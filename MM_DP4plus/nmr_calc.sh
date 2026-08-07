#!/bin/bash

#NMR calculation
for inf in *.gjf
do
  echo Running "$inf" ... 
  g16 < "$inf" > "${inf//gjf/out}"
  echo "$inf" has finished
done
