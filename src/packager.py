import tarfile

def build_package():
    infilename = "config/packagefiles.txt"
    infile = open(infilename)
    tar = tarfile.open("clientpackage.tar.gz", "w:gz")
    for line in infile.readlines():
        fline = line.strip()
        if fline:
            if fline.startswith("#"):
                continue
            else:
                tar.add(fline)
    tar.close()
    
build_package()