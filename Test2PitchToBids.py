#!/usr/bin/env python
import os
from glob import glob
import re
import pandas as pd

path = os.path.join(os.getcwd(), 'PITCH/PreprocData')
out_dir = os.path.join(os.getcwd(), 'PITCH/Bids')
beh = glob(os.path.join(path, '[0-9][0-9]/[CEa-z]*/[Preost]*/Flanker/run[1-2]/beh/*.txt'))


# rough draft
# Optionally match 'ALL'
pattern = re.compile(r"^.*PreprocData/([0-9]{2})/([CEa-z]*)/([Preost]*)/Flanker/run([1-2])/beh/.*?_(ALL)?.*$")
beh_dict = {}
for filename in beh:
    res = re.search(pattern, filename)
    # we don't want to collect 'ALL'
    if 'ALL' not in res.groups():
        dict_key = '_'.join(res.groups()[:-1])
        if dict_key in beh_dict:
            beh_dict[dict_key].append(filename)
        else:
            beh_dict[dict_key] = [filename]


cond_pattern = re.compile(r"^.*beh/.*?([NCIa-z]*)_([ICa-z]*)_[A-Z]_[RTDa-z]*.txt$")
cond_dict = {}
for sub_stype_ses_run, fnames in beh_dict.items():
    for f in fnames:
        find_cond = re.search(cond_pattern, f)
        cond_corr = '_'.join(find_cond.groups())
        if sub_stype_ses_run in cond_dict:
            if cond_corr in cond_dict:
                cond_dict[sub_stype_ses_run][cond_corr].append(f)
            else:
                cond_dict[sub_stype_ses_run][cond_corr] = [f]
        else:
            cond_dict[sub_stype_ses_run] = {cond_corr: [f]}

headers = ['onset', 'duration', 'response_time', 'correct', 'trial_type']
for sub_stype_ses_run, fdict in cond_dict.items():
    # make the output dataframe for this subject
    out_df = pd.DataFrame(columns=headers)
    for cond_corr, fnames in fdict.items():
        for fname in fnames:
            print(fname)
            # load fname into pandas dataframe
        # combine information from cond_corr (e.g. 'Neutral_Incorrect')
        # should have both Duration and RT files loaded as DataFrames
        # append the information to out_df
    # Name and find the place to save the tsv in the BIDS appropiate manner
    # ^^^ Don't use regex, we already have the relevant information from
    # sub_stype_ses_run to save the file in the correct place.
    # "sub-0{sub}/ses-{stype}{ses}/func/sub-0{sub}_ses-{stype}{ses}_task-flanker_run-0{run}_bold.nii.gz".format(your settings here)

# items to learn about:
# 1. format strings: https://www.youtube.com/watch?v=vTX3IwquFkc
# 2. pandas operations:
#    - read_csv
#    - append, concat
#    - to_csv
