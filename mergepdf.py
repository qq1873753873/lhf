import os
def merge_pdf(pre,paths):
    from PyPDF2 import PdfReader,PdfWriter
    write = PdfWriter()
    for path in paths:
        tmp_pdf=PdfReader(open(path,'rb'))
        for page in tmp_pdf.pages:
            write.add_page(page)
    with open(pre+'\\合并.pdf','wb') as out:
        write.write(out)
def generate_paths(path):
    pdf_list=[]
    for file in os.listdir(path):
        if ".pdf" in file:
            pdf_list.append(path+'\\'+file)
    pdf_list.sort()
    return pdf_list
    

if __name__=='__main__':
    print("******************这是一个用来合并多个pdf为一的程序******************")
    print("*******************************************************************")
    print("*******************************使用方法：***************************")
    print("请将需要合并的pdf存于同一文件夹下,再输入文件夹所在的绝对路径即可自动合并")
    print("**********************排序方式为python自带的sort排序*****************")
    path=input("请输入pdf存在的路径：\n")
    paths=generate_paths(path)
    merge_pdf(path,paths)