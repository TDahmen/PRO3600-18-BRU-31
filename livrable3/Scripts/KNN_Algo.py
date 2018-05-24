def KNN_Method(a,b):

    """
        /!\ The two databases "newGamesData.npy" and "newOneHotEncoded.npy" have to be located in the same directory as the Python script
        This learning algorithm KNN ("K Nearest Neighbors") uses a move's data base (newGamesData). A move is modelized by a change in the board's configuration
        A grade is given for each move, giving its power. The more powerful a move is, the more it gives advantage for the one who did it. Theses moves have grades
        from 1 to 6. However, they have been "one-hot encoded", this means that the grade is a list of size 8 full of 0 and with a 1 at the place of the grade.
        For example: if the move's grade is 6 then there will be 0 except at position 6 where there will be a 1. These grades are stored in the file newOneHotEncoded.py
        and correponds to newGamesData.
        This algorithm displays the evolution of the accuracy for each K between a and b+1.
        It also displays the most efficient K in the interval with the final precision of the prediction.
        This returns the evaluation matrix of the board

        :param a: minimal value of the interval
        :param b: maximal value of the interval
        :type a: int
        :type b: int
        :return: return evaluation matrix of the board
        :rtype: tuple array

    """

    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report

    data = np.load("newGamesData.npy")[0:10000]  # Loading the 2 data bases
    labels = np.load("newOneHotEncoded.npy")[0:10000]

    y = np.argmax(labels, axis=1) # Declaration of the labels
    X = data # declaration of data

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, stratify=y) # Creation of train databases and the test databases
    bestScore=0 # variable that will store the most efficient K

    abscissa = [] # Creation of the x-axis array
    ordinate = [] # Creation of the array which will store the values of the precision for each K


    for i in range(a,b):
        abscissa.append(i)
        knn = KNeighborsClassifier(n_neighbors=i) # Creation of a KNeighboorsClassifeier's class, the parameter is the value of K
        knn.fit(X_train, y_train) # Normalization
        ordinate.append(knn.score(X_test, y_test))

        if(knn.score(X_test, y_test)>bestScore): # Comparison with previous accuracy
            bestScore=knn.score(X_test, y_test) # Storage of the accuracy's value
            best=i # we keep optimal K

            y_pred = knn.predict(X_test) # Prediction
            best_pred = y_pred # Storage of the best prediction
            bestReport=classification_report(y_test, y_pred) # Storage of the final report comparing the prediction with the test base

    print("Evolution of accuracy by K:")
    print()
    plt.plot(abscissa,ordinate) # Layout of the precision for each K
    plt.ylabel("precision")
    plt.xlabel("K")
    plt.show()
    plt.close()
    print()
    print("The optimal 'K' is:")
    print()
    print(best) # Display of the most efficient K
    print()
    print("The accuracy is:")
    print()
    print(bestReport) # Display of the final report

    return best_pred # Return the prediction matrix
