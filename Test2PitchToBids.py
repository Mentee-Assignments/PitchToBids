#!/usr/bin/env python
import os
from glob import glob
from shutil import copyfile
import re

path = os.path.join(os.getcwd(), 'PITCH/PreprocData')
out_dir = os.path.join(os.getcwd(), 'PITCH/Bids')
file_dict = {'t1s': [], 'asls': [], 'flankers': [], 'rests': []}
file_dict['t1s'] = glob(path + '/[0-9][0-9]/[CEa-z]*/Pre/rsOut/anat/T1_MNI.nii.gz')

file_dict['flankers'] = glob(path + '/[0-9]{2}/[CEa-z]/[Preost]/Flanker/run[1-2]/beh/*')

for scantype, filenames in file_dict.items():
    if scantype == 'flankers':
        pattern = re.compile(r"^.*PreprocData/([0-9]{2})/([CEa-z]*)/([Preost]*)/Flanker/run[1-2]/beh/.*$")
        repl = r"sub-0\1/ses-\2\3/func/sub-0\1_ses-\2\3_task-flanker_run-0\4_events.tsv"
