import aiogram 
from aiogram import Bot , Dispatcher , F 
from aiogram.filters import Command
from aiogram.types import Message 
from aiogram import types
import fastapi
import asyncio
import os 
from fastapi import FastAPI , Request
app=FastAPI()
webhook_path="/webhook"
webhook_url="https://botforadil.onrender.com"
TOKEN=os.getenv("TOKEN")
bot=Bot(token=TOKEN)
dp=Dispatcher()
@app.on_event("startup")
async def create():
    await bot.set_webhook(webhook_url)
@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()
@app.post(webhook_path)
async def telegram_webhook(request: Request):
    update = types.Update.model_validate(await request.json())
    await dp.feed_update(bot, update)
    return {"ok": True}
    
@app.api_route("/",methods=["GET","HEAD"])
async def ping():
    return {"status":"alive"}
@dp.message(Command("start"))
async def start(message:Message):
    await message.answer("Привет")
