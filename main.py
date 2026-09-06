import webbrowser
import time

print("⚡ Launching ThunderX Workflow Optimizer... ⚡")
time.sleep(1)

# List the websites you use every single day (you can change these!)
websites = [
    "https://github.com",
    "https://google.com"
]

for site in websites:
    print(f"Opening: {site}")
    webbrowser.open(site)

print("✅ Workflow successfully optimized!")
