# -*-coding:utf-8-*-
import json
import downloader
import xlrd
import parser


class SpiderMain(object):

    def __init__(self):
        self.downloader = downloader.Downloader()
        self.parser  = parser.Parser()

    def craw(self, root_url):
        cont = self.downloader.download(root_url)
        return cont


    def parser360Comments(self,cont):
        s = json.loads(cont)
        self.parser.parser360Comments(s)


    def get360CommentsCount(selft,count_url):
        cont = selft.downloader.download(count_url)
        s = json.loads(cont)
        str = s['bad']
        strr = int(str)
        return strr

    def getwandoujiaComments(self):
        for i in range(1,11):
            root_url = "http://www.wandoujia.com/apps/com.pingan.paces.ccms/comment"
            root_url = root_url + str(i)
            cont = obj_spider.craw(root_url)
            self.parser.parsehtml(root_url,cont)


    def get360Comments(self):
        # 获取评论总数量num
        count_url = "http://comment.mobilem.360.cn//comment/getLevelCount?baike=%E5%B9%B3%E5%AE%89%E4%BF%A1%E7%94%A8%E5%8D%A1+Android_com.pingan.paces.ccms&c=message&a=getmessagenum&_=1506669567552"
        num = obj_spider.get360CommentsCount(count_url)
        print 'num:', num
        start = 0
        count = 40

        while True:
            # 循环发送请求，每次请求获取40条评论，直到所有评论数获取完为止
            print 'start', start

            root_url = "http://comment.mobilem.360.cn/comment/getComments?baike=%E5%B9%B3%E5%AE%89%E4%BF%A1%E7%94%A8%E5%8D%A1+Android_com.pingan.paces.ccms&c=message&a=getmessage&start=" + str(
                start) + "&count=" + str(count) + "&type=bad&level=3&_=1506671415463";

            cont = obj_spider.craw(root_url)

            # 360应用市场口袋银行app的评论解析输出到Excel文档
            obj_spider.parser360Comments(cont)


            start = start + count

            # 应用分两种情况，num能否整除count
            if num % count == 0:
                # 要对新的start进行校验
                if start == num:
                    break
            else:
                # 如果总评论数不能被40整除，则最后一次获取的评论数小于40条
                if start == num / count * count:
                    count = num % count

                if start == num:
                    break



if __name__=="__main__":

    obj_spider = SpiderMain()
    #360应用市场口袋银行app的评论获取
    # obj_spider.get360Comments()
    # 豌豆荚应用市场口袋银行app的评论获取
    obj_spider.getwandoujiaComments()




