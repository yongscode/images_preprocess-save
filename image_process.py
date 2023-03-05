import cv2
import numpy as np
import time
import os
from glob import glob








def save_process(fire):
	cnt=0
	while True:
	
		if cnt<196 : #range = Number of your photos for preprocess. Its okay have more range over picture, Range over error occurs, but picture is preprocessed and saved.
		
			img=fire[cnt]
			save_image=cv2.imread(img) 
			save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV) 
			save_image =cv2.GaussianBlur(save_image ,(3,3),0)
			
			picture_name=str(cnt)
			
			extension =".jpg"
			
			save_path="/home/yongs/custum_yolo_test/img2/"
			
			output=save_path+picture_name+extension 
			cv2.imwrite(output,save_image)
		
			cnt=cnt+1
			print(cnt)
			
		else:
			break
def main():
	fire=[]
	fire=glob("/home/yongs/custum_yolo_test/img/*.jpeg")
	save_process(fire)
	
	
if __name__ == '__main__':
	main()		
	
	


				
				
										
				
