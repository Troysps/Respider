Respider 爬虫框架架构设计

架构参照(Scrapy框架):

Scrapy: 执行引擎控制数据流:

    1. 引擎从自定义爬虫中获取初始化请求
    2. 引擎把该请求放入调度器中, 同时在调度器中获取一个待下载的请求(两个步骤 异步执行)
    3. 调度器返回一个待下载的请求给引擎
    4. 引擎将请求发送给下载器, 中间经过一系列下载中间键(例如 process_request)
    5. 一旦下载完成在下载器中生成一个响应对象, 中间经过一系列下载中间键(例如 process_request())
    6. 引擎从下载器获取一个响应对象, 将该响应对象发送到爬虫, 中间经过爬虫中间键(例如 process_spider_input())
    7. 爬虫处理该响应, 完成用户逻辑之后, 返回结果对象以及新的请求给引擎, 中间经过爬虫中间键(例如 process_spider_output())
    8. 引擎将结果对象发送给结果处理器, 将请求发送给调度器
    9. 从1开始重复执行，直到调度器中没有新的请求处理

任何爬虫框架程序共同的流程：

1. 构建入口请求
2. 发送请求返回响应
3. 解析响应，处理数据 ： 如果是请求继续发送；如果是需要保存的数据，做保存
4. 当所有请求发送完毕，程序结束。


一、确立数据对象
(http)
1. Request                  请求对象
2. Response                 响应对象

3. Item                     数据对象 --- 字典形式保存

二、核心组件(core)
1. Spider --- 爬虫组件(用户自定义组件)
    提供功能:
        <p>初始化url请求, 传入Request对象中</p>
        <p>解析Response返回对象数据, 传入Item对象中</p>

2. Schedule --- 调度器组件
    提供功能:
        <p>获取Request对象, 接受并保存</p>
        <p>实现去重功能</p>

3. Downloader --- 下载器组件
    提供功能:
        <p>接受Request对象, 并发出请求, 获取响应返回给Response对象</p>

4. Pipeline --- 管道组件
    提供功能:
        <p>接受Item对象, 处理数据</p>

5. Engine --- 引擎组件
    提供功能:
        协调各组件
        对外提供接口


三、中间件(middlewares)
1. SpiderMiddlewares  --- 爬虫中间件
    提供功能:
        <p>处理从Spider交给Engine的请求对象(Request)</p>
        <p>处理从Spider交给Engine的数据对象(Item)</p>

2. DownloaderMiddlewares --- 下载器中间件
    提供功能:
        <p>处理从Engine交给Downloader的请求对象(Request)</p>
        <p>处理从Downloader交给Engine的响应对象(Response)</p>/
        
        
目录结构:
    -- core
        -- Spider
        -- Schedule
        -- Downloader
        -- Pipeline
        -- Engine
    -- http
        -- Request
        -- Response
    -- middlewares
        -- SpiderMiddlewares
        -- DownloaderMiddlewares
    -- Item     