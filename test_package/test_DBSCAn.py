# -*- coding:utf-8 -*-  
'''
Created on 2018年3月7日

@author: Administrator
'''
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
x = read_data.x
x = StandardScaler().fit_transform(x)  #对数据进行归一化

navigation = DBSCAN(eps=0.1, min_samples=10000)
core_samples_mask = np.zeros_like(navigation.labels_, dtype=bool)
core_samples_mask[navigation.core_sample_indices_] = True
labels = navigation.labels_

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('number of clusters: %d' % n_clusters_)
#上面是进行密度聚类
#下面是将密度聚类结果上图
#两个任务之间一定要凑够三行
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        col = 'k'
    class_member_mask = (labels == k)
    xy = X[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=14)

    xy = X[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,markeredgecolor='k', markersize=3)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()