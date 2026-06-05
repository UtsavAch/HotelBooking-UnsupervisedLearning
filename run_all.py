#!/usr/bin/env python
import subprocess, os, sys
data_path = os.environ.get('HOTEL_DATA_PATH',
            '/content/hotel_bookings_course_release_v1.csv')
if not os.path.exists(data_path):
    print(f'ERROR: Dataset not found at {data_path}')
    sys.exit(1)
cmd = [
    'jupyter', 'nbconvert', '--to', 'notebook', '--execute',
    '--ExecutePreprocessor.timeout=10800',
    'hotel_clustering_final.ipynb',
    '--output', 'hotel_clustering_final_executed.ipynb'
]
subprocess.run(cmd, check=True)
print('Done — see hotel_clustering_final_executed.ipynb')
