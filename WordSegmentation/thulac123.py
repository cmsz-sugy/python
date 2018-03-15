#coding:utf-8
import thulac

thu1 = thulac.thulac(seg_only=True)  #只进行分词，不进行词性标注
text = thu1.cut('在北京大学生活区喝进口红酒.......', text=True)
print text

# thu1.cut_f("123.txt", "output.txt")  #对input.txt文件内容进行分词，输出到output.txt