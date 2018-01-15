
<!-- VARS
##title: Getting Downtime Bot featured on Product Hunt ./title
##author: Ronald ./author
##date: 2018/01/04 ./date
##slug: getting-downtime-bot-featured-on-product-hunt ./slug
./VARS -->

Launching products is what I love doing..... well, creating products and seeing it come to life and then sharing it with the world.. It think it's the coding part that's addictive. Writing code and then to see my computer finally doing what I asked it to do is what makes my dopamine levels rocket. It's satisfying.

I went to a small surfing town called Jeffreys Bay over the Christmas holidays. It was great! I got to surf some epic waves, saw family and even went sandboarding. It's an epic change of scene and routine from what I have going here. Good little breakaway. 

<div>

	<img style="width: 100%" src="https://i.imgur.com/nIdgSMu.jpg">
	
</div>

Of course, it still didn't stop me from coding as much as possible and working on multiple projects while I was there. 

<div>

	<img style="width: 100%" src="https://i.imgur.com/wB3ntyn.jpg">
	
</div>


One afternoon when I got home, I tried accessing one of my sites.. but it was just down. Silly me, I realised that I forgot to `systemctl start nginx` after configuring a few settings on my server. It was like 10 hours since I did it, which means my site was off for 10 years without even realising it. How silly. I do have a service who emails me when my site goes offline... but still - I rarely check my email especially if I'm not expecting anything. 

Being kinda annoyed about it, I started thinking of ways that would make it easier for me to know when my site goes offline - without email & third party apps. The company I was with do actually provide SMS notifications, but they charge extra and per sms. Also, my phone is on flight mode (with wifi) most of the time so SMS's wouldn't come through.

I'm a member on this really awesome Telegram group called [Work in Progress](https://wip.chat/) (or WIP) where me and fellow developers (amongst others) would write To-Do's and just chat. The To-Do's are managed by bots and it's pretty cool. You can let it know when you've completed a task and so forth. [Pieter Levels wrote a detailed article about featuring WIP.](https://levels.io/100-days-of-shipping/) 

Because I got used to using Telegram's Bots and I generally have my phone with me, as opposed to email, I figured a Telegram Bot letting me know when my site isn't working is exactly what I need!

So I decided to learn how to code Bots. 

Actually, it was relatively simple. Bots can be scripted in just about any language. I chose Python3. You get a bot token from the Botfather (another bot on Telegram) and then you hook it up to your script by using Telegram's API. You have to hose the server script yourself though.
There's many open source projects on Github you can look at to get some examples. 

After a couple of hours of coding and messing around, I finally got my Bot to message me when I typed `sudo systemctl stop nginx` on my server. I was super stoked. Went around trying to show my whole family how its done, etc. 

I loaded it up onto my server and I finally had my own bot that would notify me should something go wrong server side.

After doing some research I transformed it into a little service.

[On launch day I received close to a thousand hits and got featured on Product Hunt making it into the Top 10 products of the day.](https://www.producthunt.com/posts/downtime-bot-for-telegram) 

So basically, if you want something that doesn't exist, build it yourself... chances are it can become a little side business. Or not. But keep building your own stuff. 