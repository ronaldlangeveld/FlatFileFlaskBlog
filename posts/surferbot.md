<!-- VARS
##title: I made a Telegram bot that tells me local surf conditions. ./title
##author: Ronald ./author
##date: 2018/01/10 ./date
##slug: i-made-a-telegram-bot-that-tells-me-local-surf-conditions ./slug
./VARS -->

After I made Downtime bot, I decided to go a bit further and make it related to something I’m truly passionate about. Surfing.

It started off with mapping out my local knowledge about surfing here.

 - Wind Direction
 - Swell Direction
 - Swell Size

I also had to write a bit of code to convert the wind speeds to KMH from MPH. Feet is fine. Wave size should always be measured in feet.

Once I got that figured out I had to convert it into code, which I made available for you all on Github.

The friendly guys at Magicseaweed also hooked me up with an API so I can use it in bot.
And now I can let me tell me the report for today and tomorrow on demand in human language.

Although its cool reading charts… this saves a lot of time - and I get to tweak it all the time (in code) based on my knowledge.

<div class="container">
	<div class="row">
		<div class="col-6">
			
	<img style="width: 100%" src="https://i.imgur.com/9CmDKEM.png">

		</div>

<div class="col-6">

	<img style="width: 100%" src="https://i.imgur.com/lWcd2vU.png">
	
</div>

</div>
</div>

Over time I will advance it a bit and try to work out a ratings formula like 10/10 means the waves will be firing (ie, conditions is on par with ideal conditions) or 1/10 will be utter shit… also, I need it to automatically send me a message every night with the next morning’s conditions. 

If you wanna make your own bot just replace the variables with its own desirable conditions as every surf spot is different.

Also, the API is from MSW.  You can use my key to check it out, but I really recommend getting your own one from them.. Just email them and they will gladly send you an api key. 
Read their docs to make sure you don't get the report for the wrong location. It might confuse you.

And one more important thing: Be discrete with your location and it's conditions - you don't want to anger your friends and local surfers when a bunch of non-locals discover your bot and crowds your home break.

[Access the project on Github and feel free to fork it or contribute](https://github.com/burgundy93/localsurferbot)

Cheers!