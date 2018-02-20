<!-- VARS
##title: HOW FFFB STARTED ./title
##author: Ronald ./author
##date: 2018/02/20 ./date
##slug: building-open-source-flask-blog ./slug
##image: ffbcov.jpg ./image
./VARS -->



It's a Long post, so TLDR:
I didn't like existing CMS software, so I started my own project, got going myself, then I tweeted about it, a contributor came along and we got v1 production ready in 3 days without talking much. And it does exactly what I wanted it to do!

## Back story:

Over the past few months I've been playing around with probably 8 or 9 different CMS's (Content Management Systems). Basically web-software that organises your website for you - or more commonly used as blogging software. Even if you're just remotely into web development or blogging, then you've most probably heard of WordPress, Drupal or Ghost. 

Now I'm very much full of shit when it comes to using CMS software. As much as I like playing around with it, as soon as something doesn't quite do something the way I want it to, I pretty much dislike it immediately. From the many CMS software I experimented with, absolutely none of them did EXACTLY what I wanted it to do and the way I wanted to do it.

Let me explain.

## The Problem:

The top CMS's out there ([in terms of market share](https://websitesetup.org/popular-cms/)) is without a doubt WordPress. Personally, I used to love WordPress. It did much of what I wanted it to do, it was easy to use and I still recommend it to newbies, as its got like a gazillion themes to choose from and there's help online on just about everything you need to know. However, as a developer suffering from OCD when I have to deal with things I don't want, WordPress is too much, especially just for running a small little blog that you want easily customisable. There's some awesome WordPress blank themes to start your own theme like [Blankslate](https://wordpress.org/themes/blankslate/) and [Underscores](https://underscores.me/), but you still need to deal with a lot of PHP to get it to function properly.

I needed something more lightweight and easy to maintain. 

Soon after I came across [Pico](http://picocms.org/) and it did much of what I wanted it to do. It didn't have a database (I love this), no admin system and was fairly simple to customise. I could update my blog by pushing the updates to my Github account, pulling the updates on my server and boom, up to date. This means I will always have it backed up. However, it wasn't SEO friendly as it had terrible looking URL's, looking much like this 

> https://ronaldlangeveld.com/?blog%2Fdowntimebot

What the hell? 2018 here! (that link will not work)

Last attempt was Jekyll. On 'paper' it looks amazing. No database, easy to customise, easy to read URL's and works with Github Pages... In reality it was another nightmare installing Ruby, the dependencies and I couldn't figure out how to create a new theme for the hell of it no matter how many tutorials I followed.

Back to square 1. 

## Time to build:
After all that, I finally decided to start my own CMS. I will keep it as lightweight as possible, open-source and modular so that developers can add new features if they need to.

At first I thought I'd make this new blogging CMS with Django - but as much as I like Django, it's a bloody huge framework and just using that destroys the purpose of keeping the whole thing small and lightweight, so I better reconsider. 

## Meeting Flask:

As a Python developer, I didn't want to use any other programming language like PHP, Ruby or NodeJS. 
My brother recommended I check out [Flask](http://flask.pocoo.org/), as its super lightweight. I have looked at in the past, but always got nervous because it's "lacking" features compared to Django. But whatever, I still have to try.

After following the getting started instructions on Flask's website I got it installed in under 3 mins and ready to start messing around with the code and without even realising, I had my index.html page showing.... faster than I could ever get that with Django.

## Let the hacking begin:
I started off by playing around and setting up the URL's etc, as well as figuring out which dependencies to use. I also started playing around to see how I'd loop the Markdown files within a folder, as I will be making this blog Admin-less and database-less. This is pretty much the start of Flat File Flask Blog (FFFB).

## Getting Contributors:
It was getting late already so I decided to push everything to github and start a new repository. Also, writing a detailed Readme.MD on your Github repo is important to make sure everyone understands exactly what should be done and what shouldn't be done. After I did that, I tweeted what I'm making and to see if I could interest any of my followers (and those following #Python & #Flask).

<blockquote class="twitter-tweet" data-cards="hidden" data-lang="en-gb"><p lang="en" dir="ltr">Any <a href="https://twitter.com/hashtag/python?src=hash&amp;ref_src=twsrc%5Etfw">#python</a> and <a href="https://twitter.com/hashtag/flask?src=hash&amp;ref_src=twsrc%5Etfw">#flask</a> enthusiasts who wants to join. I&#39;m creating a super simple databaseless blogging cms kinda thing. <br>Get involved. <a href="https://t.co/whUExe9qOn">https://t.co/whUExe9qOn</a></p>&mdash; Ronald @ 🌴 (@ronaldl93_) <a href="https://twitter.com/ronaldl93_/status/952217837447385088?ref_src=twsrc%5Etfw">13 January 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


After about an hour (I was asleep already) this legend, [Luuc Verburgh](https://twitter.com/luucvp) from the Netherlands replied. 


<blockquote class="twitter-tweet" data-conversation="none" data-lang="en-gb"><p lang="en" dir="ltr">Open it up!! haha <a href="https://t.co/AGFEiLEQLn">pic.twitter.com/AGFEiLEQLn</a></p>&mdash; Luuc Verburgh (@luucvp) <a href="https://twitter.com/luucvp/status/952281202467266560?ref_src=twsrc%5Etfw">13 January 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>



The next morning I gave him access to the repository so he can push and pull from the git as he pleases.

Luuc is also in the [wip.chat](https://wip.chat/) telegram group, so I could easily find him on Telegram and where could send each other occasionally a message should we need to confirm something. 

## Production Ready?
On Tuesday evening, Luuke pushed the final crucial part of the CMS to the repository that would classify this as a fully functional blogging software. 
I hooked up the rest to the [jinja](http://jinja.pocoo.org/) templates and it was ready to be used. The first basic, concept version of Flat File Flask Blog was officially done in 3 days. And it does exactly what I want it to do that other CMS software doesn't.

 - It doesn't have a database
 - No Admin
 - No passwords
 - Lightweight
 - Can push / pull updates on git without breaking the site.
 - I can customise my URLs
 - Easy to template

## Can I help to make FFFB Better?

[Visit the repo here.](https://github.com/burgundy93/FlatFileFlaskBlog)

Feel free to contribute and / or fork it.
