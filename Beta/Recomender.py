from matplotlib.pyplot import *

def recommender(budget, expenses, costs):

    recommendation = []

    data = dict(zip(expenses, costs))
    total_spent = sum(costs)

    if total_spent > budget:
        recommendation.append("Budget is Low")

    elif total_spent > 0.8 * budget:
        highest_spend = max(costs)

        for expense, cost in data.items():
            if cost == highest_spend:
                percent_less = adjustCost(budget, cost, 45)
                recommendation.append(f"Spend {percent_less}% Less On {expense}")

    else:
        for expense, cost in data.items():
            if cost > 0.7 * budget:
                percent_less = adjustCost(budget, cost, 60)
                recommendation.append(f"Spend {percent_less}% Less On {expense}")

        if not recommendation:
            recommendation.append("All Expenses Balanced")

    return recommendation

def adjustCost(budget, cost, percentToCut):

    target = percentToCut / 100 * budget
    if cost <= target:
        return 0.0  # Already at or below 60%
    decrease_needed = cost - target
    percent_decrease = (decrease_needed / cost) * 100
    return round(percent_decrease, 2)

def create_chart(title_for_chart, x, y):

    title(title_for_chart)
    plot(x, y, marker = "o", linestyle = "solid", linewidth = 0.8)
    show()

x = ["Light Bill", "Shopping", "traveling"]
y = [5000, 3000, 20000]

print("Recommendations: \n")

print("\n".join(recommender(33000, x, y)))

create_chart("Monthly Expensis", x, y)

savefig(r"E:\coding\python\Beta\chart.png", dpi=1200)