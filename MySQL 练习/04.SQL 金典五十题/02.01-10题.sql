-- 1.查询" 01 "课程比" 02 "课程成绩高的学生的信息及课程分数
-- 利用左查询实现
SELECT * FROM (
	SELECT t1.sid, class1, class2 FROM (
		( SELECT sid, score AS class1 FROM sc WHERE sc.cid = '01' ) AS t1,
		( SELECT sid, score AS class2 FROM sc WHERE sc.cid = '02' ) AS t2
	) WHERE t1.sid = t2.sid AND t1.class1 > t2.class2
)  AS r LEFT JOIN student ON student.sid = r.sid

-- 利用右查询实现
SELECT * FROM student RIGHT JOIN (
	SELECT t1.sid,class1, class2 FROM (
		( SELECT sid, score AS class1 FROM sc WHERE sc.cid = '01' ) AS t1,
		( SELECT sid, score AS class2 FROM sc WHERE sc.cid = '02') AS t2 
	) WHERE t1.sid = t2.sid AND t1.class1 > t2.class2
) r ON student.sid = r.sid


-- 2.查询同时存在" 01 "课程和" 02 "课程的情况
SELECT t1.sid AS '学生ID', t1.语文, t2.数学 FROM (
	( SELECT sid, score AS '语文' FROM sc WHERE sc.cid = '01' ) AS t1,
	( SELECT sid, score AS '数学' FROM sc WHERE sc.cid = '02' ) AS t2
) WHERE t1.sid = t2.sid


-- 3.查询存在" 01 "课程但可能不存在" 02 "课程的情况(不存在时显示为 null )
-- 分析: 由题意可以看出,在查询出 01 课程后的结果是主表数据, 再将结果关联查询02课程数据
-- 利用左查询实现
SELECT t1.sid, t1.class1, t2.class2 FROM 
	( SELECT sid, score AS class1 FROM sc WHERE sc.cid = '01' ) AS t1
LEFT JOIN 
	( SELECT sid, score AS class2 FROM sc WHERE sc.cid = '02') AS t2 
ON t1.sid = t2.sid;

-- 利用右查询实现
SELECT t1.sid, class1, class2 FROM 
	(SELECT sid, score AS class2 FROM sc WHERE sc.cid = '02' ) AS t2
RIGHT JOIN
	( SELECT sid, score AS class1 FROM sc WHERE sc.cid = '01' ) AS t1
ON t1.sid = t2.sid;


-- 查询
SELECT r.sid, class1, class2, class3 FROM (
    SELECT t1.sid, class1, class2 FROM (
        ( SELECT sid, score AS class1 FROM sc WHERE sc.cid = '01' ) AS t1
        LEFT JOIN
        ( SELECT sid, score AS class2 FROM sc WHERE sc.cid = '02' ) AS t2
        ON t1.sid = t2.sid
    ) 
) AS r LEFT JOIN
( SELECT sid, score AS class3 FROM sc WHERE sc.cid = '03') AS t3
ON r.sid = t3.sid


-- 4.查询不存在" 01 "课程但存在" 02 "课程的情况
SELECT sid, cid, score FROM sc WHERE sc.cid = '02' AND sc.sid NOT IN (
	SELECT sid FROM sc WHERE sc.cid = '01'
)


-- 5.查询平均成绩大于等于 60 分的同学的学生编号和学生姓名和平均成绩
-- 知识点: AVG: 内置函数,用于求平均数     GROUP BY: 分组查询      HAVING: 与WHERE用法相同,但是WHERE不能用于分组查询后
SELECT student.sid, student.sname, t1.savg FROM 
	student,
	( SELECT sid, AVG(score) AS savg FROM sc GROUP BY sc.sid HAVING savg > 60 ) AS t1
WHERE
	student.sid = t1.sid


-- 6.查询在 SC 表存在成绩的学生信息
-- DISTINCT: 内置方法,去重;需要注意的是去重字段需要完全一致
SELECT DISTINCT student.* FROM student,sc WHERE student.sid = sc.sid


-- 7.查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩(只查询有成绩的)
SELECT student.sid, student.sname, t1.course_number,  FROM 
	student,
	( SELECT sc.sid, COUNT(sc.cid) AS course_number, SUM(sc.score) AS score_sum FROM sc GROUP BY sc.sid ) AS t1
WHERE student.sid = t1.sid;


-- 8.查询所有同学的学生编号、学生姓名、选课总数、所有课程的总成绩(没成绩的显示为 null )
SELECT student.sid, student.sname, t1.course_number, t1.score_sum FROM student 
LEFT JOIN (
	( SELECT sid, COUNT(sc.cid) AS course_number, SUM(sc.score) AS score_sum FROM sc GROUP BY sc.sid ) AS t1
) ON student.sid = t1.sid;


-- 9.查有成绩的学生信息
-- 如果两个表中,一个数据较大,一个数据较小; 则子查询是大表的用exiss, 子查询是小表的用in
-- 利用IN 实现; 外大内小
SELECT * FROM student WHERE student.sid IN ( SELECT DISTINCT sc.sid FROM sc )

-- 利用EXISTS 实现; 外小内大
SELECT * FROM student WHERE EXISTS ( SELECT sc.sid FROM sc WHERE student.sid = sc.sid )


-- 10.查询「李」姓老师的数量
SELECT COUNT(*) FROM teacher WHERE teacher.tname LIKE '李%'
