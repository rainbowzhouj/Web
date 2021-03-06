## Web自动化学习
- Selenium的安装
    - 下载selenium的包，如pip方式
    - 安装driver，配置环境变量
- Selenium IDE的录制
    - 适用于新手,下载后直接开始录制使用
    - 一般用火狐较多，谷歌浏览器受网络限制
    - 管理用例suites、代码导出
- Selenium测试用例的编写
    - 导入selenium，利用setup方法启动浏览器，设置窗口大小与隐式等待时间
    - 撰写需要验证的case，利用xpath与css等方式进行元素定位，并操作
    - 利用teardown方法进行退出
- 隐式等待与显示等待
    - 等待的目的是为了防止由于网络原因导致的页面加载元素不出的情况出现
    - 等待的方法
        - 强制等待，time.sleep(1)
        - 隐式等待，driver.implicitly_wait()
        - 显示等待,WebDrvierWait().until()
- 等待的使用
    -  多用显示等待，尽量不用隐式等待与强制等待
- web控件定位为常见操作
    - 常见的定位方式分xpath与CSS_selecter
        -   xpath用法
            - $x('//*[@id="kw"]')  定位百度搜索页面的元素
            - $x('//*[@id="u"]/a[1]')  /为子元素
            - $x('//*[@name="su"]//a')  //为子孙元素
            - $x('//*[@id="s_tab"]//a[1]')
            - $x('//*[@id="s_tab"]//a[last()-1]')
        - css用法
            - $('#wd')
            - $('[name=wd]')
            - $('#s_tab>b')
            - $('#s_tab a:nth-child(2)')
            - $('#s_tab>a:nth-last-child(2)')  空格为子孙，>为子元素
- web控件的交互进阶
    - ActionChains：执行PC端鼠标点击，双级，右键，拖拽等事件
    - TouchActions：模拟PC端和移动端的点击，滑动、拖拽，多点触控等多种手势操作