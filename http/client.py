import requests

# r = requests.get("https://localhost:5000", verify=False)

r = requests.get("https://localhost:5000", verify="./public.pem")

print(r.status_code)

print(r.content)
print(r.text)
