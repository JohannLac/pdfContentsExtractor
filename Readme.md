# Extract PDF Contents
Small python program to extract a table of contents from a research article in pdf format.
The sections have to be of the form "x.x title of the section" where x.x denotes the numbering of the current (sub)section.

Use:
```bash
./extractPdfContent <path/to/pdf>
```

Based on `textract`, tested on Robotics articles such as [this one](https://www.researchgate.net/profile/Emmanouil_Tsardoulias/publication/303501196_A_Review_of_Global_Path_Planning_Methods_for_Occupancy_Grid_Maps_Regardless_of_Obstacle_Density/links/5bf52667a6fdcc3a8de66100/A-Review-of-Global-Path-Planning-Methods-for-Occupancy-Grid-Maps-Regardless-of-Obstacle-Density.pdf)

Example:
```bash
>./extractContects.py article.pdf
Extract text from test.pdf...
Process and find matching patterns...
Result:
----------------------------------------
1 Introduction
2 Related Work
3 Metrics 
  3.1 Performance Metrics
    3.1.1 Mean Execution Time 
    3.1.2 Relative Standard Deviation 
    3.1.3 Mean Path Distance 
    3.1.4 Relative Standard Deviation 
    3.1.5 Path Anomaly 
    3.1.6 Estimated Time of Traversal 
    3.1.7 Success Rate 
  3.2 Experimental Environments
    3.2.1 Environment 1 
    3.2.2 Environment 2 
    3.2.3 Environment 3 
    3.2.4 Environment 4 
    3.2.5 Environment 5 
  3.3 Map Container Specifications
  4.1 Probabilistic RoadMaps 
    4.1.1 Uniform Space Sampling 
    4.1.2 Random Space Sampling 
    4.1.3 Space Sampling with Halton Sequences 
    4.1.4 Uniform Incremental Space Sampling 
    4.2.1 Simple Visibility Graph 
  4.2 Visibility Graphs
    4.2.2 Visibility Graph with Sparse Uniform Sampling
  4.3 Rapidly Exploring Random Trees 
    4.3.1 Standard RRT
    4.3.2 RRT 
    4.3.3 Multiple RRTs 
    4.3.4 Multiple Incremental RRTs 
  4.4 Space Skeletonization
    4.4.1 Generalized Voronoi Diagram 
5 Experimental Results
6 Conclusions 
----------------------------------------
```
