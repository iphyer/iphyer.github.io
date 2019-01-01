#! /bin/bash

#获取脚本所在文件目录
#大于1M图片缩小一半




for file in  `find ./ -name "*.[jJ][pP][gG]"`;
    do
   	if [ `stat --printf="%s" $file` -gt 1000000 ]
		then
    		echo $file
    		mogrify -resize 50% $file
		fi

	done

	for file in  `find ./ -name "*.[pP][nN][gG]"`;
    do
    	if [ `stat --printf="%s" $file` -gt 1000000 ]
		then
    		echo $file
    		mogrify -resize 50% $file
		fi
	done


echo "Done"
