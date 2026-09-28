from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import requests


@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    @filter.command("鸣潮体力")
    async def 鸣潮体力体力(self, event: AstrMessageEvent):
        TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVkIjoxNzkwNTU5ODc5MTMzLCJ1c2VySWQiOjEwNDEyNzY0fQ.8zFlVxyXNQjIa4Ba-wRlNZ_4kf25FxanX4Ru7cbY_kY"  # 图1中完整的token
        DEV_CODE = "54B38FAFA015125A61B99A829BFFBF2F89617B12"
        DISTINCT_ID = "07098ab3-1665-4acb-ba2e-f962c60eaa77"

# 2. 构造请求头 (完全照抄你的抓包数据)
        headers = {
            "Host": "api.kurobbs.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "okhttp/4.12.0", # 一般安卓抓包是这个，如果没有可以留空或自行补充
            "devCode": DEV_CODE,
            "source": "android",
            "version": "3.4.0",
            "versionCode": "30400",
            "token": TOKEN,
            "osVersion": "30",
            "distinct_id": DISTINCT_ID,
            "countryCode": "CN",
            "model": "Pixel 4",
            "lang": "zh-Hans",
            "channelId": "2"
        }

        # 3. 构造请求体 (❗❗请去抓包软件的“请求 -> Text/Raw”中查看实际的请求体内容)
        # 根据图4的响应，大概率需要传这些字段：
        payload = {
            "roleId": "102314104",  # 图4响应里的roleId
            "gameId": "3",          # 图4响应里的gameId
            # "userId": "10412764", # 如果接口需要userId，也请加上
        }

        url = "https://api.kurobbs.com/aki/widget/refresh"

        try:
            # 发送POST请求
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status() # 检查HTTP响应状态码
            
            # 解析JSON
            res_data = response.json()
            
            if res_data.get("code") == 200:
                data = res_data.get("data", {})
                energy = data.get("energyData", {})
                
                role_name = data.get("roleName", "未知角色")
                cur_energy = energy.get("cur", 0)
                total_energy = energy.get("total", 0)
                
                yield event.plain_result(f"=== 鸣潮体力查询 ===\n角色名称: {role_name}\n当前体力: {cur_energy} / {total_energy}\n=========================")
            else:
                yield event.plain_resultf(f"接口请求失败: {res_data.get('msg')}")
                
        except Exception as e:
            yield event.plain_result(f"发生错误: {e}")

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
        
        
    

    


    