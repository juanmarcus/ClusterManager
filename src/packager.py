import os
import tarfile

srcdir = "src"

def build_package():
    
    infilename = "config/packagefiles.txt"
    infile = open(infilename)
    
    os.remove("clientpackage.tar.gz")
    
    tar = tarfile.open("clientpackage.tar.gz", "w:gz")
    
    os.chdir("./%s"%srcdir)
    for line in infile:
        fline = line.strip()
        if fline:
            if fline.startswith("#"):
                continue
            else:
                tar.add(fline)
    tar.close()

if __name__ == "__main__":
    build_package()