# Python自动化测试开发框架

### Github准备

1. 创建目录，开启本地Repo

   ```bash
   git init
   ```

2. 从远程获取已有的Repo

   ```bash
   git remote add origin https://github.com/brant8/mypython.git
   ```

3. 抓取最新远程Repo资源

   ```bash
   git pull origin master
   ```

4. 可在本地进行编辑后，按照正常步骤提交即可push到remote



### 市场行情

1.主流接口测试工具实现自动化（中小型）

​	Postman + Newman + Git/Svn + Jenkins（基于Javascript语言）

​	Jmeter + Ant + Git/Svn + Jenkins （基于Java和BeanShell语言）接口自动化

2.基于代码的接口自动化（中大型）

 	Python + Request + Yami +Pytest + Allure + Logging + 热加载 + Jenkins齿形继承接口自动化

3.基于平带的接口自动化（适用于特大型/外包型）

​	测试开发



### Requests模块以及常用方法

1.Requests模块用于发送Http请求以及接口http响应的，python的第三方库

```bash
#安装命令
> pip install requests
```

2.查看已安装的库

```bash
> pip list
Package            Version
------------------ ---------
certifi            2023.7.22
charset-normalizer 3.3.0
idna               3.4
pip                21.1.2
requests           2.31.0
setuptools         57.0.0
urllib3            2.0.6
wheel              0.36.2
```

3.Requests模块常用的函数

​	get、request、post、session、put、delete

```bash
def get(url, params=None, **kwargs):
def post(url, data=None, json=None, **kwargs):
def put(url, data=None, **kwargs):
def delete(url, **kwargs):
#request方法是上述四个方法的底层调用
def request(method, url, **kwargs):
def session():

#request里最后返回的是Session对象的request方法，即：
def request(
        self,
        method,
        url,
        params=None,			#get请求传参
        data=None,				#post活put请求传参
        headers=None,			#post请求传参
        cookies=None,			#Cookie信息
        files=None,				#文件上传
        auth=None,				#鉴权
        timeout=None,			#超时处理
        allow_redirects=True,	#是否允许重定向
        proxies=None,			#代理
        hooks=None,				#钩子
        stream=None,			#文件下载
        verify=None,			#证书验证
        cert=None,				#CA证书
        json=None,				#post请求传参
    ):
```

​	`post`请求中`data`传参和`json`传参的区别：

​		在Postman中的`POST`**传参**是在`Body`中。

​			`form-data` 对应`[files?]`：文件上传。且在`Headers`中的`Content-Type`需要使用`multipart/form-data`

​			`x-www-form-urlencoded` 对应`[data?]`：表单。在`Headers`中使用`Content-Type:application/x-www-form-urlencoded`

​			`raw`：文本，`Headers`中具有多个选择

​						1.`Content-Type:application/json`		对应`[json]`

​						2.`Content-Type:text/plain`					对应`[data?]`

​						3.`				Content-Type:application/javascript`			对应`[data?]`		

​						4.`Content-Type:text/html` 					对应` [data?]`

​						5.`Content-Type:application/xml`  		对应`[data?]`

​			`binary`对应`[files?]`：二进制。`Content-Type:application/content-stream`		

4. Response对象

   ```bash
   res.text 	#返回文本格式
   res.content	#返回bytes类型数据
   res.json()	#返回json数据
   res.status_code	#返回状态码
   res.reason	#返回状态信息
   res.cookies	#返回cookie信息
   res.encoding	#返回编码格式
   res.headers	#返回响应头
   res.request.???	#返回请求的信息和数据
   ```

### 接口自动化实战和封装

1. 基于pytest单元测试框架，默认测试用例的规则：

   1. 模块（py文件）名必须以`test_`开头活`_test`结尾
   2. 类名必须Test开头
   3. 用例名必须以`test_`开头

2. 代码示例

   ```bash
   import pytest as pytest
   import requests
   
   class TestApi:
       def test_get_token(self):
           print("/n打印入口")
           #方式一 url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET"
           url = "https://api.weixin.qq.com/cgi-bin/token"
           datas = {
               "grant_type":"client_credential",
               "appid": "wx74a8627810cfa308",
               "secret": "e40a02f9d79a8097df497e6aaf93ab80",
           }
           #kwargs
           res = requests.get(url=url, params=datas)
           print(res.json())
           # requests.post()
           # requests.put()
           # requests.delete()
           # requests.session()
           # requests.request()
   
   if __name__ == '__main__':  #入口
       #若无法自动安装，手动安装命令：pip install pytest
       pytest.main()
       
       
   #输出：
   ============================== 1 passed in 1.29s ==============================
   
   Process finished with exit code 0
   PASSED                              [100%]/n打印入口
   {'access_token': '73_9BnvFZTyARe6S2NNonoLXXppXnS4P2fwKEm7gCBBsvnV3dH__DhN5SPA-0HkWj2ITmWpUrfKyJFOywsMwQ3vuyZ5_-EcGhQf5V1Kdwt3dlkYb2_VUZDaVdYjMHERKMeAHADWY', 'expires_in': 7200}
   ```

3. 提示：json是字典的字符串格式，两者可以相互转换

4. 示例2

   ```bash
   import pytest as pytest
   import requests
   
   
   class TestApi:
       access_token = ""   #为第二个例子保留信息
       #获取鉴权码
       def test_get_token(self):
           print("/n打印入口")
           #方式一 url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=APPID&secret=APPSECRET"
           url = "https://api.weixin.qq.com/cgi-bin/token"
           datas = {
               "grant_type":"client_credential",
               "appid": "wx74a8627810cfa308",
               "secret": "e40a02f9d79a8097df497e6aaf93ab80",
           }
           #kwargs
           res = requests.get(url=url, params=datas)
           result = res.json()
           TestApi.access_token = result["access_token"]
           print(res.json())
           print("---获取鉴权码---")
           # requests.post()
           # requests.put()
           # requests.delete()
           # requests.session()
           # requests.request()
   
       #编辑标签接口
       def test_edit_flag(self):
           url = "https://api.weixin.qq.com/cgi-bin/tags/update?access_token="+TestApi.access_token
           data = None, #data一般表示表单，键值对形式
           json = {"tag": {"id":134,"name":"广东人"}}  #json一般表示json，即json格式
           res = requests.post(url=url,json=json)
           print(res.json())
           print("---编辑标签接口---")
   
       #文件上传
       def test_file_upload(self):
           url = "https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token="+TestApi.access_token
           datas = {
               #"media":open("I:\\Download\\load.jpg",encoding="utf-8",mode="rb")     #二进制（mode）不能使用encoding，二选其一
               "media":open("I:\\Download\\load.jpg",mode="rb")     #上传图片要先打开该文件
           }
           res = requests.post(url=url,files=datas)
           print(res.json())
           print("---文件上传---")
   
   if __name__ == '__main__':  #入口
       #若无法自动安装，手动安装命令：pip install pytest
       #pytest.main(['-vs'])    # [-vs] 打印调试信息
       pytest.main()    # [-vs] 打印调试信息
   ```

5. 上述方式不好，因为当获取token失败后，会导致其他测试无法继续下去



### 接口自动化框架封装

1.

​	









































