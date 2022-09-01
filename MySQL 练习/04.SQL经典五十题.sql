create database sql_demo;
use sql_demo;
-- 学生表studen
create table student(sid varchar(10),sname varchar(10),sage datetime,ssex varchar(10));
insert into student values('01','赵雷','1990-01-01','男'),('02','钱电','1990-12-21','男'),('03','孙风','1990-12-20','男'),('04','李云','1990-12-06','男'),('05','周梅','1991-12-01','女'),('06','吴兰','1992-01-01','女'),('07','郑竹','1989-01-01','女'),('09','张三','2017-12-20','女'),('10','李四','2017-12-25','女'),('11','李四','2012-06-06','女'),('12','赵六','2013-06-13','女'),('13','孙七','2014-06-01','女');

--  课程表course
create table course(cid varchar(10),cname nvarchar(10),tid varchar(10));
insert into course values('01','语文','02'),('02','数学','01'),('03','英语','03');

-- 教师表teacher
create table teacher(tid varchar(10),tname varchar(10));
insert into teacher values('01','张三'),('02','李四'),('03','王五');

-- 成绩表
create table sc(sid varchar(10),cid varchar(10),score decimal(18,1));
insert into sc values('01','01',80),('01','02',90),('01','03',99),('02','01',70),('02','02',60),('02','03',80),('03','01',80),('03','02',80),('03','03',80),('04','01',50),('04','02',30),('04','03',20),('05','01',76),('05','02',87),('06','01',31),('06','03',34),('07','02',89),('07','03',98);




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















5.查询「李」姓老师的数量
6.查询学过「张三」老师授课的同学的信息
7.查询没有学全所有课程的同学的信息
8.查询至少有一门课与学号为" 01 "的同学所学相同的同学的信息
9.查询和" 01 "号的同学学习的课程 完全相同的其他同学的信息
10.查询没学过"张三"老师讲授的任一门课程的学生姓名
11.查询两门及其以上不及格课程的同学的学号，姓名及其平均成绩
12.检索" 01 "课程分数小于 60，按分数降序排列的学生信息
13.按平均成绩从高到低显示所有学生的所有课程的成绩以及平均成绩
14.查询各科成绩最高分、最低分和平均分:
以如下形式显示:课程 ID，课程 name，最高分，最低分，平均分，及格率，中等率，优良率，优秀率
及格为>=60，中等为:70-80，优良为:80-90，优秀为:>=90
要求输出课程号和选修人数，查询结果按人数降序排列，若人数相同，按课程号升序排列
15.按各科成绩进行排序，并显示排名， Score 重复时保留名次空缺
15.1按各科成绩进行排序，并显示排名， Score 重复时合并名次
16.查询学生的总成绩，并进行排名，总分重复时保留名次空缺
16.1查询学生的总成绩，并进行排名，总分重复时不保留名次空缺
17.统计各科成绩各分数段人数:课程编号，课程名称，[100-85]，[85-70]，[70-60]，[60-0] 及所占百分比
18.查询各科成绩前三名的记录
19.查询每门课程被选修的学生数
20.查询出只选修两门课程的学生学号和姓名
21.查询男生、女生人数
22.查询名字中含有「风」字的学生信息
23.查询同名同性学生名单，并统计同名人数
24.查询 1990 年出生的学生名单
25.查询每门课程的平均成绩，结果按平均成绩降序排列，平均成绩相同时，按课程编号升序排列
26.查询平均成绩大于等于 85 的所有学生的学号、姓名和平均成绩
27.查询课程名称为「数学」，且分数低于 60 的学生姓名和分数
28.查询所有学生的课程及分数情况（存在学生没成绩，没选课的情况）
29.查询任何一门课程成绩在 70 分以上的姓名、课程名称和分数
30.查询不及格的课程
31.查询课程编号为 01 且课程成绩在 80 分以上的学生的学号和姓名
32.求每门课程的学生人数
33.成绩不重复，查询选修「张三」老师所授课程的学生中，成绩最高的学生信息及其成绩
34.成绩有重复的情况下，查询选修「张三」老师所授课程的学生中，成绩最高的学生信息及其成绩
35.查询不同课程成绩相同的学生的学生编号、课程编号、学生成绩
36.查询每门功成绩最好的前两名
37.统计每门课程的学生选修人数（超过 5 人的课程才统计）。
38.检索至少选修两门课程的学生学号
39.查询选修了全部课程的学生信息
40.查询各学生的年龄，只按年份来算
41.按照出生日期来算，当前月日 < 出生年月的月日则，年龄减一
42.查询本周过生日的学生
43.查询下周过生日的学生
44.查询本月过生日的学生
45.查询下月过生日的学生
