import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import os

# Simulated scan results (replace with actual tool outputs if needed)
scan_summary = {
    "Checkov": {"Critical": 3, "High": 4, "Medium": 3, "Low": 2},
    "Trivy": {"Critical": 5, "High": 10, "Medium": 7, "Low": 4},
    "Gitleaks": {"Critical": 1, "High": 1, "Medium": 1, "Low": 0},
    "AI Best Practices": {"Critical": 2, "High": 1, "Medium": 1, "Low": 1}
}

recommendations = {
    "Checkov": "Review Terraform configurations. Use strict IAM policies. Implement resource tagging and security groups.",
    "Trivy": "Update base images. Apply patches to vulnerable libraries. Use minimal OS layers.",
    "Gitleaks": "Remove secrets from code. Rotate compromised credentials. Use secret managers like AWS Secrets Manager.",
    "AI Best Practices": "Enable CI/CD policies. Train developers. Use automation to enforce secure coding standards."
}

# Step 1: Generate Markdown Report
today = datetime.now().strftime("%Y-%m-%d")
with open("ai-security-analysis.md", "w") as f:
    f.write(f"# AI-Powered DevSecOps Summary Report\n\n")
    f.write(f"**Scan Date:** {today}  \n**Pipeline Trigger:** GitHub Actions  \n**Environment:** Multi-Cloud Infrastructure\n\n")
    f.write("## Findings Summary\n\n")
    f.write("| Tool | Total | Critical | High | Medium | Low |\n")
    f.write("|------|-------|----------|------|--------|-----|\n")
    for tool, levels in scan_summary.items():
        total = sum(levels.values())
        f.write(f"| {tool} | {total} | {levels['Critical']} | {levels['High']} | {levels['Medium']} | {levels['Low']} |\n")
    f.write("\n## AI Recommendations\n")
    for tool, rec in recommendations.items():
        f.write(f"\n**{tool}:** {rec}")

# Step 2: Generate CSV with Recommendations
rows = []
for tool, levels in scan_summary.items():
    for severity, count in levels.items():
        if count > 0:
            rows.append({
                "Tool": tool,
                "Severity": severity,
                "Count": count,
                "Recommendation": recommendations[tool]
            })
df = pd.DataFrame(rows)
df.to_csv("devsecops_recommendations.csv", index=False)

# Step 3: Generate Chart
categories = list(scan_summary.keys())
critical = [scan_summary[tool]["Critical"] for tool in categories]
high = [scan_summary[tool]["High"] for tool in categories]
medium = [scan_summary[tool]["Medium"] for tool in categories]
low = [scan_summary[tool]["Low"] for tool in categories]

bar_width = 0.2
x = range(len(categories))

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar([i - 1.5 * bar_width for i in x], critical, width=bar_width, label='Critical')
ax.bar([i - 0.5 * bar_width for i in x], high, width=bar_width, label='High')
ax.bar([i + 0.5 * bar_width for i in x], medium, width=bar_width, label='Medium')
ax.bar([i + 1.5 * bar_width for i in x], low, width=bar_width, label='Low')

ax.set_xticks(list(x))
ax.set_xticklabels(categories)
ax.set_ylabel("Issue Count")
ax.set_title("Security Scan Summary")
ax.legend()

plt.tight_layout()
plt.savefig("devsecops_scan_results.png")
print(" Markdown, CSV, and Chart generated successfully.")
