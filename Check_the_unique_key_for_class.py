import pandas as pd

anji=pd.read_csv("/content/TF-2.x-Object-Detection/images/train_labels.csv")

anji['class'].value_counts()
