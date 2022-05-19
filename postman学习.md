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
   6. Tests：请求之后的断言。
   7. Settings：其他设置。
   8. Cookies：用于管理cookie信息。
7. 操作界面 之 响应页签 （请求过后获得到的信息）
   1. Body：接口返回的数据
      1. Pretty：以Json、html、XML...不同的格式查看返回的数据。
      2. Raw：以文本的方式查看返回的数据。
      3. Preview：以网页的方式查看返回的数据。
   2. Cookies：响应的Cookie信息。
   3. Headers：响应头
   4. Test Results：断言的结果。
   5. `200   OK   681ms   343B`：响应状态码、状态信息、响应的时间、响应的字节数
   6. Save Response：可以选择保存。

