import pandas as pd
import matplotlib.pyplot as plt

# load dtaset
data = pd.read_csv("attendance.csv")

# filter low attendance students (<75%)
low_attendance = data[data['Attendance'] < 75]
print("Student with low attendance (<75%) :")
print(low_attendance)

# pie chart 
plt.figure(figsize=(6,6))
plt.pie(
    [len(low_attendance), len(data) - len(low_attendance)],
    labels=['Low Attendance', 'Good Attendance'],
    autopct='%1.1f%%',
    colors=['pink', 'green']
)
plt.title("Attendance Distribution")
plt.show()