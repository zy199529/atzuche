import jieba
import jieba.analyse
import jieba.posseg
import pandas as pd


def dosegment_all(sentence):
    '''
    带词性标注，对句子进行分词，不排除停词等
    :param sentence:输入字符
    :return:
    '''
    sentence_seged = jieba.posseg.cut(sentence.strip())
    outstr = ''
    for x in sentence_seged:
        outstr += "{}/{},".format(x.word, x.flag)
    # 上面的for循环可以用python递推式构造生成器完成
    print(",".join([("%s/%s" % (x.word, x.flag)) for x in sentence_seged]))


if __name__ == "__main__":
    df = pd.read_csv("评论.csv", encoding='gb18030')
    content = list(df["renter_comment_content"])
    for i in range(len(content)):
        try:
            dosegment_all(content[i])
        except:
            pass
