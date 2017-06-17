#!/usr/bin/env python

'''Compute a single row of a distance matrix from a pdbinfo file.  
This allows for distributed processing'''

import clustering

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute a single row of a distance matrix from a pdbinfo file.')
    parser.add_argument('--pdbfiles',type=str,required=True,help="file with target names and paths to pbdfiles of targets (separated by space)")
    parser.add_argument('-r','--row',type=int,required=True,help="row to compute")
    parser.add_argument('--out',help='output file (default stdout)',type=argparse.FileType('w'),default=sys.stdout)

    args = parser.parse_args()
    
    target_names, targets = train.readPDBfiles(args.pdbfiles)

    r = args.row
    if r < len(target_names):
        name = target_names[r]
        row = []
        for i in xrange(len(target_names):
            (a, b, mindist) = train.cUTDM2(targets, (r,i))
            row.append((target_names[i],mindist))
        #output somewhat verbosely
        for (n,dist) in row:
            args.out.write('%s %s %f\n'%(name,n,dist)
    else:
        print "Invalid row",r,"with only",len(target_names),"targets"