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

