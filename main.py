import requests
from pathlib import Path


class Connection:
    def request(self, link):
        try:
            request = requests.get(link)
            match request.status_code:
                case 200:
                    print(f"You've connected to {link}")
                case 301:
                    print(
                        f"\n{link} error\n301 Moved Permanently: Indicates a permanent URL change\n "
                    )
                case 302:
                    print(
                        f"\n{link} error\n302 Found: Indicates a temporary URL change\n "
                    )
                case 302:
                    print(
                        f"\n{link} error\n303 See Other: Redirects to another resource\n "
                    )
                case 304:
                    print(
                        f"\n{link} error\n304 Not Modified: Content has not changed; use cached version\n "
                    )
                case 401:
                    print(
                        f"\n{link} error\n401 Unauthorized: Authentication is required\n "
                    )
                case 403:
                    print(
                        f"\n{link} error\n403 Forbidden: Access to the resource is denied\n "
                    )
                case 404:
                    print(
                        f"\n{link} error\n404 Not Found: The requested page was not found\n "
                    )
                case 408:
                    print(
                        f"\n{link} error\n408 Request Timeout: The request timed out\n "
                    )
                case 500:
                    print(
                        f"\n{link} error\n500 Internal Server Error: A generic server error occurred\n "
                    )
                case 502:
                    print(
                        f"\n{link} error\n502 Bad Gateway: Invalid response from another server\n "
                    )
                case 503:
                    print(
                        f"\n{link} error\n503 Service Unavailable: The server is currently unable to handle the request\n "
                    )
                case 504:
                    print(
                        f"\n{link} error\n504 Gateway Timeout: The server did not receive a timely response\n "
                    )
        except requests.exceptions.SSLError:
            print("{link} is blocked for you (try with vpn)")

    def internet_connection(self):
        try:
            requests.get("https://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            print("Your internet is not connected")
        except requests.Timeout:
            print("Your internet speed is slow")

    def all_link(self):
        file_path = Path(__file__).parent / "Include" / "links.txt"
        with open(file_path, "r") as file:
            links = file.read()
            links = links.replace(" ", "")
            links = links.splitlines()
            return links

    def run(self):
        if self.internet_connection():
            print("Your internet is connected")
            print(f'Your IP is {requests.get("https://api.ipify.org").text}')
            for i in self.all_link():
                self.request(i)


if __name__ == "__main__":
    obj = Connection()
    obj.run()
