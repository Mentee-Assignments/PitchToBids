import os
from glob import glob
from shutil import copyfile

path = os.path.join(os.getcwd(),'PITCH/PreprocData')
#glob(path + '/PreprocData/[0-9][0-9]/[CEa-z]*/*/*/**')
file_dict = {'t1s': [], 'asls': [], 'flankers': [], 'rests': []}
file_dict['t1s'] = glob(path + '/[0-9][0-9]/[CEa-z]*/Pre/rsOut/anat/T1_MNI.nii.gz')

file_dict['asls'] = glob(path + '/[0-9][0-9]/[CEa-z]*/[Preost]*/ASL/CBF_calc_1_5spld.nii.gz')

file_dict['flankers'] = glob(path + '/[0-9][0-9]/[CEa-z]*/[Preost]*/Flanker/run[1-2]/Flanker[1-2]Raw.nii.gz')

file_dict['rests'] = glob(path + '/[0-9][0-9]/[CEa-z]*/[Preost]*/rsOut/func/RestingStateRaw.nii.gz')

for scantype, filenames in file_dict.items():
    if scantype == 't1s':
        pattern = re.compile(r"")
        repl = r""
    elif scantype == 'asls':
        pattern = re.compile(r"")
        repl = r""
    elif scantype == 'flankers':
        pattern = re.compile(r"")
        repl = r""
    elif scantype == 'rests':
        pattern = re.compile(r"^.*PreprocData/([0-9]{2})/([CEa-z]*)/([Preost]*).*$")
        repl = r"sub-0\1/ses-\2\3/func/sub-0\1_ses-\2\3_task-rest_bold.nii.gz"

    for filename in filenames:
        # perhaps do a validation to make sure all groups exist that should exist
        len(re.search(pattern, filename).groups())

        out_filename = re.sub(pattern, repl, filename)
        # add the path back in
        
        copyfile(filename, out_filename)
