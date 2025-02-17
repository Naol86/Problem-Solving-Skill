import speedtest
import time

def run_speed_test():
    st = speedtest.Speedtest()
    print("Finding best server...")
    st.get_best_server()
    
    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping

    print(f"Download speed: {download_speed:.2f} Mbps")
    print(f"Upload speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")
    print("-" * 40)

try:
    while True:
        run_speed_test()
        print("Waiting for 1 minute...")
        time.sleep(60)  # Wait for 1 minute
except KeyboardInterrupt:
    print("Speed test stopped.")

