
### CSS
css(层叠样式表): 就是给HTML标签添加样式,让他变得更加好看

CSS语法结构
```angular2html
选择器 {
    属性1: 值1;
    属性2: 值2;
    属性3: 值3;
}
```

CSS三种引入方式
```angular2html
1. style标签内直接书写
    <style>
        h1 {
          color: burlywood;
        }
    </style>
2. link标签引入外部CSS文件(最正规的方式)
    <link rel="stylesheet" href="mycss.css">
3. 行内式(一般不用)
    <h1 style="color: green"> Hello CSS </h1>
```

基本选择器
```angular2html
# id原则器
        #d1 {  /*   找到id是d1的标签 将文本颜色改为 greenyellow   */
          color: greenyellow;
        }

# 类原则器
        .c1 {  /*  找到class值包含c1的标签  */
            color: red;
        }

# 元素/标签选择器
        span {  /*  找到所有的span标签  */
            color: aqua;
        }

# 通用选择器
        * {  /*  将HTML页面上所有的标签全部找到  */
            color: burlywood;
        }
```

组合选择器
```angular2html
"""
在前端 我们将标签的嵌套用亲戚关系来表述层级
	<div>div
        <p>div p</p>
        <p>div p
            <span>div p span</span>
        </p>
        <span>span</span>
        <span>span</span>
  </div>
  div里面的p span都是div的后代
  p是div的儿子
  p里面的span是p的儿子 是div的孙子
  div是p的父亲
  ...
"""

# 后代选择器
    div span {  /* div 内部所有的span变为红色 */
        color: red;
    }

# 儿子选择器
    div > span { /* div 内部儿子span变为 burlywood */
        color: burlywood;
    }

# 毗邻选择器
    div + span {  /* 同级别禁挨着的下面的第一个标签 */
        color: aqua;
    }

# 弟弟选择器
    div ~ span { /* 同级别下面所有的span */
        color: aquamarine;
    }
```

属性选择器
```angular2html
"""
1. 含有某个属性
      [username] { /* 将所有含有属性名username的标签背景色改为红色 */
        background-color: red;
      }
2. 含有某个属性并且有某个值
      [username = 'Jason'] {  /* 找到所有属性名是username并且属性值是Jason的标签 */
          background-color: aqua;
      }
3. 含有某个属性并且有某个值的某个标签
      input[username='Tom'] {  /* 找到所有属性名是username并且属性值是Tom的input标签 */
          background-color: khaki;
      }
"""
# 属性选择器是以[]作为标志的

```

分组与嵌套
```angular2html
div,p,span {  /*逗号表示并列关系*/
            color: yellow;
        }
#d1,.c1,span  {
            color: orange;
        }
```

伪类选择器
````angular2html
a:link {  /*访问之前的状态*/
    color: red; 
}

a:hover {  /*需要记住*/
    color: aqua;  /*鼠标悬浮态*/
}

a:active {
    color: black;  /*鼠标点击不松开的状态  激活态*/
}

a:visited {
    color: darkgray;  /*访问之后的状态*/
}

input:focus {  /*input框获取焦点(鼠标点了input框)*/
    background-color: red;
}
````

伪元素选择器
```angular2html
p:first-letter {
            font-size: 48px;
            color: orange;
        }
p:before {  /*在文本开头 同css添加内容*/
            content: '你说的对';
            color: blue;
        }
p:after {
            content: '雨露均沾';
            color: orange;
        }
ps:before和after通常都是用来清除浮动带来的影响:父标签塌陷的问题
```

选择器的优先级
```angular2html
id选择器
类选择器
标签选择器
行内式
    1.选择器相同 书写顺序不同
        就近原则:谁离标签更近就听谁的
    2.选择器不同 ...
        行内 > id选择器  > 类选择器 > 标签选择器
        精确度越高越有效
```

css相关属性
```angular2html
p {
    background-color: red;  背景色
    height: 200px;  高度
    width: 400px;   宽度 
}
```

字体属性
```angular2html
        p {
            font-family: "Arial Black","微软雅黑","...";  /*第一个不生效就用后面的 写多个备用*/

            font-size: 24px;  /*字体大小*/

            font-weight: inherit;  /*bolder lighter 100~900 inherit继承父元素的粗细值*/

            color: red;  /*直接写颜色英文*/
            color: #ee762e;  /*颜色编号*/
            color: rgb(128,23,45);  /*三基色 数字  范围0-255*/
            color: rgba(23, 128, 91, 0.9);  /*第四个参数是颜色的透明度 范围是0-1*/

            /*当你想要一些颜色的时候 可以利用现成的工具
                1 pycharm提供的取色器
                2 qq或者微信截图功能
  							也可以多软件结合使用 
            */
        }
```

文字属性
```angular2html
文字对齐
    text-align: center;  /*居中*/
    text-align: right;
    text-align: left;
    text-align: justify;  /*两端对齐*/

文字划线
    text-decoration: underline;  下划线
    text-decoration: overline;   上划线
    text-decoration: line-through;   删除线
    text-decoration: none;  去除样式  主要用于给a标签去掉自带的下划线
    在html中 有很多标签渲染出来的样式效果是一样的


    font-size: 16px;  文字大小
    text-indent: 32px;   /*缩进32px*/
```

背景属性
```angular2html
background-color: red;  背景色


background-image: url("222.png");  背景图片,默认全部铺满 
background-repeat: no-repeat;  不平铺
background-repeat: repeat-x;  x轴方向平铺
background-repeat: repeat-y;  y轴方向平铺
background-position: center center;  图片展示位置,第一个参数控制左,第二个右


background-attachment: fixed;  
```