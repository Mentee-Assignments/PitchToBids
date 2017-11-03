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
  - [Excellent Introduction](https://www.youtube.com/watch?v=0sOfhhduqks&feature=youtu.be&t=5m27s)
    - [matching tutorial exercises](https://pycon2016.regex.training/)
    - ^^^ This will be crucial to matching the files we want to change and "grabbing" them intelligently
