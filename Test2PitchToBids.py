#!/usr/bin/env python
import os
from glob import glob
import re
import pandas as pd
import numpy as np

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
            if cond_corr in cond_dict[sub_stype_ses_run]:
                cond_dict[sub_stype_ses_run][cond_corr].append(f)
            else:
                cond_dict[sub_stype_ses_run][cond_corr] = [f]
        else:
            cond_dict[sub_stype_ses_run] = {cond_corr: [f]}
            
def non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0
headers = ['onset', 'duration', 'response_time', 'correct', 'trial_type']

for sub_stype_ses_run, fdict in cond_dict.items():
    run_df = pd.DataFrame(columns=headers)
    # make the output dataframe for this subject
    for cond_corr, fnames in fdict.items():
        fname_dict = {'Duration': None, 'RT': None}
        cond, corr = cond_corr.split('_')
        for fname in fnames: #has RT and Duration file
            if 'Duration' in fname:
                col_names = ['onset', 'duration', 'extra1', 'extra2']
                key = 'Duration'
            elif 'RT' in fname:
                col_names = ['onset', 'response_time', 'extra1', 'extra2']
                key = 'RT'
            else:
                print('something is wrong for {fname}'.format(fname=fname))
            if non_zero_file(fname):
            # load fname into pandas dataframe
                df_fname = pd.read_csv(fname, sep='       ', header=None)
                df_fname.columns = col_names
                df_fname.drop(labels=['extra1', 'extra2'], axis=1, inplace=True)
                fname_dict[key] = df_fname
                new_cols = ['trial_type', 'correct']
                cond_list = [cond for _ in range(len(df_fname))]
                if corr == 'Correct':
                    int_corr = 1
                elif corr == 'Incorrect':
                    int_corr = 0
                else:
                    print('{fcorr} is neither correct nor incorrect'.format(fcorr=corr))
                corr_list = [int_corr for _ in range(len(df_fname))]
                # Add corr_list and cond_list to df_fname
                for lst, coln in zip([cond_list, corr_list], new_cols):
                    se = pd.Series(lst)
                    df_fname[coln] = se.values
        if fname_dict['Duration'] is not None:
            if fname_dict['RT'] is None:
                df_Nan = fname_dict['Duration'].copy()
                df_Nan.rename(index=str, columns={'duration': 'response_time'}, inplace=True)
                RT_list = [np.nan] * len(df_Nan)
                df_Nan['response_time'] = RT_list
                fname_dict['RT'] = df_Nan
            df_cond_corr = pd.merge(fname_dict['Duration'], fname_dict['RT'], on=['onset', 'correct', 'trial_type'])
            # Append the resulting df from the above operation to run_df
            run_df = run_df.append(df_cond_corr)
    run_df = run_df[headers]
    run_df.sort_values(by=['onset'], inplace=True)
    sub, stype, ses, run = sub_stype_ses_run.split('_')
    out_file = os.path.join(os.getcwd(), 'PITCH/Bids/sub-0{sub}/ses-{stype}{ses}/func/sub-0{sub}_ses-{stype}{ses}_task-flanker_run-0{run}_events.tsv'.format(sub=sub, ses=ses, run=run, stype=stype))
    if not run_df.empty:
        run_df.to_csv(out_file, sep='\t', na_rep='NaN', index=False)
    #run_df.drop(['correct', 'trial_type', 'correct_x', 'trial_type_x'], axis=1, inplace=True)
    # write out run_df to disk (as a tsv)

        # X combine information from cond_corr (e.g. 'Neutral_Incorrect')
        # X should have both Duration and RT files loaded as DataFrames
        # X append the information to run_df
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
