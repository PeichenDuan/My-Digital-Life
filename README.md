My-Digital-Life（我的数字生命）脚本使用说明

一、写在前面

本脚本采用Python的wxauto库（https://github.com/cluic/wxauto ）以及讯飞星火大模型提供的免费API，在电脑端实现微信消息全自动回复，全流程免费且无需使用VPN。请不要将此脚本用作商用，祝您使用愉快！


二、使用前准备

库的安装：

使用脚本之前首先要安装Python（版本大于3.8），并确保你的Python已经配置了以下库：wxauto、requests和spark_ai_python，未安装的可按照如下操作安装：

1.Win+R 打开电脑运行对话框界面输入“CMD”，在打开的界面输入“pip install wxauto”；

2.Win+R 打开电脑运行对话框界面输入“CMD”，在打开的界面输入“pip install requests”；

3.Win+R 打开电脑运行对话框界面输入“CMD”，在打开的界面输入“pip install --upgrade spark_ai_python”。

三个库全部安装完成后便成功了三分之一。

API的获取：

1.登录讯飞星火大模型官网（https://xinghuo.xfyun.cn/ ）；

2.右上角点击注册账号，登录后点击新界面左下角的“API接入”；

3.点击新界面的“在线调试”，进入“我的应用>创建应用”界面；

4.输入应用名称、应用分类（推荐“通讯社交”中的“聊天社交”）和应用功能描述；

5.创建完成后需要领取tokens（相当于你能让AI说的总字数），点击新界面左侧“星火认知大模型”中的“Spark Light”（这个是免费领无限tokens，其他付费的需要参考），系统会提醒你做实名认证；

6.实名认证选个人实名认证就行，填写相关信息后等待人工认证，速度快的话几十秒就通过了；

7.实名认证完成后回到刚才“星火认知大模型”中“Spark Light”的界面，左侧点击“领取无限量”，右侧查看你的APPID、APISecret和APIKey（这三个一会儿脚本里要填）；

太棒了！现在你创建了自己的API，成功了三分之二。

脚本的下载、编辑与运行：

1.点击“我的数字生命.py”脚本到电脑上的任意路径；

2.鼠标右键点击脚本，用Notepad打开查看代码，代码如下：
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

    import time
    from wxauto import *
    from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
    from sparkai.core.messages import ChatMessage
    import re
    
    wx = WeChat()
    
    while True:
    
        c = "不要回答"
        
        msgs = wx.GetNextNewMessage()
        
        if "XXX" in msgs:
            a = msgs["XXX"]
            for b in a:
                if b[0] == "XXX":
                    c = b[1]
                    print(c)
    
        if c != "不要回答":
    
            # 星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
            SPARKAI_URL = 'wss://spark-api.xf-yun.com/v1.1/chat'
            # 星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
            SPARKAI_APP_ID = '填写你的APP_ID'
            SPARKAI_API_SECRET = '填写你的API_SECRET'
            SPARKAI_API_KEY = '填写你的API_KEY'
            # 星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
            SPARKAI_DOMAIN = 'general'
    
            if __name__ == '__main__':
                try:
                    spark = ChatSparkLLM(
                        spark_api_url=SPARKAI_URL,
                        spark_app_id=SPARKAI_APP_ID,
                        spark_api_key=SPARKAI_API_KEY,
                        spark_api_secret=SPARKAI_API_SECRET,
                        spark_llm_domain=SPARKAI_DOMAIN,
                        streaming=False,
                    )
                    handler = ChunkPrintHandler()
                    user_input = c
                    messages = [ChatMessage(
                        role="user",
                        content=user_input
                    )]
                    response = spark.generate([messages], callbacks=[handler])
                    # Print the entire response for debugging
                    print("Full response:", response)
                    # Extract text within quotes
                    text_in_quotes = re.findall(r"text='([^']*)'", str(response))
                    if text_in_quotes:
                        print(text_in_quotes[0])
                    else:
                        print("No text found in response.")
                except Exception as e:
                    print(f"An error occurred: {e}")
    
            # 获取当前微信客户端
            wx = WeChat()
    
            # 获取会话列表
            wx.GetSessionList()
    
            # 向某人发送消息（以`XXX`为例）
            msg = text_in_quotes[0]
            who = 'XXX'
            wx.SendMsg(msg, who)  # 向`XXX`发送消息
    
        # 等待10秒
        time.sleep(10)
——————————————————————————————————————————————————————————————————————————————————————————————————————————————————

其中有几处需要自行编辑的地方（按从上到下顺序）：

        c = "不要回答"
引号里的可改成任意文字，当对方输入这个文字后将不会得到你的AI的回复；

        if "XXX" in msgs:
            a = msgs["XXX"]
            for b in a:
                if b[0] == "XXX":
                    c = b[1]
                    print(c)
这部分里的三个“XXX”需要改成你想要使用AI进行聊天的一个微信好友的名字（三个“XXX”改成同一个名字）（是你自己聊天时给好友备注的名字）（别忘了打英文引号）；


      if c != "不要回答":
引号里的可改成任意文字，但要与上面该的保持一致，当对方输入这个文字后将不会得到回复；

            SPARKAI_APP_ID = '填写你的APP_ID'
            SPARKAI_API_SECRET = '填写你的API_SECRET'
            SPARKAI_API_KEY = '填写你的API_KEY'
这三行藏在“#星火认知大模型...”那一坨里，三个引号里文字改成你记录的APPID、APISecret和APIKey；

            who = 'XXX'
脚本倒数第三行，同样是把“XXX”改为你的好友名，与前面填的三个保持一致；

    time.sleep(10)
这个在脚本的最后一行，括号里的数字为刷新时间，如填“10”则表示每隔10秒检测是否有新消息，可以改成别的数字，最好不要太小（容易崩）。

全部改完，搞定收工，别忘了保存修改后的脚本，关闭修改界面，现在可以测试它了。


三、运行脚本

养兵千日用兵一时，终于到了使用脚本的时候了。

打开你的电脑版微信到聊天窗口，双击脚本，会弹出一个窗口，记录你的新消息以及AI帮你回复的内容。

让你在脚本里编辑的好友给你发条消息，如果电脑自动打开聊天窗口并编辑信息发送，那么恭喜你，建立了自己的第一个数字生命！

之后你还可以在讯飞官网训练自己的大模型，作出属于你自己风格的聊天AI~


四、后记

这个东西是作者在研究AI在生物学领域应用的时候一拍脑袋想出来的，也是借助AI之力花了半天时间才捣鼓出了第一版，之后可能会做一些优化，如增加同时AI聊天的好友数等。

AI大模型的建设过程少不了海量信息的纳入，这意味着一切你能看到的AI的回答其实都是基于已有的信息迭代产生的。“如何不被AI取代”这个问题的答案其实很简单，那就是：不断创新，突破原有框架。

最后引用《海上钢琴师》的台词作为结尾————

    "Take a piano.
    The keys begin,the keys end.
    You know there are eighty-eight of them, nobody can tell you any difference.
    They are not infinite.
    You are infinite.
    And on these keys the music that you can make is infinite."
