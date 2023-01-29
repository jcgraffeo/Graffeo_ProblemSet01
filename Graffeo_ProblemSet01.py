import arcpy

def flooding():  # Flooding Analysis

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    floodzones = "floodzones"
    basin = "basin"

    # Process: Clip (Clip) (analysis)
    floodzones_Clip = "C:\\GIS 419\\Week 3\\ProblemSet#1_Data\\Study.gdb\\floodzones_Clip"
    arcpy.analysis.Clip(in_features=floodzones, clip_features=basin, out_feature_class=floodzones_Clip, cluster_tolerance="")

    # Process: Select (Select) (analysis)
    flooding = "C:\\GIS 419\\Week 3\\ProblemSet#1_Data\\Study.gdb\\flooding"
    arcpy.analysis.Select(in_features=floodzones_Clip, out_feature_class=flooding, where_clause="SFHA = 'IN'")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\GIS 419\Week 3\ProblemSet#1_Data\Study.gdb", workspace=r"C:\GIS 419\Week 3\ProblemSet#1_Data\Study.gdb"):
        flooding()
