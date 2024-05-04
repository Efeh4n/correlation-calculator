#                   correlation calculator 
data_x = []
data_y = []
mean_x = (sum(data_x)/len(data_x))
mean_y = (sum(data_y)/len(data_y))

def correlation_calculator(data_x, data_y):
        x_list = [] # x - mean of data_X
        y_list = [] # y - mean of data_Y
        z_list = [] # 
        sqr_list_x = []
        sqr_list_y = []      
        for i in data_x:
            x_list.append(i-mean_x)
        for j in data_y:
            y_list.append(j-mean_y)
        for i in range(len(data_x)):
            z_list.append(x_list[i]*y_list[i]) 
        for n in x_list:
            sqr_list_x.append(n ** 2)
        for m in y_list:
            sqr_list_y.append(m ** 2)
        sum_sqr_list_x = sum(sqr_list_x)
        sum_sqr_list_y = sum(sqr_list_y)
        numerator = sum(z_list)     
        denominator = (sum_sqr_list_x * sum_sqr_list_y)**0.5

        return  numerator/denominator
print("correlation :", correlation_calculator(data_x, data_y))













        
