import opensmile
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)
df = smile.process_file(r"#######################")
df.to_csv("features_func.csv")
print(df.shape, "Features")  
df.to_csv("features_func.csv", index=True)
print(df.columns[:10])   
print(df.iloc[0].describe())
