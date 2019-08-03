import glob
import os

for hour in range(24):
    #cmd = 'aws s3 cp s3://cliodinamica/12_uber/SCL_hora%02d.csv.gz .' %hour
    #os.system(cmd)
    cmd = 'git add SCL_hora%02d.csv.gz .' %hour
    os.system(cmd)

os.system('git commit -am "added uber Santiago maps"')

