#!/bin/bash
# method: https://gist.github.com/tanaikech/f0f2d122e05bf5f971611258c22c110f#update-at-march-21-2019
fileid="1pqZvEIMKehdoiCNaob2HutHTdvCbtLub"
filename="wine-reviews.zip"
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=${fileid}" > /dev/null
curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=${fileid}" -o ${filename}
