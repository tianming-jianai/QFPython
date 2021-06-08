import fitz
import os

file = r'example.pdf'
pdf = fitz.open(file)


def method_01():
    """保存单页为图片文件"""
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(5, 5).preRotate(0)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.writePNG('page' + str(pg) + '.png')


# method_01()

'''
交易对方: 95.38368000000003 99.11711999999996
卢保会 62.89368000000002 57.980959999999996
交易对方: 95.50367999999997 99.11711999999996
卢保会 62.74368000000004 57.980959999999996
交易对方: 95.53368000000003 99.11711999999996
卢保会 62.86368 57.980959999999996
'''

def method_02():
    pdf_file = r'example.pdf'
    pdfDoc = fitz.open(pdf_file)
    page = pdfDoc[0]
    # 设置缩放和旋转系数
    w = page.mediabox.width
    h = page.mediabox.height

    length = w if w>=h else h
    zoom = 1600/length # 将长边缩放到600像素

    trans = fitz.Matrix(zoom,zoom).preRotate(0)

    # 剪切百分比
    clip_rate = (0.2,0.1,0.9,1)
    clip = (w*clip_rate[0],h*clip_rate[1],w*clip_rate[2],h*clip_rate[3])

    pm = page.get_pixmap(matrix=trans,alpha=False,clip=clip)
    img_path = os.path.join(os.path.splitext(pdf_file)[0]+'.png')

    pm.writePNG(img_path)

method_02()


