import xadmin
from .models import *


class ArticleAdmin:
    # 模型想要使用ueditor样式，必须重新注册模型管理类
    style_fields = {"body": "ueditor"}

xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Tag)
xadmin.site.register(Category)
xadmin.site.register(Ads)