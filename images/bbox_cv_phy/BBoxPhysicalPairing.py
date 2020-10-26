import numpy as np

# create array data

predict = np.array([[1,2,2,1],
                   [4.5,2.5,10,0.5],
                   [6,6,8,4], 
                   [6.26,6.26,8.26,4.26]],np.double)

truth = np.array([[1,4,3,3],
                 [1.2,2.2,2.2,1.2],
                [5,2,8,1],
                [6.1,6.1,8.1,4.1],
                [8.1,8.1,11.1,9.1]], np.double)
# get useful variables
nums_pred = len(predict)
nums_gt = len(truth)

iou_matrix = np.zeros((nums_pred,nums_gt))


# boxA 存储的是边界框的左上顶点坐标和右下顶点坐标
# boxA=[x1,y1,x2,y2]
def iou(boxA, boxB):
    # 计算重合部分的上下左右4个边的值，注意最大最小函数的使用
    left_max = max(boxA[0],boxB[0])
    top_max = max(boxA[1],boxB[1])
    right_min =  min(boxA[2], boxB[2])
    bottom_min = min(boxA[3], boxB[3])

    # 计算重合部分的面积
    inter = max(0,(right_min-left_max)) * max(0, (bottom_min-top_max)) # 宽*高
    Sa = (boxA[2]-boxA[0])*(boxA[3]-boxA[1])
    Sb = (boxB[2]-boxB[0])*(boxB[3]-boxB[1])

    # 计算所有区域的面积并计算 iou
    union = Sa+Sb-inter
    iou = inter/union
    return iou

def transformBBox(boxA):
	# 将 BBox 从左下 + 右上 表示转换为 左上 + 右下
	return [boxA[0], boxA[3], boxA[2], boxA[1]]
# get iou matrix

for i in range(nums_pred):
	for j in range(nums_gt):
		#print(truth[j])
		iou_matrix[i][j] = iou(transformBBox(predict[i]), transformBBox(truth[j]))

print(iou_matrix)

res  = []
IOU_theta = 0.4

while np.any(iou_matrix > IOU_theta):
	ind = np.argmax(iou_matrix)
	ind_col = ind % nums_gt
	ind_row = (ind - ind_col) // nums_gt
	print("row = %d, col = %d"%(ind_row, ind_col))
	# store results for more analysis
	res.append([predict[ind_row], truth[ind_col]])
	# set the correspoding row and col to zero
	# exclude those already paired from future comparsion
	iou_matrix[ind_row][:] = 0
	# set col to 0
	for ii in range(nums_pred):
		iou_matrix[ii][ind_col] = 0
	print(iou_matrix)
print(res)