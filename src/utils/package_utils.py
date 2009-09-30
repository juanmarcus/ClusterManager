import os
import tarfile

def build_package(packagename, filelist, srcdir="./src"):
    
    if os.path.exists(packagename):
        print "removing previous package: %s" % packagename
        os.remove(packagename)
    
    print "creating package: %s" % packagename
    tar = tarfile.open(packagename, "w:gz")
    
    # Save current directory
    cwd = os.getcwd()
    
    # Change to sources directory
    os.chdir(srcdir)
    
    # Add all files in the list
    for line in filelist:
        fline = line.strip()
        if fline:
            if fline.startswith("#"):
                continue
            else:
                print "addind file: %s" % fline
                tar.add(fline)
                
    # Close package
    print "closing package: %s" % packagename
    tar.close()
    
    # Return to previous dir
    os.chdir(cwd)

if __name__ == "__main__":
    infilename = "config/packagefiles.txt"
    packagename = "nodepackage.tar.gz"
    
    filelist = open(infilename)
    build_package(packagename, filelist)
