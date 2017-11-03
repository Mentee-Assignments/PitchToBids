
path = os.path.join(os.getcwd(),'PITCH/PreprocData')
#glob(path + '/PreprocData/[0-9][0-9]/[CEa-z]*/*/*/**')

T1s = glob(path + '/[0-9][0-9]/[CEa-z]*/Pre/rsOut/anat/T1_MNI.nii.gz')

asls = glob(path + '/[0-9][0-9]/[CEa-z]*/[Preost]*/ASL/CBF_calc_1_5spld.nii.gz')

flankers = glob(path + '/[0-9][0-9]/[CEa-z]*/[Preost]*/Flanker/run[1-2]/Flanker[1-2]Raw.nii.gz')

rest = glob(path + '/[0-9][0-9]/[CEa-z]*/[Preost]*/rsOut/func/RestingStateRaw.nii.gz')
