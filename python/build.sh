#!/bin/bash 

#pip3 --target package psutil
rm -f function.zip 

cd package 
zip -r9 ../function.zip .

cd ..
zip function.zip *.py


