import requests

def check_vulnerabilities(url):

    paths = [
        "/admin", "/login", "/phpinfo.php", "/wp-login.php", "/cgi-bin/",
        "/.git/", "/.htaccess", "/robots.txt", "/test.php"
    ]
    
    for path in paths:
        full_url = url + path
        response = requests.get(full_url)
        
        if response.status_code == 200:
            print(f"Potential vulnerability found: {full_url}")
        else:
            print(f"Checked {full_url}: Not accessible")

url = input("Enter the target website URL (e.g., http://example.com): ")
check_vulnerabilities(url)
