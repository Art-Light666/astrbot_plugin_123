from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
players = {}


@register("helloworld", "YourName", "一个简单的 Hello World 插件", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("helloworld")
    async def helloworld(self, event: AstrMessageEvent):
        """这是一个 hello world 指令""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        logger.info(message_chain)
        yield event.plain_result(f"Hello, {user_name}, 你发了 {message_str}!") # 发送一条纯文本消息

    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
    @filter.command("签到")
    async def qd(self, event: AstrMessageEvent):
        """这是一个 签到 指令""" 
        user_name = event.get_sender_name()
        message_str = event.message_str # 用户发的纯文本消息字符串
        message_chain = event.get_messages() # 用户所发的消息的消息链 # from astrbot.api.message_components import *
        yield event.plain_result(f"Hello, {user_name}, 您今日已完成签到") # 发送一条纯文本消息
class Player: 
    HP = 100
    Atk = 10
    Dfc = 5
    level = 0
    exp = 0
    @filter.command("创建角色")    
    async def create(self,event: AstrMessageEvent):
        user_name = event.get_sender_name()
        if user_name not in players:
            players[user_name] = Player()
            yield event.plain_result(f"At{user_name},角色创建成功啦")
        else:
            yield event.plain_result(f"At{user_name},您已创建过角色哦")
    @filter.command("修炼")            
    async def exercise(self,event: AstrMessageEvent):
        user_name = event.get_sender_name()
        if user_name in players:
            players[user_name].exp = players[user_name].exp + 100
            yield event.plain_result(f"At{user_name},修炼完毕,经验+100")
        else:
            yield event.plain_result(f"At{user_name},您还未创建角色哦")
    @filter.command("属性")
    async def askexp(self, event: AstrMessageEvent):
        user_name = event.get_sender_name()
        if user_name in players:
            yield event.plain_result(f"@{user_name}的信息如下\n生命{players[user_name].hp}\n攻击{players[user_name].atk}\n防御{players[user_name].dfc}\n经验值{players[user_name].exp},满100经验可使用'升级'指令升级哦\n技能点数:{players[user_name].point}")
        else :
            yield event.plain_result(f"@{user_name},您还未创建角色哦")
    @filter.command("升级")
    async def levelup(self,event: AstrMessageEvent):
        user_name = event.get_sender_name()
        if user_name in players and players[user_name].exp >= 100:
            players[user_name].exp = players[user_name].exp - 100
            players[user_name].level = players[user_name].level + 1
            players[user_name].hp = players[user_name].hp + 10
            players[user_name].point = players[user_name].point + 1
        yield event.plain_result(f"@{user_name},升级成功！可输入'属性'指令查询各项数值")
    @filter.command("列表")
    async def ask(self,event: AstrMessageEvent):
        yield event.plain_result(f"当前有{len(players)}名玩家注册\n{players.keys}")
        
        
        
        
    

    


    