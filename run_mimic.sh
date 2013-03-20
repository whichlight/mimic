#!/bin/bash
sudo /home/pi/projects/mimic/mimic.py -d True > /home/pi/projects/mimic/data/`date +"%y-%m-%d_%H:%M:%S"`.tsv
