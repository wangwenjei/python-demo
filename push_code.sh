
commit=`date +%Y-%m-%d`


git add .
git commit -m $commit
#git push -u origin master

log="代码更新记录: $commit"
echo >> ./push_code_log.txt
