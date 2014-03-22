#! /bin/sh -x

sort -t: -r video.txt

sort -t: -k 1 video.txt

sort -t: -nk 3 video.txt

sort -t: -r -nk4 -k1 video.txt

#uniq必须处理已经sort的文件
sort myfile.txt | uniq -c

cut -c1,2-4 video.txt

cut -d: -f1,3 video.txt


split -2 video.txt
