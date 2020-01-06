#!/bin/bash
# 使用albacore分批识别,1000个一组
for i in {0..7}
do 
	read_fast5_basecaller.py -i ./rawSignal/$i -t 8 -f FLO-MIN107 -k SQK-LSK308 -o fast5 -s ./fast5_albacore/$i
done
