## API

## novel
## IP地址： 20.97.6.101
## 端口： 8080 web服务端口（api）
## 端口： 5888 后台系统端口

----
### 进入书架页面
**GET**
`:8080/#/bookshelf?user_id=<user_id>`
|字段|属性|描述|
|----|----|----|
|user_id|str|用户id，建议加盐hash给我|


----
### 进入书本详情页
**GET**
`:8080/#/book/<book_id>?user_id=<user_id>`
book_id 为int型数据
对应表：
|book_id|书本名|描述|
|----|----|----|
|4|改革创新大家谈（第一辑）|测试用书本|
|5|改革创新大家谈（第二辑）|测试用书本|


----

### 获取某人剩余未读书本
**GET**
`:8080/api/unread?user_id=<user_id>`
`:5888/api/unread?user_id=<user_id>`

Return: json格式,用户不存在时返回所有书籍数目，相当于一本未读
|字段名|类型|描述|
|----|----|----|
|user_id|str|用户唯一id|
|unread|int|剩余多少书未读|
|stat|int|1=success, 0=fail|
|msg|str|具体错误信息，未出错时为空字符串|

Errors：
	- 500 for internet server error
|字段名|类型|描述|
|----|----|----|
|stat|int|0|
|msg|str|具体错误信息|
