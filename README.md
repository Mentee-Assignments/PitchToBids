# PitchToBids
Goal: take the PITCH dataset and rename/move files so they conform to the BIDS standard

## Getting Started, Step 0
1) clone this repository: click on the green clone/download button and select the copy to clipboard option
2) On your linux computer, open a terminal and type `git clone https://github.com/Mentee-Assignments/PitchToBids/`
3) `cd` into your newly cloned repository
### after you make a change
1) say you added a txt file called "file.txt" in the top level directory (e.g. PitchToBids/file.txt)
2) add the file to be tracked by git using `git add file.txt` (assuming you are in the PitchToBids directory)
3) commit the file by typing `git commit -m 'added file.txt'`
4) then submit the change to the online repository by typing `git push origin master`


## Step 1: Come up with a template for naming the 4 files (anat, rest, flanker, asl)
- Guides:
  - [BIDS spec](https://docs.google.com/document/d/1HFUkAEE-pB-angVcYe6pf_-fVf4sCpOHKesUvfb8Grc/edit#heading=h.qdzsf8lh4for)
  - [BIDS paper](https://www.nature.com/articles/sdata201644)
  - [BIDS ASL spec](https://docs.google.com/document/d/15tnn5F10KpgHypaQJNNGiNKsni9035GtDqJzWqkkP6c/edit#)
- Result:
  - Template for each filetype (anat, rest, flanker, asl)
    - ex: sub-[0-9]+/ses-[ExercisePre,ExcercisePost]/anat/TEMPLATE-FILENAME
  - Place the templates as a .txt file in this respository

## Step 2: Coding
- Background: REGEX
  - [Excellent Introduction](https://www.youtube.com/watch?v=0sOfhhduqks)
    - [matching tutorial exercises](http://pycon2017.regex.training/)
    - ^^^ This will be crucial to matching the files we want to change and "grabbing" them intelligently

## Step 3: Describe the behavioral data for the flanker task
- Reading section [4.2 of the BIDS spec](http://bids.neuroimaging.io/bids_spec1.0.2.pdf) gives us the general format of the output behavioral tsv we want. A simple end result will look like this:

| onset | duration | response_time | correct | trial_type |
|:-----:|:--------:|:-------------:|:-------:|:----------:|
| 8.00  | 0.517    | 0.909         | 1       | congruent  |
| 12.00 | 0.517    | 1.217         | 0       | incongruent|
| 22.00 | 0.517    | 0.833         | 1       | congruent  |
| 30.00 | 0.517    | 1.011         | 1       | incongruent|

- The files that contain all the pertinent information look like this:
  - P01C1BOL_ALL_Incorrect_A_Duration.txt
  - P01C1BOL_Congruent_Correct_A_Duration.txt
  - P01C1BOL_Congruent_Correct_A_RT.txt
  - P01C1BOL_Congruent_Incorrect_A_Duration.txt
  - P01C1BOL_Congruent_Incorrect_A_RT.txt
  - P01C1BOL_Incongruent_Correct_A_Duration.txt
  - P01C1BOL_Incongruent_Correct_A_RT.txt
  - P01C1BOL_Incongruent_Incorrect_A_Duration.txt
  - P01C1BOL_Incongruent_Incorrect_A_RT.txt
  - P01C1BOL_Neutral_Correct_A_Duration.txt
  - P01C1BOL_Neutral_Correct_A_RT.txt
  - P01C1BOL_Neutral_Incorrect_A_Duration.txt
  - P01C1BOL_Neutral_Incorrect_A_RT.txt
- From that listing we see we will get the "correct" information and the
  "trial_type" information from the filenames.
- The contents of a Duration file look like this:

| | | |
|-|-|-|
|10.009059 | 0.51663 | 1|
|23.957940 | 0.51662 | 1|
|45.906190 | 0.51662 | 1|
|55.888724 | 0.51662 | 1|
|57.871890 | 0.51662 | 1|
|65.854588 | 0.51662 | 1|
|105.751380 | 0.51662 | 1|
|109.717748 | 0.51660 | 1|
|121.666754 | 0.51662 | 1|
|129.649453 | 0.51663 | 1|
|147.598022 | 0.51662 | 1|
|153.580874 | 0.51662 | 1|
|177.845593 | 0.51662 | 1|
|201.743675 | 0.51662 | 1|
|217.659050 | 0.51663 | 1|
|241.607136 | 0.51662 | 1|
|297.402644 | 0.51663 | 1|
|307.368512 | 0.51663 | 1|
|323.317242 | 0.51662 | 1|
|327.300254 | 0.51662 | 1|
|335.282948 | 0.51662 | 1|

- ^^ The first column corresponds to onset, the second column to duration, and
  we don't care about the third column.

- The contents of a RT file look like this:

| | | |
|-|-|-|
|10.009059 | 0.50260 | 1|
| 23.957940 | 0.52935 | 1|
| 45.906190 | 0.63653 | 1|
| 55.888724 | 0.60575 | 1|
| 57.871890 | 0.82254 | 1|
| 65.854588 | 0.72759 | 1|
| 105.751380 | 0.67776 | 1|
| 109.717748 | 0.63933 | 1|
| 121.666754 | 0.72197 | 1|
| 129.649453 | 1.14706 | 1|
| 147.598022 | 0.76601 | 1|
| 153.580874 | 0.68698 | 1|
| 177.845593 | 0.71768 | 1|
| 201.743675 | 0.93095 | 1|
| 217.659050 | 0.93515 | 1|
| 241.607136 | 0.51674 | 1|
| 297.402644 | 0.90944 | 1|
| 307.368512 | 0.79132 | 1|
| 323.317242 | 0.91417 | 1|
| 327.300254 | 0.99504 | 1|
| 335.282948 | 0.89215 | 1|

- ^^ The first column corresponds to onset, the second column to response_time,
  and the third we don't care about.

- Finally the name of the file will conform to section 8.5 of the
  [BIDS spec](http://bids.neuroimaging.io/bids_spec1.0.2.pdf). The output
  file name will be identical to the flanker bold file name, except the suffix
  will change from `_bold.nii.gz` to `_events.tsv`.

- From this we have all the information we need to create a BIDS behavioral tsv.

## Step 4: Write out how you would solve this problem in English
- first think of the general steps required to solve this problem and then think
about how you would complete each of those steps. This will determine the
outline of the code solution.

## Step 5: Implement the solution in python
