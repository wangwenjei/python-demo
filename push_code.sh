
commit=`date +%Y-%m-%d`

log="代码更新记录: $commit"
echo $log >> ./push_code_log.txt

git add .
git commit -m $commit
git push -u origin master


