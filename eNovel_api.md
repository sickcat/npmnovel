## API

## novel
## IP地址： 192.168.0.110

----
### 进入书架页面
**GET**
`/#/bookshelf?user_id=<user_id>`
|字段|属性|描述|
|----|----|----|
|user_id|str|用户id，建议加盐hash给我|


----
### 进入书本详情页
**GET**
`/#/book/<book_id>?user_id=<user_id>`
book_id 为int型数据
对应表：
|book_id|书本名|描述|
|----|----|----|
|18|改革创新大家谈（第一辑）|测试用书本|


----

### 获取某人剩余未读书本
**GET**
`/#/api/unread?user_id=<user_id>`

Return: json格式
|字段名|类型|描述|
|----|----|----|
|user_id|str|用户唯一id|
|unread|int|剩余多少书未读|
|stat|int|1=success, 0=fail|
|msg|str|具体错误信息，未出错时为空字符串|

Errors：
	- 404 for user not found
	- 500 for internet server error
|字段名|类型|描述|
|----|----|----|
|stat|int|0|
|msg|str|具体错误信息|
