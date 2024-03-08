# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 22:18:04 2024

@author: Boom
"""

import os
import pandas as pd

# 定义原始文件夹和目标文件夹的路径
input_folder = 'E:\青岛项目\聚类分析\青岛聚类分析\聚类结果'
output_folder = 'E:\青岛项目\聚类分析\青岛聚类分析\聚类pattern结果'

# 遍历原始文件夹中的所有文件
for file in os.listdir(input_folder):
    if file.endswith(".xlsx"):
        # 构建原始文件和目标文件的完整路径
        input_file = os.path.join(input_folder, file)
        output_file = os.path.join(output_folder, file)
        
        # 读取Excel文件
        df = pd.read_excel(input_file)
        
        # 按照"Cluster"列的值进行分类
        grouped = df.groupby('Cluster')
        
        # 创建一个Excel写入对象
        writer = pd.ExcelWriter(output_file)
        
        # 遍历每个分类
        for name, group in grouped:
            # 将每个分类保存到新工作表
            group.to_excel(writer, sheet_name=str(name), index=False)
        
        # 保存新的Excel文件
        writer.save()
        
        # 读取结果文件
        result_df = pd.read_excel(output_file, sheet_name=None)
        
        for sheet_name, sheet_df in result_df.items():
        # 计算第2到25列的平均值
            avg_values = sheet_df.iloc[:, 1:25].mean(axis=0)
    
    # 将平均值写入每个工作表的下一行
            sheet_df.loc['均值'] = avg_values
    
    # 计算最后一行的24个数除以它们的和，并赋予行标题为"pattern"
            sum_values = sheet_df.iloc[-1, 1:25].sum()
            if sum_values != 0:
               sheet_df.loc['pattern'] = sheet_df.iloc[-1, 1:25] / sum_values * 24
  
            
            # 将倒数第二行的第一列输入"均值"
            sheet_df.iloc[-2, 0] = "均值"
            
            # 将倒数第一行的第一列输入"pattern"
            sheet_df.iloc[-1, 0] = "pattern"
 
        # 保存修改后的Excel文件
        with pd.ExcelWriter(output_file) as writer:
            for sheet_name, sheet_df in result_df.items():
                sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)
