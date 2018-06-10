from sklearn import tree;
# 0 smooth , 1 bumpy
features = [[140,0],[130,0],[170,1],[180,1]]; 

# 0 apple, 1 orange
labels = ['apple','apple','orange','orange'];

clf = tree.DecisionTreeClassifier();
clf = clf.fit(features,labels);

print ( clf.predict([ [160,1] ]) );
