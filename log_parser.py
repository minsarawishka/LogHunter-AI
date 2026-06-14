import re
import pandas as pd

def parse_log_file(file_path):
    log_data = []
    pattern = r'(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - IP: (?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - User: (?P<user>\w+) - Status: (?P<status>[\w\s]+)'
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    log_data.append(match.groupdict())
                    
        df = pd.DataFrame(log_data)
        return df
    except Exception as e:
        print(f"Error reading log file: {e}")
        return pd.DataFrame()

def detect_brute_force(df, threshold=3):
    if df.empty:
        return pd.DataFrame()
    
    failed_logins = df[df['status'].str.strip() == 'Failed Password']
    ip_counts = failed_logins['ip'].value_counts()
    suspicious_ips = ip_counts[ip_counts >= threshold].index
    brute_force_alerts = failed_logins[failed_logins['ip'].isin(suspicious_ips)]
    
    return brute_force_alerts

if __name__ == "__main__":
    test_file = "sample_logs/auth_vulnerable.log"
    print("--- Parsing Log File ---")
    parsed_df = parse_log_file(test_file)
    print(parsed_df)
    
    print("\n--- Detecting Brute Force (Threshold >= 3) ---")
    alerts = detect_brute_force(parsed_df)
    print(alerts)