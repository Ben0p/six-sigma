# six-sigma
Windows system environment statistical logging and covariance analysis

#### NOTE
This project has been put on the back burner shortly after starting due to higher priorities. Added to the graveyard with all my other partially started projects.

## Overview
Heavily based on psutil, gathers windows information and resource utilization. Logs to various .csv files for later processing. If running on multiple machines, save to a networked drive for central acess.

1. Static information
    * Number of disks / partitions
    * Number of CPUs - physical / logical
    * ...
2. Historical information
    * CPU usage
    * RAM usage
    * Disk
    * Netowrk
    * Processes
    * Users
3. Report generation
    * Generate plots / reports
    (T.B.A)

### Architecture
* Main process initiates multiprocess threads of each worker
* Workers in /workers module
* Dictonary models in /models (guide only, they are not being imported)
* Each worker puts it's dictonary into the multiprocess queue
* Main process retreives these from the queue and combines into main dictionary
* The main dictionary is then processes into .csv files
* It could also be inserterted into a nosql db if desired