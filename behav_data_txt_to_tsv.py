#!/usr/bin/env python
from bids.grabbids import BIDSLayout
import os
import pandas as pd
import numpy as np
import re


def transform_behav_data(behav_dir, num, tsv_name):
    con_txt = os.path.join(behav_dir, 's' + num + '_con_RTdur.txt')
    isempty = os.stat(con_txt).st_size == 0

    if not isempty:
        con_pd = pd.read_csv(
            con_txt,
            names=["onset", "response_time", "trial_type"],
            sep='\t')

        con_pd['trial_type'] = con_pd['trial_type'].map({1: 'congruent_correct'})
    else:
        con_pd = None

    neu_txt = os.path.join(behav_dir, 's' + num + '_neu_RTdur.txt')
    isempty = os.stat(neu_txt).st_size == 0

    if not isempty:
        neu_pd = pd.read_csv(
            neu_txt,
            names=["onset", "response_time", "trial_type"],
            sep='\t')

        neu_pd['trial_type'] = neu_pd['trial_type'].map({1: 'neutral_correct'})
    else:
        neu_pd = None

    inc_txt = os.path.join(behav_dir, 's' + num + '_inc_RTdur.txt')
    isempty = os.stat(inc_txt).st_size == 0

    if not isempty:
        inc_pd = pd.read_csv(
            inc_txt,
            names=["onset", "response_time", "trial_type"],
            sep='\t')

        inc_pd['trial_type'] = inc_pd['trial_type'].map({1: 'incongruent_correct'})
    else:
        inc_pd = None

    err_txt = os.path.join(behav_dir, 's' + num + '_errors_RTdur.txt')
    isempty = os.stat(err_txt).st_size == 0

    if not isempty:
        err_pd = pd.read_csv(
            err_txt,
            names=["onset", "response_time", "trial_type"],
            sep='\t')

        err_pd['trial_type'] = err_pd['trial_type'].map({1: 'incorrect'})
    else:
        err_pd = None

    pd_list = [x for x in [con_pd, neu_pd, inc_pd, err_pd] if x is not None]
    combined_pd = pd.concat(pd_list)

    full_pd = combined_pd.assign(duration=pd.Series(np.full((len(combined_pd)), .2)).values)
    full_pd.to_csv(tsv_name, index=False, sep='\t')


dataset_path = os.path.expanduser("~/VossLabMount/Projects/PACR-AD/Imaging/BIDS/sourcedata")
print('getting bids data')
bids_dataset = BIDSLayout(dataset_path)

query = bids_dataset.get(type='bold', task='flanker', return_type='file', extensions='.nii.gz')

for item in query:
    print('formatting '+str(item))
    num = re.findall(r'\d+', item)[0].lstrip("0")
    sub_num = str('sub')+num

    # get session info
    r = re.compile(r'\bpost\b|\bpre\b')
    ses = r.findall(item)[0]

    # make the base directory
    sub_base_dir = sub_num + '_' + ses

    # top dir
    top_dir = os.path.dirname(item)

    # combine top dir and base dir
    behav_dir = os.path.join(top_dir, sub_base_dir)

    tsv_name = item.split('.')[0].replace('bold', 'events.tsv')

    transform_behav_data(behav_dir, num, tsv_name)
