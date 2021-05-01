#!/usr/bin/env bash

mkdir -p tmp
cd tmp
chmod 644 *
newres=800x450

for old_fname in `ls`
do

  mogrify -format jpg -quality 72 -resize 800x450\! -colorspace Gray $old_fname
  rm -f $old_fname

done
