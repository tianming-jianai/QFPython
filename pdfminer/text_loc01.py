# encoding : udf-8

"""
解析pdf文本保存到txt文件中
"""
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBoxHorizontal
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed, PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfparser import PDFDocument, PDFParser

path = 'example.pdf'


def parse():
    fp = open(path, 'rb')  # 以二进制读模式打开
    praser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器 与文档对象
    praser.set_document(doc)
    doc.set_parser(praser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDf 资源管理器 来管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page的内容
        for page in doc.get_pages():  # doc.get_pages() 获取page列表
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            print('------------------')
            print('页码：',page.pageid)
            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    with open(r'res.txt', 'w',encoding='utf-8') as f:
                        results = x.get_text()
                        if '交易对方' in results:
                            print('交易对方:',x.height,x.width)
                        if '卢保会' in results:
                            print('卢保会',x.height,x.width)
                        # print(results)
                        f.write(results + '\n')


if __name__ == '__main__':
    parse()
