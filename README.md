# Interactive-Foreground-Segmentation
CS-867 Computer Vision Assignment 2 Spring 2021

Image segmentation is the classification of an image into different groups. Many kinds of research have been done in the area of image segmentation using clustering.Foreground detection is one of the major tasks in the field of computer vision and image processing whose aim is to detect changes in image sequences. Background subtraction is any technique which allows an image's foreground to be extracted for further processing (object recognition etc.)

![image](https://user-images.githubusercontent.com/79583184/198886604-7d5d6bab-21e8-4560-bcc6-76cc9f1a090b.png)
Pic Credit: datastuff.tech

Image segmentation is an important step in image processing, and it seems everywhere if we want to analyze what’s inside the image. For example, if we seek to find if there is a chair or person inside an indoor image, we may need image segmentation to separate objects and analyze each object individually to check what it is. Image segmentation usually serves as the pre-processing before pattern recognition, feature extraction, and compression of the image.

Image segmentation is the classification of an image into different groups. Many kinds of research have been done in the area of image segmentation using clustering. There are different methods and one of the most popular methods is K-Means clustering algorithm.

So here in this article, we will explore a method to read an image and cluster different regions of the image. But before doing lets first talk about:

1.Image Segmentation
2.How Image segmentation works
3.K-Means clustering ML Algorithm
4.Merge K-Means clustering Algorithm with Image Segmentation.
5.Canny Edge detection

K Means Clustering Algorithm:
K Means is a clustering algorithm. Clustering algorithms are unsupervised algorithms which means that there is no labelled data available. It is used to identify different classes or clusters in the given data based on how similar the data is. Data points in the same group are more similar to other data points in that same group than those in other groups. 

K-means clustering is one of the most commonly used clustering algorithms. Here, k represents the number of clusters.

Let’s see how does K-means clustering work –

1.Choose the number of clusters you want to find which is k.
2.Randomly assign the data points to any of the k clusters.
3.Then calculate the center of the clusters.
4.Calculate the distance of the data points from the centers of each of the clusters.
5.Depending on the distance of each data point from the cluster, reassign the data points to the nearest clusters.
6.Again calculate the new cluster center.
7.Repeat steps 4,5 and 6 till data points don’t change the clusters, or till we reach the assigned number of iterations.
