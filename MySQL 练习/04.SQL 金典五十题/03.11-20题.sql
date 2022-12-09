-- 11.查询学过「张三」老师授课的同学的信息
SELECT * FROM student WHERE student.sid IN (
	SELECT sc.sid FROM sc WHERE sc.cid IN ( 
		SELECT tid FROM teacher WHERE teacher.tname = '张三' 
	) 
)


-- 12.查询没有学全所有课程的同学的信息
SELECT * FROM student WHERE student.sid NOT IN (
	SELECT sc.sid FROM sc GROUP BY sc.sid HAVING COUNT(sc.cid) = (SELECT COUNT(*) FROM course)
)


-- 13.查询至少有一门课与学号为" 01 "的同学所学相同的同学的信息
-- 关联查询实现
SELECT DISTINCT student.* FROM student LEFT JOIN sc ON student.sid = sc.sid WHERE
	sc.cid IN ( SELECT cid FROM sc WHERE sid = '01') AND
	student.sid != '01';

-- 子查询实现
SELECT * FROM student WHERE student.sid IN (
	SELECT DISTINCT sc.sid FROM sc, student WHERE sc.cid IN (
		SELECT sc.cid FROM sc WHERE sc.sid = '01'  -- 01 学生学习课程
	)
) AND student.sid != '01'


-- 14.查询和" 01 "号的同学学习的课程 完全相同的其他同学的信息
SELECT * FROM Student WHERE student.sid IN (
	SELECT sid FROM sc WHERE 
		sc.sid != '01' AND -- 排除01自身
		sid NOT IN (SELECT sid FROM sc WHERE cid NOT IN (SELECT cid FROM sc WHERE sc.sid = '01') -- 去除所选课程中01学生未选课程的人
	) GROUP BY sc.sid HAVING COUNT(cid) = (SELECT COUNT(cid) FROM sc WHERE sc.sid = '01') -- 分组统计,与01学生所选课程数相同的人
)


-- 15.查询没学过"张三"老师讲授的任一门课程的学生姓名
SELECT * FROM student s WHERE s.sid NOT IN (
	SELECT t2.sid,t2.sid FROM 
		(SELECT cid FROM course WHERE tid = (SELECT tid FROM teacher WHERE  teacher.tname = '张三')) AS t1 -- 获取到张三老师教授的课程ID
	LEFT JOIN 
		sc t2 ON t1.cid = t2.cid  
)


SELECT * FROM student  WHERE sid NOT IN (
	SELECT s.sid FROM student s
	LEFT JOIN sc ON s.sid = sc.sid
	LEFT JOIN course c ON sc.cid =  c.cid
	LEFT JOIN teacher t ON c.tid = t.tid WHERE t.tname = '张三'
)


-- 16.查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
SELECT s.sid, s.sname, t1.score_avg FROM (
	SELECT sid,AVG(score) AS score_avg  FROM sc WHERE sc.score < 60 GROUP BY sid HAVING COUNT(cid) > 1 
) AS t1
LEFT JOIN student s ON t1.sid = s.sid


-- 17.检索" 01 "课程分数小于 60，按分数降序排列的学生信息以及学生成绩
SELECT s.* ,t1.score FROM (
	SELECT sid,score FROM sc WHERE sc.cid = '01' AND sc.score < 60 ORDER BY sc.score DESC
) AS t1
LEFT JOIN student s ON s.sid = t1.sid



-- 18.按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
SELECT * FROM sc LEFT JOIN (
	SELECT sid, AVG(score) AS score_avg FROM sc GROUP BY sc.sid
) t ON t.sid = sc.sid ORDER BY score_avg DESC


-- 19.查询各科成绩最高分、最低分和平均分:
以如下形式显示:课程 ID，课程 name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
及格为>=60，中等为:70-80，优良为:80-90，优秀为:>=90
要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
SELECT 
	sc.cid,course.cname,
	MAX(sc.score) AS 最高分,
	MIN(sc.score) AS 最低分,
	AVG(sc.score) AS 平均分,
	COUNT(*) AS 选修人数,
	SUM(CASE WHEN sc.score >= 60 THEN 1 ELSE 0 END) / COUNT(*) AS 及格率,
	SUM(CASE WHEN sc.score >= 70 AND sc.score < 80 THEN 1 ELSE 0 END) / COUNT(*) AS 中等率,
	SUM(CASE WHEN sc.score >= 80 AND sc.score < 90 THEN 1 ELSE 0 END) / COUNT(*) AS 优良率,
	SUM(CASE WHEN sc.score >= 90 THEN 1 ELSE 0 END) / COUNT(*) AS 优秀率
FROM sc,course
WHERE sc.cid = course.cid
GROUP BY sc.cid,course.cname
ORDER BY 选修人数 DESC, sc.cid ASC


-- 20.按各科成绩进行排序，并显示排名， Score 重复时保留名次空缺

