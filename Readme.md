# Extract PDF Contents
Small python program to extract a table of contents from a research article in pdf format.
The sections have to be of the form "x.x title of the section" where x.x denotes the numbering of the current (sub)section.

Use:
```bash
./extractPdfContent <path/to/pdf>
```

Based on `textract`, tested on Robotics articles such as [this one](https://www.researchgate.net/profile/Emmanouil_Tsardoulias/publication/303501196_A_Review_of_Global_Path_Planning_Methods_for_Occupancy_Grid_Maps_Regardless_of_Obstacle_Density/links/5bf52667a6fdcc3a8de66100/A-Review-of-Global-Path-Planning-Methods-for-Occupancy-Grid-Maps-Regardless-of-Obstacle-Density.pdf)
