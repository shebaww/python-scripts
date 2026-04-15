import socks
import socket

socks.set_default_proxy(socks.SOCKS5, '127.0.0.1', 9050)

def check_site(website, ports=[80, 443, 8080, 8443, 666, 1337, 22, 21]):
    website = website.replace('http://', '').replace('https://', '').split('/')[0]
    
    for port in ports:
        try:
            sock = socks.socksocket()
            sock.settimeout(5)
            sock.connect((website, port))
            sock.close()
            print(f"✅ Online on port {port}")
            return True
        except Exception as e:
            print(f"❌ Port {port}: {str(e)[:50]}")
            continue
    
    print("❌ Site offline on all tested ports")
    return False

if __name__ == "__main__":
    website = input('Put in your website link: ')
    check_site(website)
