#!/usr/bin/env python
# coding=utf-8
import os
import re

import pandas as pd

from pyltp import Segmentor, Postagger, Parser

A = []


class LtpLanguageAnalysis(object):
    def __init__(self, model_dir=r"F:\BaiduNetdiskDownload\3.4.0\ltp_data_v3.4.0"):
        self.segmentor = Segmentor()
        self.segmentor.load(os.path.join(model_dir, "cws.model"))
        self.postagger = Postagger()
        self.postagger.load(os.path.join(model_dir, "pos.model"))
        self.parser = Parser()
        self.parser.load(os.path.join(model_dir, "parser.model"))

    def analyze(self, text):
        # 分词
        words = self.segmentor.segment(text)
        content = '-'.join(words)
        content=content.split("-")

        # 词性标注
        postags = self.postagger.postag(words)
        pos = '-'.join(postags)
        pos = re.sub("nl", "!", pos)
        pos = re.sub("nd", "@", pos)
        pos = re.sub("nz", "#", pos)
        pos = re.sub("nh", "$", pos)
        pos = re.sub("nt", "%", pos)
        pos = re.sub("ns", "^", pos)
        pos = re.sub("ws", "&", pos)
        pos = re.sub("wp", "!", pos)
        str = "".join(pos.split("-"))
        print(str)
        word = "nda"
        a = [m.start() for m in re.finditer(word, str)]
        for j in a:
            A.append("".join(content[j:j + 3]))
        word = "na"
        a = [m.start() for m in re.finditer(word, str)]
        for j in a:
            A.append("".join(content[j:j + 2]))
        # for i in range(len(postags)):
        #     if len(postags[i]) > 1:
        #         if postags[i] not in A:
        #             A[postags[i]] = 1
        #         else:
        #             A[postags[i]] += 1
        # # 句法分析
        # arcs = self.parser.parse(words, postags)
        # print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))

    # def release_model(self):
    #     # 释放模型
    #     self.segmentor.release()
    #     self.postagger.release()
    #     self.parser.release()


if __name__ == '__main__':
    ltp = LtpLanguageAnalysis()
    # ltp.analyze("味道不错")
    # ltp.release_model()
    df = pd.read_csv("评论.csv", encoding='gb18030')
    content = list(df["renter_comment_content"])
    for i in range(len(content)):
        try:
            ltp.analyze(content[i])
        except:
            pass
    print(A)
