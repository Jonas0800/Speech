import opensmile
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.LowLevelDescriptors,
)
df_lld = smile.process_file(r"######################")  
df_lld.to_csv("features_lld.csv")
