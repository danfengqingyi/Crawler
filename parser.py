# -*-coding:utf-8-*-
from bs4 import BeautifulSoup

import outputer


class Parser(object):

    def __init__(self):
        self.outputer = outputer.Outputer()

    def parser360Comments(self, s):
        str = s['data']
        strr = str['messages']
        print "%d" % len(strr)
        #每次获取到的40条评论，要去遍历每条评论信息获取其中的关键信息字段
        for ss in strr:
            print "content:", ss["content"]
            print "version_name:", ss["version_name"]
            print "model:", ss["model"]
            var = [ss["content"],ss["version_name"],ss["model"]]
            self.outputer.outputerexcel(var)


    def parsehtml(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_data = self._get_new_data(page_url,soup)
        return new_data

    def _get_new_data(self, page_url, soup):
        res_data = {}
        print 'page_url:',page_url,"" \
                                   ""
        comment_nodes = soup.findAll('li',class_="normal-li")
        for comment_node in comment_nodes:
            title_nodes = comment_node.findAll('p', class_="cmt-content")
            for title_node in title_nodes:
                res_data['comment'] = title_node.get_text()
            first_node = comment_node.find('p', class_="first")
            summary_node = first_node.findAll("span")
            res_data['name'] = summary_node[0].get_text()
            res_data['time'] = summary_node[1].get_text()
            var = [res_data["comment"], res_data["name"], res_data["time"]]
            self.outputer.outputerexcel(var)
            print 'name,time,comment:', res_data['name'], res_data['time'], res_data['comment'], "" \
                                                                                                 ""

