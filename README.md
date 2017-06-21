# Status check of the website 'http://nits.ac.in'
A python script to periodically check the status of a particular website, and log the status results.

## Code
This script is written in python, and tested with python 3 or higher. 

## Usage
From the terminal of the workstation, run `...$ ipython check_web.py` or `...$ python3 check_web.py`
Plese note that the variable `CHECK_INTERVAL` indicates the periodic time, after which a test is conducted.

## Log file
The generated log file notes the following items:
* `Date`: Date stamp of the sanity check
* `Time`: Time stamp of the sanity check
* `Status`: Status of the nits.ac.in website. A `OK` flag indicates that it is working fine, and `Not OK` flag indicates otherwise.
* `Ping Time (ms)`: Successful ping time measured in mili seconds
* `Remarks`: Any additional remarks.
