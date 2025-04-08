import os
import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta
import re

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

scheduler = AsyncIOScheduler()


@bot.event
async def on_ready():
    print(f"✅ ログイン完了: {bot.user}")
    scheduler.start()


@bot.command()
async def remind(ctx, time_str: str, *, message: str):
    try:
        # HH:MM形式のチェック
        if not re.match(r"^\d{1,2}:\d{2}$", time_str):
            await ctx.send("⏰ 時間は HH:MM 形式で指定してください。")
            return

        hour, minute = map(int, time_str.split(":"))
        now = datetime.now()
        target_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

        if target_time < now:
            target_time += timedelta(days=1)

        def reminder_job():
            return bot.loop.create_task(ctx.send(f"⏰ リマインド：{message}"))

        scheduler.add_job(reminder_job, trigger="date", run_date=target_time)

        await ctx.send(f"✅ {target_time.strftime('%Y-%m-%d %H:%M')} にリマインダーを設定しました：{message}")

    except Exception as e:
        print("エラー:", e)
        await ctx.send("⚠️ リマインダーの設定に失敗しました。")


# 環境変数からトークン取得（Railway用）
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
