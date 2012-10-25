#!/bin/sh
# PBI building script
# This will run after your port build is complete
##############################################################################

avs_pbi_path=/usr/pbi/avs-$(uname -m)

find ${avs_pbi_path}/lib -iname "*.a" -delete
#rm -rf ${avs_pbi_path}/include
rm -rf ${avs_pbi_path}/share/doc
rm -rf ${avs_pbi_path}/share/emacs
rm -rf ${avs_pbi_path}/share/examples
rm -rf ${avs_pbi_path}/share/gettext
rm -rf ${avs_pbi_path}/share/gtk-doc/html/gi
rm -rf ${avs_pbi_path}/man
