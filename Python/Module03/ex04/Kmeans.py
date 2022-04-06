from math import sqrt
from random import randint
import numpy as np
import pandas as pd


class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids : list = [] # values of the centroids
        self.cluster : list = [] # All cluster representation

    def fit(self, X : np) -> None:
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        None.
        Raises:
        This function should not raise any Exception.
        """
        new_centroids : list = []
        for i in range(0,self.ncentroid):
            self.centroids.append([])
            new_centroids.append([])
            for j in range(0,X.shape[1]):
                self.centroids[i].append(
                    randint(int(X.min()),int(X.max()))
                )

        print(self.centroids)
        dis_clu : list = []

        for iter in range(0,self.max_iter):
            self.cluster.clear()
            for c in range(0,self.ncentroid):
                self.cluster.append([])
            for m in range(0,X.shape[0]):
                for num_centr in range(0,self.ncentroid):
                    dis_clu.append(round(
                        np.linalg.norm(
                            np.array(self.centroids[num_centr]) - X[m]
                        ), 2)
                    )
                min_index = np.argmin(np.array(dis_clu))
                self.cluster[min_index].append(X[m])
                dis_clu = []
                new_centroids = []
            for ctr in range(0,self.ncentroid):
                if self.cluster[ctr] == []:
                    new_centroids.append([])
                    for j in range(0,X.shape[1]):
                        new_centroids[ctr].append(
                            randint(int(X.min()),int(X.max()))
                        )
                else:
                    new_centroids.append(np.mean(np.array(self.cluster[ctr]), axis=0))

            #if (np.array(new_centroids) == np.array(self.centroids)).all():
            #    print(new_centroids)
            #    break
            #else:
            self.centroids = new_centroids
            print(self.centroids)
            print(self.cluster)
            print("_____________________________")
        #print(self.centroids)
        #print(self.cluster)

                

    def predict(self, X : np):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        This function should not raise any Exception.
        """
        self.cluster.clear()
        dis_clu : list = []
        for m in range(0,X.shape[0]):
            for num_centr in range(0,self.ncentroid):
                dis_clu.append(round(
                    np.linalg.norm(
                        np.array(self.centroids[num_centr]) - X[m]
                    ), 2)
                )
            min_index = np.argmin(np.array(dis_clu))
            self.cluster.append(min_index)
            dis_clu = []
        print(self.cluster)

X = np.array([[0,1,2],[2,3,7],[0.5,3,5],[3,7,1],[8,2,2]])
SSC = pd.read_csv('solarsystemcensus.csv')
SSC = np.array(SSC)
SSC = np.delete(SSC, 0, axis=1)

test = KmeansClustering(ncentroid=4)
test.fit(SSC)
#test.predict(np.array([[0,1,2]]))
#Problème avec mes centroid