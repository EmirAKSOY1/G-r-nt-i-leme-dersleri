import cv2 as cv

resim = cv.imread("resim/resim1.jpg")#verilen dizindeki resmi okur

# print(resim)
print(resim.shape)#Resmin boyutları y/x şeklinde veriyor
#print(resim.ndim)#resmin Kaç boyutlu olduğu
#print(resim.size)#toplam piksel sayısı