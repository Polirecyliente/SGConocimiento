#!/bin/bash
#   File compression

#T# tar, zip, and unzip commands

cd ~/PolirecylBases/tutos/Bash/Section2/
#T# create a tar file from file1 with tar cf tarName.tar file1
tar cvvf tarDebug.tar Section2_2.sh
#T# compress to a fileName.zip with zip fileName file1 file2
zip sections Section2_2.sh Section2_3.sh
#T# compress a dir recursively to a zip with the -r flag
zip -r sectionsRecurs dir1/

#T# list the file contents of a tar file with tar tf tarName.tar
tar tf tarDebug.tar
#T# list the contents of a zip file with unzip -l zipFile.zip
unzip -l zipFile.zip

#T# extract the files from a tar file with tar xf tarName.tar
tar xf tarDebug.tar
#T# unzip to a dir with unzip -d newDir file.zip
unzip -d newDir file.zip
#T# untar to a dir with tar xf tarName.tar -C dirName
tar xf tarDebug.tar -C dirName

#T# you can have verbose output adding v to the options, e.g. 
# tar xvf tarName.tar ; tar cvf tarName.tar file1

#T# for tar, a single hyphen - means read from stdin, it's used to decompress a tar in stdin, e.g. 
# xz -cd file.tar.xz | tar xf -
cat tarDebug.tar | tar xf -

#T# extract the files from a gzip file with tar xzf file.tar.gz
tar xzf file.tar.gz

#T# extract the files from a bzip2 file with tar xjf file.tar.bz2
tar xjf file.tar.bz2