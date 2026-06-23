import pandas as pd
import matplotlib.pyplot as plt
import os

print("=" * 50)
print("      DATA VISUALIZATION PROJECT")
print("=" * 50)

# Load Dataset
data = pd.read_csv("sales_data.csv")

print("\nDATASET:")
print(data)

# Create charts folder
if not os.path.exists("charts"):
    os.makedirs("charts")

# -----------------------------
# BAR CHART
# -----------------------------
plt.figure(figsize=(8, 5))
plt.bar(data["Month"], data["Sales"])
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("charts/bar_chart.png")
plt.show()

# -----------------------------
# LINE CHART
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(data["Month"], data["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/line_chart.png")
plt.show()

# -----------------------------
# PIE CHART
# -----------------------------
plt.figure(figsize=(8, 8))
plt.pie(
    data["Sales"],
    labels=data["Month"],
    autopct="%1.1f%%"
)
plt.title("Sales Contribution by Month")
plt.tight_layout()
plt.savefig("charts/pie_chart.png")
plt.show()

# -----------------------------
# ANALYSIS
# -----------------------------
highest_sales = data["Sales"].max()
lowest_sales = data["Sales"].min()

highest_month = data.loc[data["Sales"].idxmax(), "Month"]
lowest_month = data.loc[data["Sales"].idxmin(), "Month"]

average_sales = data["Sales"].mean()

print("\n" + "=" * 50)
print("KEY INSIGHTS")
print("=" * 50)

print(f"Highest Sales Month : {highest_month}")
print(f"Highest Sales Value : {highest_sales}")

print(f"\nLowest Sales Month  : {lowest_month}")
print(f"Lowest Sales Value  : {lowest_sales}")

print(f"\nAverage Sales       : {average_sales:.2f}")

print("\nACTION TITLE:")
print(f"Sales increased steadily and reached a peak of {highest_sales} in {highest_month}.")

print("\nProject Completed Successfully!")