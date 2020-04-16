# dlcs_metadata_merge
Python script to combine dlcs export csv with bucketeered and festerized csvs for DLCS migration.

# Clone this repo
$ git clone https://github.com/UCLALibrary/dlcs_metadata_merge.git

# Navigate into the directory
$ cd dlcs_metadata_merge

# Run the script
$ python3 metadata_merge.py

# Add csv from eureka as prompted in terminal
$ Eureka CSV path: eureka.csv

# Add csv from DLCS export app
$ DLCS Export CSV path: dlcs_export.csv

# Notes

1. This script will overwrite the csv from the Eureka repo
2. It doesn't matter where the csvs are kept. You can drap and drop them into the terminal for their full path
3. This script requires all three new fields from the Bucketeer and Fester services (i.e. it will not run if only one service has been used and not all of the fields are included)
