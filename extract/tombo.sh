#!/bin/bash
# 使用tombo分批识别,1000个一组
for i in {0..7}
do
  tombo resquiggle ./passFast5/$i ./ref.fa --processes 8 --corrected-group RawGenomeCorrected_001 --basecall-group Basecall_1D_000 --overwrite
done