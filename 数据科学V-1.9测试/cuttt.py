# encoding=utf-8
from __future__ import unicode_literals
import sys
sys.path.append("../")

import jieba
import jieba.analyse
import jieba.posseg


def cut_words(word):
    seg_list = jieba.cut(word,cut_all=False)
    return seg_list
