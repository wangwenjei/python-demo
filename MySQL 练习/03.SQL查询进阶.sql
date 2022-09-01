# https://blog.csdn.net/weixin_43348955/article/details/120481733

-- 01. 查询
select * from student RIGHT JOIN (
    select t1.sid, class1, class2 from
          (select SId, score as class1 from sc where sc.cid = '01')as t1, 
          (select SId, score as class2 from sc where sc.cid = '02')as t2
    where t1.sid = t2.sid AND t1.class1 > t2.class2
)r 
on student.sid = r.sid;


-- 14. 查询和" 01 "号的同学学习的课程完全相同的其他同学的信息
SELECT * FROM student WHERE student.sid In (
	SELECT A.sid FROM  (
		( SELECT sc.sid,GROUP_CONCAT(sc.cid order by sc.cid)  AS courses FROM sc   GROUP BY sc.sid ) AS A,
		( SELECT GROUP_CONCAT(sc.cid order by sc.cid) AS courses FROM sc WHERE sc.sid = 1 GROUP BY sc.sid ) B
	) WHERE A.courses = B.courses
) AND student.sid <> 1



-- 16. 查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
SELECT student.sid, student.sname, r.avg_score FROM student RIGHT JOIN) r
ON r.sid = student.sid

