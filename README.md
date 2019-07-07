# File System Silent Corrupt
This code monitors a directory for silent data corruption.
It looks for changes in md5 sums but without change in file access time.

## Install
#### Dependencies
1. `Python 3`
2. `OSX 10.13` - This is when Apple switched from HFS to APFS.

#### Running
1. `python3 /absolute/path/to/dir/to/monitor`
