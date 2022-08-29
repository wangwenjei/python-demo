drop database sql_test;
create database sql_test charset=utf8mb4 collate=utf8mb4_unicode_ci;

-- 创建教师表
create table teacher (
    tid int not null primary key auto_increment comment '教师ID',
    tname varchar(25) not null comment '教师姓名'
) comment '教师表';

-- 创建学生表
create table student (
    sid int not null primary key auto_increment comment '学生ID',
    sname varchar(25) not null comment '学生姓名',
    sage datetime not null comment '入学时间',
    ssex enum('f','m','o') not null default 'm' comment '性别:f(女),m(男,默认男),o(其他)'
) comment '学生信息表';

-- 创建课程表
create table course (
    cid int not null primary key auto_increment comment '课程ID',
    cname varchar(25) not null comment '课程名称',
    tid int not null comment '教师ID'
) comment '课程信息表';

-- 创建成绩表
create table sc (
    sid int not null comment '学生ID',
    cid int not null comment '课程ID',
    score float unsigned not null comment '分数'
) comment '学生成绩表';

-- 录入教师信息
insert into teacher(tid,tname) values(1,'曹操'),(2,'刘备'),(3,'孙权');

-- 录入学生信息
insert into student(sname,sage,ssex) values('张辽','1990-12-21 09:17:26','m'),('乐进','1990-12-21 09:37:38','m'),('于禁','2013-06-13 11:11:11','m'),('张郃','2014-06-01 19:27:38','m'),('徐晃','1990-12-20 09:57:58','m'),('甄宓','1991-12-01 13:17:18','f');
insert into student(sname,sage,ssex) values('关羽','1992-01-01 09:17:26','m'),('张飞','1989-01-01 05:17:38','m'),('赵云','2017-12-20 22:22:22','m'),('马超','2017-12-25 17:27:18','m'),('黄忠','2012-06-06 09:27:58','m'),('黄月英','1990-01-01 03:17:18','f');
insert into student(sname,sage,ssex) values('甘宁','1990-12-21 15:27:18','m'),('徐盛','2013-06-13 11:11:11','m'),('凌统','2014-06-01 23:27:58','m'),('程普','1990-12-20 12:37:48','m'),('韩当','1991-12-01 17:17:18','m'),('孙尚香','1992-01-01 05:27:18','f');

-- 录入课程信息
insert into course(cname,tid) values('语文',1),('数学',2),('英语',3);

-- 录入学生成绩
insert into sc(sid,cid,score) values(1,1,80.0),(2,1,70.0),(3,1,80.0),(4,1,50.0),(5,1,76.0),(6,1,31.0),(7,1,80.0),(8,1,78.0),(9,1,93.0),(10,1,46.0),(11,1,75.0),(12,1,92.0),(13,1,65.0),(14,1,48.0),(15,1,56.0),(16,1,99.0),(17,1,80.0),(18,1,93.0);
insert into sc(sid,cid,score) values(1,2,90.0),(2,2,60.0),(3,2,80.0),(4,2,30.0),(5,2,87.0),(6,2,80.0),(7,2,89.0),(8,2,80.0),(9,2,45.0),(10,2,13.0),(11,2,80.0),(12,2,99.0),(13,2,56.0),(14,2,49.0),(15,2,98.0),(16,2,87.0),(17,2,88.0),(18,2,91.0);
insert into sc(sid,cid,score) values(1,3,99.0),(2,3,80.0),(3,3,80.0),(4,3,20.0),(5,3,80.0),(6,3,34.0),(7,3,98.0),(8,3,66.0),(9,3,99.0),(10,3,18.0),(11,3,69.0),(12,3,87.0),(13,3,79.0),(14,3,50.0),(15,3,18.0),(16,3,57.0),(17,3,89.0),(18,3,97.0);



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
SELECT student.sid, student.sname, r.avg_score FROM student RIGHT JOIN (
SELECT sc.sid,AVG(sc.score) AS avg_score FROM sc WHERE sc.score < 60 GROUP BY sc.sid HAVING COUNT(score) > 1
) r
ON r.sid = student.sid
