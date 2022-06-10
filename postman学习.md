## Postman

## 接口测试的简介和分类

1. 测试外部接口：被测系统和外部系统之间的接口，比如电子商务与支付宝这样的支付系统的测试。（测试正例即可）

2. 测试内部接口：

   1. 内部接口值提供内部系统的使用。比如预算系统、承包系统。（测试正例即可）
   2. 内部接口提供给外部系统使用。（全面测试，测试正例、各种异常场景，权限控制）

3. 接口测试流程以及用例的设计

   1. 拿到接口API文档，（通过抓包工具获取），熟悉接口业务，接口地址，鉴权方式，入参，出参，错误码。
   2. 编写接口用例及评审。
   3. 思路：
      1. 正例：输入正常入参，接口能给个成功返回数据
      2. 反例：
         1. 鉴权返利：鉴权码为空，鉴权码错误，鉴权码过期...
         2. 参数反例：参数为空，参数类型异常，参数长度异常。
         3. 错误码覆盖：根据业务而定。
         4. 其他错误场景：接口黑名单，接口调用次数限制，分页场景，请求方式。
   4. 使用接口测试工具Postman执行接口测试
   5. Postman + Newman + Jenkins实现持续继承，并且输出测试报告&发送右键。

4. 微信公众平台接口 案例

   1. 获取权限
   2. appid（ID）
   3. secret（密钥）

5. 界面介绍 - Workspaces

   1. Collections：集合，项目集合
   2. APIs： API文档
   3. Environments：环境变量
   4. Mock Servers：虚拟服务器
   5. Monitors：监听器（最大一千个监听服务）
   6. History：历史记录

6. 操作界面 之 请求页签（根据params要发送给服务器的请求）

   1. Params：在地址栏有`http://localhost/api/token?grant_type=XX&aapid=XX`，则参数自动填入grant_type以及aapid。主要应用于GET方法的请求传参（主要键值对形式）。
   2. Authorization：鉴权。常用鉴权方式Bearer Token和Basic Auth。
   3. Headers：请求头
   4. Body：请求体。主要用于POST请求传参的地方。
      1. none：没有参数
      2. form-data：既可以传键值对参数，也可以传文件（在VALUE下拉框选择文件或者键值对）。
      3. x-www-form-urlencoded：只能够传键值对参数。
      4. raw：可以传多种参数（菜单行尾选择），如 json、text、xml、 html、 JavaScript 。
      5. binary：把文件以二进制的方式传参。
   5. Pre-request Script：请求之前的脚本。
   6. Tests：请求之后的断言。如可以写`console.log(responseBody)`(console软件下方可以展开查看)
   7. Settings：其他设置。
   8. Cookies：用于管理cookie信息。
   9. ![界面](https://github.com/brant8/mypython/blob/master/pics/postman1.PNG)

7. 操作界面 之 响应页签 （请求过后获得到的信息）

   1. Body：接口返回的数据
      1. Pretty：以Json、html、XML...不同的格式查看返回的数据。
      2. Raw：以文本的方式查看返回的数据。
   2. Preview：以网页的方式查看返回的数据。
   3. Cookies：响应的Cookie信息。
   4. Headers：响应头
   5. Test Results：断言的结果。
   6. `200   OK   681ms   343B`：响应状态码、状态信息、响应的时间、响应的字节数
   7. Save Response：可以选择保存。

8. GET请求一般获取数据，在地址栏使用`?`和`&`方式发送请求

9. POST请求一般提交数据，在Body里面传参请求

10. 在Collections测试时，每个测试都需要打入一大串地址，比如ip地址等。可以在Environments设置环境变量让其地址变得简短

    1. 设置新的环境变量Environments，如 '微信公众平台测试环境'和'微信公众平台生产环境'
    2. 测试环境其设置值有`Variable`值为`ip`，`Initial Value`值为`192.168.0.100`，以及`Current Value`值为`192.168.0.100`
    3. 生产环境设置值有`Variable`值为`ip`，`Initial Value`值为`wx.qq.com`，以及`Current Value`值为`wx.qq.com`
    4. 在Collections中的地址栏可以使用`http://{{ip}}/cgi-bin/...`且需要在右上角选择对应的哪一个环境
    5. 1. ![界面](https://github.com/brant8/mypython/blob/master/pics/postman2.PNG)

11. Environments中的Globals：能够在任何接口下使用。'Create New Environment' 是需要手动切换变量的。

12. 在Tests断言中使用：JSON提取器实现接口关联

    1. 目的：在Collections中测试不同的接口共享Token
    2. 第一次发送请求：`var resutlt = JSON.parse(responseBody)`：把返回的字符串格式的数据转换成对象的形式，可以使用console.log测试。
    3. `pm.globals.set("access_token",result.access_token)`，把access_token设置为全局变量。可在Cookies下方的SNIPPETS小窗口点击Set a global variable一键生成该代码。
    4. 第二次在其他接口中发送请求，即可携带token一起发送。

13. 在Tests断言中使用：正则表达式实现接口关联，match匹配

    1. `var result = responseBody.match(new RegExp('"access_token":"(.*?)"'))`：中的`(.*?)`即为提取出来的值。
    2. 设置为全局变量。注意result提取出来的值为数组，结果使用`result[1]`为token值。

14. Postman内置动态参数以及自定义的动态参数

    1. 内置动态参数形式`{{$}}` （视频中在Body的raw使用JSON测试）
       1. `{{$timestamp}}`生成当前的时间戳
       2. `{{$randomInt}}`生成0-1000之间的随机数
       3. `{{$guid}}`生成随机GUID字符串
    2. 自定义动态参数，（在Body的Pre-request Script中设置）
       1. 比如：手动获得时间戳`var times = Date.now()`
       2. 然后设置成全局变量`pm.globals.set("times",times)`
       3. 再在Body的raw选择JSON获得自定义参数，如 `{"tag":{"name":"时尚{{times}}"}}`

15. 常用Postman断言（Tests右侧SNIPPETS）

    1. `Status code: Code is 200`：检查返回的状态码是否为200
    2. `Response body Contains string`：检查响应中包括指定字符串，检查是否右token
    3. `Response body: Json value check`：检查响应中json的值
    4. `Response body: is equal to a string`：检查响应等于一个字符串
    5. `Response headers:Context-Type`：检查是否包含响应头Content-Type
    6. `Response time is less than 200ms`：检查请求耗时小于200ms
    7. 断言中获取自定义动态参数方式(下面的times为全局变量)
       1. 使用拼接方式`to.include("嘿嘿"+pm.globals.get("times"))`
       2. `to.include("嘿嘿"+pm.globals.("times"))`
       3. 不能直接使用`{{times}}`

16. 批量：鼠标放在Collection项目名上即可看到三个点菜单。

17. Postman之CSV或JSON文件实现数据驱动

18. 测试必须要带的请求头，可通过抓取软件查看正常情况下发送给服务器的请求头是什么样子的。

    1. 抓取软件Progress Telerik Fiddler Web Debugger

19. Mock Servers：在前后端分离，后端未完成的情况下，使用Mock Severs模拟后端API接口及返回值/状态进行测试。

20. Postman的Cookie鉴权

    1. cookie是一段文本，格式key=value。
    2. 当客户端第一次访问服务器的时候，那么服务器就会生成Cookie信息，并且在响应头的set-cookie里面把生成的cookie信息发送给客户端
    3. 当客户第2-N次访问服务器的时候，那么客户端就会在请求头的cookie带上cookie信息，从而实现鉴权。
    4. Cookie分类
       1. 会话cookie，保存在内存，当浏览器关闭之后自动清除
       2. 持久cookie，保存在硬盘，有时效性。

    

