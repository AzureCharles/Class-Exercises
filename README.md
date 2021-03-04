# 基于关键词的GitHub仓库信息简单爬虫（分装版）

## 程序简介

本程序支持基于用户输入关键词的自动爬取，支持csv文档存储爬取结果，并提供了MongoDB数据库的存储接口。

主要爬取信息如下：

* 仓库名称

* 仓库链接

* 作者主页链接

* star数

* fork数

## 程序结构

与大多数标准爬虫程序类似，本程序主要数据流示意图如图所示：

![module and data flow](https://user-images.githubusercontent.com/71918203/109914471-06500b80-7ceb-11eb-8657-9ab5b8d9d3bd.png)

各模块名称与对应功能如下：

* __Superman__：启动/调度模块，主要负责调度，包括各种参数的指定；

* __ParaHtml__：解析模块，解析下载器下载的页面；

* __SaveData__：数据存储模块，将ParaHtml解析返回的数据写入文档；

* __UrlManage__：地址管理模块，处理解析的新url；

* __Download__：页面加载模块，用于加载新的页面。

## 程序使用说明

建议用户按照如下步骤使用本程序：

### 1）设置cookie与user-agent

用户可进入DownLoad模块对应位置进行设置。

![cookie and user-agent](https://user-images.githubusercontent.com/71918203/109914777-a3ab3f80-7ceb-11eb-8321-d64c33c57fe8.png)

### 2）配置MongoDB相关服务

有需求的用户需要完成数据库服务配置，并进入SaveData模块更改服务器地址。

![database server](https://user-images.githubusercontent.com/71918203/109914961-f7b62400-7ceb-11eb-9c77-ca9065d084b9.png)

亦可禁用MongoDB入口，在启动模块中将此行变为注释。

![MongoDB entry](https://user-images.githubusercontent.com/71918203/109915189-57143400-7cec-11eb-99d8-1fd05805e4c8.png)

### 3）启动程序

设置完毕后，用户可进入程序所在目录，在命令行窗口下输入命令：

```python SuperMan```

即可启动爬虫程序。

## 使用注意

本程序对网络状况和响应时间要求较高，建议用户挂载代理服务运行。
