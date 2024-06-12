echo "create dir..."
basepath="./data/tar-ceshi"
mkdir -p $basepath && cd $basepath

echo "touch file"
file1="file1.txt"
file2="file2.txt"
touch $file1 && touch $file2

echo "modify file"
file1content=file1
file2content=file2

[ -f $file1 && echo $file1content >> $file1 ]
[ -f $file2 && echo $file2content >> $file2 ]


echo "tar dir"
tarfile="tar-ceshi.tgz"
[ -f $file1 && -f $file2 && tar zcvf $tarfile $file1 $file2 ]
mv $tarfile $tarfile"-"$(date +%Y%m%d%H%M%S)
