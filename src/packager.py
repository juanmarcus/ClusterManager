import os
import tarfile

srcdir = "src"

def build_package():
    
    infilename = "config/packagefiles.txt"
    infile = open(infilename)
    packagename = "clientpackage.tar.gz"
    
    if os.path.exists(packagename):
        print "removing previous package: %s" % packagename
        os.remove(packagename)
    
    print "creating package: %s" % packagename
    tar = tarfile.open(packagename, "w:gz")
    
    os.chdir("./%s" % srcdir)
    for line in infile:
        fline = line.strip()
        if fline:
            if fline.startswith("#"):
                continue
            else:
                print "addind file: %s" % fline
                tar.add(fline)
    print "closing package: %s" % packagename
    tar.close()

if __name__ == "__main__":
    build_package()
