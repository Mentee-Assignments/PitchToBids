import os
from glob import glob
from shutil import copyfile
import re

path = os.path.join(os.getcwd(), 'PITCH/PreprocData')
out_dir = os.path.join(os.getcwd(), 'PITCH/Bids')
file_dict = {'t1s': [], 'asls': [], 'flankers': [], 'rests': []}
file_dict['t1s'] = glob(path + '/[0-9][0-9]/[CEa-z]*/Pre/rsOut/anat/T1_MNI.nii.gz')

# abstract some paths so lines don't get too long
prefix = '/[0-9][0-9]/[CEa-z]*/[Preost]*'
file_dict['asls'] = glob(path + prefix + '/ASL/CBF_calc_1_5spld.nii.gz')

file_dict['flankers'] = glob(path + prefix + '/Flanker/run[1-2]/Flanker[1-2]Raw.nii.gz')

file_dict['rests'] = glob(path + prefix + '/rsOut/func/RestingStateRaw.nii.gz')

asdf = 5

for scantype, filenames in file_dict.items():
    if scantype == 't1s':
        pattern = re.compile(r"")
        repl = r""
        #
    elif scantype == 'asls':
        pattern = re.compile(r"")
        repl = r""
        #
    elif scantype == 'flankers':
        pattern = re.compile(r"")
        repl = r""
        #
    elif scantype == 'rests':
        pattern = re.compile(r"^.*PreprocData/([0-9]{2})/([CEa-z]*)/([Preost]*).*$")
        repl = r"sub-0\1/ses-\2\3/func/sub-0\1_ses-\2\3_task-rest_bold.nii.gz"
        #sub-001/ses-ControlPre/func/sub-001_ses-ControlPre_task-rest_bold.nii.gz

    for filename in filenames:
        # perhaps do a validation to make sure all groups exist that should exist
        len(re.search(pattern, filename).groups())

        out_filename = re.sub(pattern, repl, filename)
        out_path = os.path.join(out_dir, out_filename)
        # add the path back in
        copyfile(filename, out_path)
