#!/bin/bash

#Generation of NMR calculation inputfile
rm template*
cp ../template_nmr.gjf template.gjf
for inf in *.out
do
  Multiwfn "$inf" < ~/software/Multiwfn_2026.4.10_bin_Linux/gjf_selection.txt > /dev/null
done
rm template.gjf

#Rename
for inf in gau*.gjf
do
  mv "$inf" "$(echo "$inf" | sed 's/gau/nmr/g')"
done

#NMR calculation
for inf in *.gjf
do
  echo Running "$inf" ... 
  g16 < "$inf" > "${inf//gjf/out}"
  echo "$inf" has finished
done
