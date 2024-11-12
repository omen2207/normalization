import csv

def min_max_normalization(new_min, new_max, marks):
    min_val = min(marks)
    max_val = max(marks)
    return [(((mark - min_val) / (max_val - min_val)) * (new_max - new_min)) + new_min for mark in marks]

def z_score_normalization(marks):
    mean = sum(marks) / len(marks)
    variance = sum((mark - mean) ** 2 for mark in marks) / len(marks)
    std_dev = variance ** 0.5
    return [(mark - mean) / std_dev for mark in marks]
a = []
b = []
with open(r'C:\Users\bhilw\OneDrive\Documents\DM\iris.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  
    for row in reader:
        roll_no = int(row[0])
        mark = float(row[1])
        a.append(roll_no)
        b.append(mark)

new_min = int(input("Enter the min boundary for min-max: "))
new_max = int(input("Enter the max boundary for min-max: "))

min_max_marks = min_max_normalization(new_min, new_max, b)
z_score_marks = z_score_normalization(b)

print("Roll No\tOriginal Marks\tMin-Max Normalized\tZ-Score Normalized")
for i in range(len(a)):
    print(f"{a[i]}\t{b[i]:.2f}\t\t{min_max_marks[i]:.2f}\t\t\t{z_score_marks[i]:.2f}")

with open(r"C:\Users\bhilw\OneDrive\Documents\DM\2_normalization code\normalized.csv",'w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["roll_no","original-marks","min-max_marks","z-score"])
    for i in range(len(a)):
        writer.writerow([a[i],b[i],f"{min_max_marks[i]:.2f}",f"{z_score_marks[i]:.2f}"])
