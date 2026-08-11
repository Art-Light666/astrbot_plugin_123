from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
list = []
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
class player(Star): 
    def __init__(self):
        self.hp = 100
        self.atk = 10
        self.dfc = 10
        self.level = 1
        self.exp = 0
        self.point = 0
    @filter.command("创建角色")    
    async def creat(self,event: AstrMessageEvent):
        user_name = event.get_sender_name()
        if user_name not in list:
            user_name = player()
            list.append(user_name)
            yield event.plain_result(f"@{user_name},角色创建成功啦")
            yield list
            
        else:
            yield event.plain_result(f"@{user_name},您已创建过角色哦")
    async def levelup(self):
        self.level = self.level + 1
        self.hp = self.hp + 10
        self.point = self.point + 1
        self.point = 0
        return 
    @filter.command("修炼")            
    async def exercise(self,event: AstrMessageEvent):
        user_name = event.get_sender_name()
        self.exp = self.exp + 10
        if self.exp >=100:
            self.levelup()
    @filter.command("属性")
    async def askexp(self, event: AstrMessageEvent):
        user_name = event.get_sender_name()
        if user_name in list:
            yield event.plain_result(f"'{user_name}'的信息如下\n生命{self.hp}\n攻击{self.atk}\n防御{self.dfc}\n经验值{self.exp},满100经验可使用'升级'升级哦")
        else :
            yield event.plain_result(f"@{user_name},您还未创建角色哦")
    @filter.command("升级")
    async def levelup(self,event: AstrMessageEvent):
        user_name = event.get_sender_name()
        if user_name in list:
            self.level = self.level + 1
            self.hp = self.hp + 10
            self.point = self.point + 1
            self.point = 0
        yield event.plain_result(f"@{user_name},升级成功！可输入'属性'指令查询属性")
    @filter.command("注册玩家")
    async def ask(self,event: AstrMessageEvent):
        yield event.plain_result(f"当前有{len(list)}名玩家注册\n{list}")
        
        
        
        
    

    


    