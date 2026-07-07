import pandas as pd
df = pd.read_csv("data/student_results.csv")
print(df)
df["Total"] = df["MATH"] + df["SCIENCE"] +df["ENGLISH"]
print(df)
topper = df.loc[df["Total"].idxmax()]
print("topper")
print(topper)
df["Average"] = df["Total"] /3
print(df)
topper = df.loc[df["Total"].idxmax()]
print("Topper:")
print(topper)
lowest = df.loc[df["Total"].idxmin()]
print("Lowest Scorer:")
print(lowest)
df["Result"] = df["Average"].apply(lambda x: "Pass" if x>=35
else "Fail")
print(df)
import matplotlib.pyplot as plt
plt.bar(df["NAME"],df["Total"])
plt.title("Student Total Marks")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.show()
plt.figure()
plt.pie(df["Total"], labels=df["NAME"],autopct="%1.1f%%")
plt.title("Student Total Marks Distribution")
plt.show()
df.to_csv("data/final_student_results.csv",index=False)
print("file saved successfully!")
print("Analysis Completed Successfully!")